from flask import Flask, render_template, request, redirect, url_for, flash , session
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask_migrate import Migrate
import requests
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9375160975@localhost/img_hunt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '2123342242232342'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'patwarinetra@gmail.com'
app.config['MAIL_PASSWORD'] = 'wkms pxgn anes sjxq'
app.config['MAIL_DEFAULT_SENDER'] = 'patwarinetra@gmail.com'


mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

from app import all_routes