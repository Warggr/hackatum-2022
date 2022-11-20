from flask import Flask, request, Response, send_file
from create_certificate import create_certificate, give_name
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

def upload_to_server(file, username):
	filename = username[:16] + file.filename
	file.save(os.path.join(UPLOAD_DIR, filename))
	return "http://localhost:5000/content/" + filename

@app.route('/upload', methods=['POST'])
def create():
	file = request.files['certificate']
	filename = file.filename
	if len(filename) > 32:
		filename = filename[:16] + filename[-16:]
	file_url = upload_to_server(file, user1['sk'])
	print('URL: ', file_url)
	assetId = create_certificate(user1, file.read(), filename, file_url)
	# asset names are limited to 32 char, and we want to keep the extension
	return Response(str(assetId), status=201)

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
	give_name(user1, 'Technical University of Munich')
	give_name(user2, 'Example Student')
	print('Using user with public key', user1['pk'])
	print('Using user with public key', user2['pk'])
	app.run()
