from flask import Flask, request, Response
from create_certificate import create_certificate
from create_acc import create_acc
import os.path

app = Flask(__name__, static_folder='user_content')

user = None

def upload_to_server(file):
	file.save(os.path.join('user_content', file.filename))
	return "http://localhost:5000/static/" + file.filename

@app.route('/upload', methods=['POST'])
def create():
	file = request.files['certificate']
	filename = file.filename
	file_url = upload_to_server(file)
	print(user['pk'])
	create_certificate(user, file.read(), file_url)
	return Response('Created', status=201)

if __name__ == "__main__":
	user = create_acc()
	print('Using user with private key', user['pk'])
	app.run()
