const INDEXER_URL = "http://131.159.214.36:8980";

'use strict';

const e = React.createElement;

const reactDomContainer = document.querySelector('#persons');
const root = ReactDOM.createRoot(reactDomContainer);

const MOCK_DATA = "{\"assets\":[{\"created-at-round\":5808,\"deleted\":false,\"index\":25,\"params\":{\"clawback\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"creator\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"decimals\":0,\"default-frozen\":false,\"freeze\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"manager\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"metadata-hash\":\"BWsshv3w9VJTJEw3jnnxQpT8nJ0sWdjmrjiSDXeLu+A=\",\"name\":\"Alice's Artwork Coins@arc3\",\"name-b64\":\"QWxpY2UncyBBcnR3b3JrIENvaW5zQGFyYzM=\",\"reserve\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"total\":1000,\"unit-name\":\"ALICEOI\",\"unit-name-b64\":\"QUxJQ0VPSQ==\",\"url\":\"https://path/to/my/asset/details\",\"url-b64\":\"aHR0cHM6Ly9wYXRoL3RvL215L2Fzc2V0L2RldGFpbHM=\"}},{\"created-at-round\":5855,\"deleted\":false,\"index\":26,\"params\":{\"clawback\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"creator\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"decimals\":0,\"default-frozen\":false,\"freeze\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"manager\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"metadata-hash\":\"BWsshv3w9VJTJEw3jnnxQpT8nJ0sWdjmrjiSDXeLu+A=\",\"name\":\"Alice's Artwork Coins@arc3\",\"name-b64\":\"QWxpY2UncyBBcnR3b3JrIENvaW5zQGFyYzM=\",\"reserve\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"total\":1000,\"unit-name\":\"ALICEOI\",\"unit-name-b64\":\"QUxJQ0VPSQ==\",\"url\":\"https://path/to/my/asset/details\",\"url-b64\":\"aHR0cHM6Ly9wYXRoL3RvL215L2Fzc2V0L2RldGFpbHM=\"}},{\"created-at-round\":5934,\"deleted\":false,\"index\":28,\"params\":{\"clawback\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"creator\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"decimals\":0,\"default-frozen\":false,\"freeze\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"manager\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"metadata-hash\":\"BWsshv3w9VJTJEw3jnnxQpT8nJ0sWdjmrjiSDXeLu+A=\",\"name\":\"Alice's Artwork Coins@arc3\",\"name-b64\":\"QWxpY2UncyBBcnR3b3JrIENvaW5zQGFyYzM=\",\"reserve\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"total\":1000,\"unit-name\":\"ALICEOI\",\"unit-name-b64\":\"QUxJQ0VPSQ==\",\"url\":\"https://path/to/my/asset/details\",\"url-b64\":\"aHR0cHM6Ly9wYXRoL3RvL215L2Fzc2V0L2RldGFpbHM=\"}},{\"created-at-round\":6026,\"deleted\":false,\"index\":29,\"params\":{\"clawback\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"creator\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"decimals\":0,\"default-frozen\":false,\"freeze\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"manager\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"metadata-hash\":\"BWsshv3w9VJTJEw3jnnxQpT8nJ0sWdjmrjiSDXeLu+A=\",\"name\":\"Alice's Artwork Coins@arc3\",\"name-b64\":\"QWxpY2UncyBBcnR3b3JrIENvaW5zQGFyYzM=\",\"reserve\":\"DRL6BOQDJ7FMLLP35DCUOQFFOOIYBLZPD7YO4BTN2PBLZLM7EPEWDBSU74\",\"total\":1000,\"unit-name\":\"ALICEOI\",\"unit-name-b64\":\"QUxJQ0VPSQ==\",\"url\":\"/home/programmer/Hackatum/aliceAssetMetaData.json\",\"url-b64\":\"L2hvbWUvcHJvZ3JhbW1lci9IYWNrYXR1bS9hbGljZUFzc2V0TWV0YURhdGEuanNvbg==\"}}],\"current-round\":6973,\"next-token\":\"29\"}";

async function getUserData(){
	const request = new XMLHttpRequest();
	return new Promise((resolve, reject) => {
		// resolve(MOCK_DATA);
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

const LOREM_IPSUM = 'Omnis illo minima quaerat eveniet sed deserunt dolor ducimus. Et explicabo quia et ad quisquam reiciendis. Blanditiis tenetur assumenda et voluptas voluptatum est impedit possimus. Molestiae animi saepe laborum. Est ut sed possimus ut. Provident aut eligendi nemo consequuntur sit voluptatibus est.';

class MiniHeader extends React.Component {
	render(){
		return e('div', {className: "mini-header"},
			e('h3', {}, this.props.user),
			e('img', {src: 'resources/mock_profile.jpg'}),
			e('div', {className: "about"}, LOREM_IPSUM)
		);
	}
}

class DocumentView extends React.Component {
	render(){
		return e('div', {className: "col-md-3", key: this.props.asset.name}, [
			e('div', {}, [
				e('h5', {}, this.props.asset.name),
				e('img', {src: "resources/pdf_icon.png", style: {height: "160px", align: "center"}}, null)
			])
		]);
	}
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
		allUsersReact = [];
		for(let user in assets_by_user){
			let miniHeaderReact = e(MiniHeader, {user:user}, null);
			let documentsReact = e('div', { className: "docs documents" }, [
				e('h4', {}, 'Documents'),
				e('div', { className: "container"},
					e('div', { className: "row" },
						assets_by_user[user].map(asset => e(DocumentView, {asset:asset}, null))
					)
				)
			]);
			allUsersReact.push( e('div', { key: user }, [miniHeaderReact, documentsReact]) );
		}
		if(allUsersReact.length == 0) root.render( 'No data :(' );
		else root.render( allUsersReact );
	})
	.catch(_err => root.render('Error when reloading data') );
}
