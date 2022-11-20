const INDEXER_URL = "http://131.159.214.36:8980";

'use strict';

const e = React.createElement;

const reactDomContainer = document.querySelector('#persons');
const root = ReactDOM.createRoot(reactDomContainer);

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

const LOREM_IPSUM = 'Omnis illo minima quaerat eveniet sed deserunt dolor ducimus. Et explicabo quia et ad quisquam reiciendis. Blanditiis tenetur assumenda et voluptas voluptatum est impedit possimus. Molestiae animi saepe laborum. Est ut sed possimus ut. Provident aut eligendi nemo consequuntur sit voluptatibus est.';

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
		let extension = this.props.asset.url.split('.').slice(-1);
		let icon = extension == 'pdf' ? 'pdf_icon.png' :
				   extension == 'json' ? 'icon_json.png' :
				   extension == 'py' ? 'icon_python.png' :
				   'icon_graph.png';

		return e('div', {className: "col-md-3", key: this.props.asset.name}, [
			e('a', {href: this.props.asset.url},
			e('div', {}, [
				e('h5', {}, this.props.asset.name),
				e('img', {src: "resources/" + icon, style: {height: "160px", align: "center"}}, null)
			])
			)
		]);
	}
}

async function reloadUserData(){
	const data = await getUserData()
	.then(data_string => {
		const data = JSON.parse(data_string);
		console.log(data);
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
			let profile_url;
			let profile_pic = assets_by_user[user].find(e => e.name == '.profile.meta');
			if(profile_pic){ profile_url = profile_pic.url; assets_by_user[user] = assets_by_user[user].filter(e => e.name != '.profile.meta'); }
			else {  profile_url = 'resources/mock_profile.jpg'; }

			let name;
			let name_data = assets_by_user[user].find(e => e.name == '.name.meta');
			if(name_data){ name = name_data.url.substr(8); assets_by_user[user] = assets_by_user[user].filter(e => e.name != '.name.meta'); }
			else { name = user; }

			let about = 'No additional information entered.';

			let miniHeaderReact = e(MiniHeader, {username:name, profile_pic:profile_url, about:about}, null);
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
