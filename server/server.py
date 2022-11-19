from flask import Flask
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/create", methods=['POST'])
def create_cert():
	f = request.files['file']
	print(f)
	return "Success"
