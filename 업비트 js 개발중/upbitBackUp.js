const axios = require("axios");
const crypto = require("crypto");
const pako = require("pako");
const capmonster = require('capmonster');

const DDAY = new Date("2022-04-20T18:00:10");
const tokenArr = ["Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTg5ODcyfQ.tMDEXIYF5YJiydObjgSsC9x0Zx-mRoK0kip9ZpvEr_w",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTkwODU0fQ.HLCR5gZYQ7RmKJ8aX331d6emMjs3hDrtR5nD2yqmB3w",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTkxODYxfQ.NOB0n084MY7PS7zySqA5GbSLHre79gZzYhEaL3r-E7Y",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTkyODM5fQ.B4AUn5JDfOS3P_DLwMU8LDaiRiHLvvNRl1_4PdU_dEo",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTkzODM2fQ.VetotBMmvQExVGx_8gi-aYagCSgMRhwYNRAzdSJjdRY",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTk0ODQzfQ.u7LjLBdNUuDacNejg7EuNxpBwvilq67rV9ufgmppC5A",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTk1ODU2fQ.C4qT1jmWcAdXPbsJjQed8KUwORERRoWs5FAaxDS_hNA",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTk2ODY4fQ.ctWT7fU68mRLz5IQqS1__EGbkD3UKI1haJ2mBCd2Ui4",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTk3ODY2fQ.zQw4hOxVSofClmo894qAzygZD33R9EhuFrnoFq1w4gA",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTk4Nzk5fQ.R8TunV65NTnBbpRz5LhLE8graxV3R9TwXZTFUxkyZ7U",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NTk5ODMxfQ.ZA6YLGG5QKVL0K3J2SmSvm5Tk--saAyt1mcDYDa810I",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NjAwODEwfQ.zqoQFTPR7kF2IH_1R-dbvpTK252zX0rpioOsWxpqpWo",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NjAxNzkyfQ.k0naltcPZgxB17ZSJV8JCalS2z34N0U1a0ZvHVJmoaA",
"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3Nfa2V5IjoiZHBzUFFWcjhGNENxZnZTQVhNenNRUzhTYzJqQ3NDcXZQWnV0UDRhQSIsIm5vbmNlIjoxNjUwNDQ0NjAyODA2fQ.SWu6_JAIXDYqjTC6Ejho6GI9U5SaTLPgtoHrJVOgRQ4"];
const nftArr = ["2c6566e6-0514-42c8-95aa-4151f6551be7",
"871d0857-296b-4fc9-9f0c-de5a4a22b3e1",
"1bb9f5ac-19c2-4cd4-be37-a4311205da79"];
const bidVolume = 1;

const captcha = new capmonster('fa75f054590f219728526f71efacd3bf');

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

async function captchaSolver(image) {
    const start = Date.now();
    let task = await captcha.createTask({
        type: 'ImageToTextTask',
        body: image,
    });
    console.log(task);
    try {
        let result = await captcha.getResult(task.taskId);
        console.log(result.solution.text);
        console.log((Date.now() - start)/1000);
        return result.solution.text;
    } catch (e) {
        throw e;
    }
};

const config = (token) => {
    return {
      headers: {
        Authorization: token,
      },
    };
};

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
};

const upbitBuyer = async (nft) => {
    do {
        const lastCount = DDAY - Date.now();
        await sleep(lastCount < 13000 ? 500 : 1000);
        console.log(`captcha image not yet ${new Date().toString()}`);
        let dropState = "SCHEDULED";
        console.log(lastCount/1000);
        if (lastCount < 13000) {
            const getState = await axios.get(
                `https://ccx.upbit.com/nx/v1/fixed-price-auctions/${nft}`);
        dropState = getState.data.state;
        }
    console.log(dropState);
    if (dropState !== "SCHEDULED") {
        let token = tokenArr.pop();
        await sleep(100);
        try {
            const captchaRes = await axios.post(
                `https://ccx.upbit.com/nx/v1/auction-captcha?auctionUuid=${nft}`,
                {},
                config(token)
            );
            const uri = decrypt(captchaRes.data.image);
            const text = await captchaSolver(uri);
            token = tokenArr.pop();
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
    for (const nft of nftArr) {
        promises.push(upbitBuyer(nft));
    }
    await Promise.allSettled(promises);
};

main();