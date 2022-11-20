from flask import Flask, request, Response, send_file
from create_certificate import create_certificate
from create_acc import create_acc
import os.path

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', 'content')
WEB_FILES = os.path.join(os.path.dirname(__file__), '..', '..', 'client')

print(UPLOAD_DIR, WEB_FILES)

app = Flask(__name__, static_folder='content')

user = None

def upload_to_server(file):
	file.save(os.path.join(UPLOAD_DIR, file.filename))
	return "http://localhost:5000/content/" + file.filename

@app.route('/upload', methods=['POST'])
def create():
	file = request.files['certificate']
	filename = file.filename
	file_url = upload_to_server(file)
	create_certificate(user, file.read(), file_url)
	return Response('Created', status=201)

@app.route('/web/<path:filepath>')
def send_static(filepath):
	return send_file(os.path.join(WEB_FILES, filepath))

if __name__ == "__main__":
	user = create_acc()
	print('Using user with private key', user['pk'])
	app.run()
