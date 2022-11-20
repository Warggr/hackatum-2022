const INDEXER_URL = "http://127.0.0.1:8980";

'use strict';

const e = React.createElement;

const reactDomContainer = document.querySelector('#persons');
const root = ReactDOM.createRoot(reactDomContainer);

async function ajax(method, url){
	const request = new XMLHttpRequest();
	return new Promise((resolve, reject) => {
		request.onreadystatechange = () => {
			if(request.readyState === XMLHttpRequest.DONE) {
				if(request.status < 300) resolve(request.responseText);
				else reject(request);
			}
		}
		request.open(method, url);
		request.send();
	});
}

class MiniHeader extends React.Component {
	render(){
		return e('div', {className: "mini-header"},
			e('h3', {}, this.props.username),
			e('img', {src: this.props.profile_pic}),
			e('div', {className: "about"}, this.props.about)
		);
	}
}

class DocumentView extends React.Component {
	render(){
		let extension = this.props.asset.params.url.split('.').slice(-1);
		let icon = extension == 'pdf' ? 'pdf_icon.png' :
				   extension == 'json' ? 'icon_json.png' :
				   extension == 'py' ? 'icon_python.png' :
				   'icon_graph.png';

		return e('div', {className: "col-md-3", key: this.props.asset.params.name}, [
			e('a', {href: this.props.asset.params.url},
			e('div', {}, [
				e('h5', {}, this.props.asset.params.name),
				e('img', {src: "resources/" + icon, style: {height: "160px", align: "center"}}, null)
			])
			)
		]);
	}
}

async function reloadUserData(){
	const data = await ajax('GET', INDEXER_URL + "/v2/accounts")
	.then(data_string => {
		const data = JSON.parse(data_string);
		console.log(data);
		const accounts = data.accounts;
		let assets = {};
		for(let account of accounts){
			if(account['created-assets']) for(let asset of account['created-assets']){
				if(assets[asset.index]){
					assets[asset.index].creator = account.address;
					assets[asset.index].data = asset;
				} else {
					assets[asset.index] = { creator : account.address, data: asset };
				}
			}
			if(account['assets']) for(let asset of account['assets']){
				if(assets[asset['asset-id']]){
					assets[asset['asset-id']].owner = account.address;
				} else {
					assets[asset['asset-id']] = { owner: account.address };
				}
			}
		}
		let assets_by_users = {};
		for(let assetId in assets){
			let asset = assets[assetId];
			if(assets_by_users[asset.owner]) assets_by_users[asset.owner].push(asset);
			else assets_by_users[asset.owner] = [ asset ];
		}
		allUsersReact = [];
		for(let user in assets_by_users){
			let allAssetsReact = [];
			let name = user;
			let profile_url = 'resources/mock_profile.jpg';
			let about = 'No additional information entered.';
			for(let asset of assets_by_users[user]){
				if(asset.data.params.name == '.profile.meta'){
					profile_url = asset.data.params.url;
				} else if(asset.data.params.name == '.name.meta'){
					name = asset.data.params.url.substr(8).replaceAll('+', ' ');
				} else {
					allAssetsReact.push( e(DocumentView, {asset:asset.data}, null) );
				}
			}

			let miniHeaderReact = e(MiniHeader, {username:name, profile_pic:profile_url, about:about}, null);

			let documentsReact = e('div', { className: "docs documents" }, [
				e('h4', {}, 'Documents'),
				e('div', { className: "container"},
					e('div', { className: "row" },
						allAssetsReact
					)
				)
			]);
			allUsersReact.push( e('div', { key: user }, [miniHeaderReact, documentsReact]) );
		}
		if(allUsersReact.length == 0) root.render( 'No data :(' );
		else root.render( allUsersReact );
	})
	.catch(_err => { console.warn(_err); root.render('Error when reloading data'); } );
}
