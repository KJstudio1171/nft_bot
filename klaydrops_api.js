QR = ""

fetch("https://api.klipdrops.com/v2/market/token/0xa9a95c5fef43830d5d67156a2582a2e793acb465/10001800150003/purchase",{
	method:"POST",
	credentials : 'include',
	headers:{
		"Content-Type":"application/json;charset=UTF-8",
	},
	body:JSON.stringify({
		transfer_agreement: true,
		transfer_agreement_at: "2022-02-08T11:04:40+09:00"}),}
	).then((response)=>response.json()).then((data)=>{
	QR = data;
	fetch("https://api.klipdrops.com/v2/wallet/klip/result?request_key=" + QR.request_key,{
	method:"GET",
	credentials : 'include',
	}).then((response)=>response.json()).then((data)=>console.log(data));
	console.log("https://klipwallet.com/?target=/a2a?request_key="+QR.request_key);}
	)

QR = ""

fetch("https://api.klipdrops.com/v2/dfactory/drops/fixed/1000260008/buy",{
	method:"POST",
	credentials : 'include',
	headers:{
		"Content-Type":"application/json;charset=UTF-8",
	},
	body:JSON.stringify({
		transfer_agreement: true,
		transfer_agreement_at: "2022-02-09T09:00:02+09:00"}),}
	).then((response)=>response.json()).then((data)=>{
	QR = data;
	fetch("https://api.klipdrops.com/v2/dfactory/drops/fixed/1000190021/result?request_key=" + QR.request_key,{
	method:"GET",
	credentials : 'include',
	}).then((response)=>response.json()).then((data)=>console.log(data));
	console.log("https://klipwallet.com/?target=/a2a?request_key="+QR.request_key);}
	)

fetch("https://api.klipdrops.com/v2/market/token/0xa9a95c5fef43830d5d67156a2582a2e793acb465/10001900240004/purchase", {
  "headers": {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  "referrer": "https://klipdrops.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"transfer_agreement\":true,\"transfer_agreement_at\":\"2022-04-05T12:09:04+09:00\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then((response)=>response.json()).then((data)=>{
	QR = data;
	fetch("https://api.klipdrops.com/v2/wallet/klip/result?request_key=" + QR.request_key,{
	method:"GET",
	credentials : 'include',
	}).then((response)=>response.json()).then((data)=>console.log(data));
	console.log("https://klipwallet.com/?target=/a2a?request_key="+QR.request_key);}
);
copy("https://klipwallet.com/?target=/a2a?request_key="+QR.request_key);

// 번호와 시간을 바꾸고 사용하면 됩니다.
fetch("https://api.klipdrops.com/v2/dfactory/drops/fixed/1000180026/buy", {
  "headers": {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  "referrer": "https://klipdrops.com/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "{\"transfer_agreement\":true,\"transfer_agreement_at\":\"2022-04-10T09:00:11+09:00\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
}).then((response)=>response.json()).then((data)=>{
	QR = data;
	fetch("https://api.klipdrops.com/v2/wallet/klip/result?request_key=" + QR.request_key,{
	method:"GET",
	credentials : 'include',
	}).then((response)=>response.json()).then((data)=>console.log(data));
	console.log("https://klipwallet.com/?target=/a2a?request_key="+QR.request_key);}
);
copy("https://klipwallet.com/?target=/a2a?request_key="+QR.request_key);