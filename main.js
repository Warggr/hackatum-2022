const INDEXER_URL = "http://localhost:8980";

function getUserData(){
	/*
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
	*/
	const MOCK_DATA = [
		{ "type": "certificate", "owner": "Mock User", "name": "Bachelor's Degree", "signed-by": "TUM", "text": "Lorem Ipsum" },
		{ "type": "certificate", "owner": "Mock User", "name": "Master's Degree", "signed-by": "TUM", "text": "Lorem Ipsum" },
		{ "type": "document", "owner": "Mock User", "name": "CV", "signed-by": "Mock User", "text": "Lorem Ipsum" }
	];
	return MOCK_DATA;
}

function reloadUserData(){
	const data = getUserData();
}
