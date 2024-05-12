from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__, template_folder='./templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/ltPanel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'ltPanel'

CORS(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
ma = Marshmallow(app)

@app.after_request
def apply_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response