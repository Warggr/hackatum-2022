from flask import Flask, request, Response, send_file
from create_certificate import create_certificate
from create_acc import create_acc
from transaction import optIn, transferAssets
import os.path

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'content')
WEB_FILES = os.path.join(os.path.dirname(__file__), '..', '..', 'client')

print(UPLOAD_DIR, WEB_FILES)

app = Flask(__name__, static_folder='content')

user1 = None
user2 = None
assetId = None

def upload_to_server(file):
	file.save(os.path.join(UPLOAD_DIR, file.filename))
	return "http://localhost:5000/content/" + file.filename

@app.route('/upload', methods=['POST'])
def create():
	file = request.files['certificate']
	filename = file.filename
	file_url = upload_to_server(file)
	assetId = create_certificate(user1, file.read(), file_url)
	return Response(assetId, status=201)

@app.route('/transfer/<int:assetId>', methods=['POST'])
def transfer(assetId):
	print('During transfer, assetID is', assetId)
	print('During transfer, user2 is', user2)
	optIn(user2, assetId)
	transferAssets(user1, user2, assetId)
	return Response('Done', 200)

@app.route('/web/<path:filepath>')
def send_static(filepath):
	return send_file(os.path.join(WEB_FILES, filepath))

if __name__ == "__main__":
	user1 = create_acc()
	user2 = create_acc()
	print('Using user with public key', user1['pk'])
	print('Using user with public key', user2['pk'])
	app.run()
