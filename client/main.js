const INDEXER_URL = "http://localhost:8980";

function getUserData(){
	const request = new XMLHttpRequest();
	request.onreadystatechange = () => {
		if(request.readyState === XMLHttpRequest.DONE) {
			if(request.status < 300) {
				console.log(request.responseText);
			} else {
				console.warn("ERROR");
			}
		}
	}
	request.open("GET", INDEXER_URL + "/v2/assets");
	request.send();
	return JSON.parse(request.responseText).assets;
}

function reloadUserData(){
	const data = getUserData();
}
