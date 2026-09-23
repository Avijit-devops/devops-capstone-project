"""
Service Package Initialization with Talisman Security and CORS Policies
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devops-capstone-secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'object-src': '\'none\''
    },
    force_https=False
)

CORS(app)

from service import routes, models
