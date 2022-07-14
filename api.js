fetch("https://api.nu-world.io/pre-users/add",{
	method:"POST",
	body:JSON.stringify({
		email: "btime754@gmail.com",
		addr: "0x449A735E5Bf1a5113F37E84BBAFF8A88e6C92d3e",
		walletType: 2,
		nickName:"rerere#9205"}),}
	).then((response)=>console.log(response))