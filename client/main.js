const INDEXER_URL = "http://131.159.214.36:8980";

async function getUserData(){
	const request = new XMLHttpRequest();
	return new Promise((resolve, reject) => {	
		request.onreadystatechange = () => {
			if(request.readyState === XMLHttpRequest.DONE) {
				if(request.status < 300) resolve(request.responseText);
				else reject(request);
			}
		}
		request.open("GET", INDEXER_URL + "/v2/assets");
		request.send();
	});
}

async function reloadUserData(){
	const data = await getUserData()
	.then(data_string => {
		const data = JSON.parse(data_string);
		const assets = data.assets;
		let assets_by_user = {};
		for(let asset of assets){
			if(assets_by_user[asset.params.manager])
				assets_by_user[asset.params.manager].push(asset.params);
			else
				assets_by_user[asset.params.manager] = [ asset.params ];
		}
		for(let user in assets_by_users){
			for(let asset of assets_by_users[user]){

			}
		}
	});
	return data;
}
