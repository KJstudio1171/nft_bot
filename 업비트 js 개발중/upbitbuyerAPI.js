const axios = require("axios");
const crypto = require("crypto");
const pako = require("pako");
const capmonster = require('capmonster');

const DDAY = new Date("2022-04-20T18:00:10");
const tokenArr = [];
const nft = "2c6566e6-0514-42c8-95aa-4151f6551be7";
const bidVolume = 1;

const captcha = new capmonster('fa75f054590f219728526f71efacd3bf');

async function captchaSolver(image) {
    const start = Date.now();
    let task = await captcha.createTask({
        type: 'ImageToTextTask',
        body: image,
    });
    try {
        let result = await captcha.getResult(task.taskId);
        console.log(`CAPTCHA TIME: ${(Date.now() - start)/1000}second`);
        return result.solution.text;
    } catch (e) {
        throw e;
    }
};

const decrypt = (source) => {
    const i = Buffer.from(source, "base64");
    const pakoI = pako.ungzip(i);
    const password = Buffer.from(pakoI).toString("base64");

    let key = Buffer.from(
        "Fb9VWgbm5fbL9Me50+CzmTTz+vWPwtXRD8S2xy8mJRM=",
        "base64"
    );
    let iv = key.slice(0, 16);
    let cipher = crypto.createDecipheriv("aes-256-cbc", key, iv);
    let decrypted = cipher.update(password, "base64", "base64");
    decrypted += cipher.final("base64");
    return `data:image/png;base64,${decrypted}`;
};

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
};

const config = (token) => {
    return {
      headers: {
        Authorization: token,
      },
    };
};

const upbitBuyer = async (nft) => {
    do {
        const lastCount = DDAY - Date.now();
        await sleep(lastCount < 1500 ? 50 : 500);
        console.log(`captcha image not yet ${new Date().toString()}`);
        let dropState = "SCHEDULED";
        if (lastCount < 1500) {
            const getState = await axios.get(
                `https://ccx.upbit.com/nx/v1/fixed-price-auctions/${nft}`);
        dropState = getState.data.state;
        }
    if (dropState !== "SCHEDULED") {
        let token = tokenArr.pop();
        console.log(`DROPS OPEN!!! ${new Date().toString()}`);
        await sleep(10);
        try {
            const captchaRes = await axios.post(
                `https://ccx.upbit.com/nx/v1/auction-captcha?auctionUuid=${nft}`,
                {},
                config(token)
            );
            const uri = decrypt(captchaRes.data.image);
            const text = await captchaSolver(uri.split(",")[1]);
            token = tokenArr.pop();
            console.log(token);
            const result = await axios.post(
                `https://ccx.upbit.com/nx/v1/fixed-price-auctions/${nft}/bids`,
                {
                    captchaUuid:captchaRes.data.uuid,
                    code:text,
                    volume:bidVolume,
                },
                config(token)
            );
            console.log(result);
        } catch (e) {
          console.log(e.response.data);
        }
    }
  } while (Date.now() < DDAY);
};

async function main()
{
    const promises = [];
    promises.push(upbitBuyer(nft));
    await Promise.allSettled(promises);
};

main();