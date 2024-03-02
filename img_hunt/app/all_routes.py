from app import app , db , bcrypt , mail , Message
from flask import render_template, request, redirect, url_for, flash, session
from app.models import Users , Otp , LoginInfo ,  Post
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
import secrets
import random

from app.routes.home import home 
from app.routes.signup import signup , generate_otp , send_email , send_verification_email
from app.routes.login import login
from app.routes.verify_email import verify_email , please_verify_email , resend 
from app.routes.profile_onboarding import profile_onboarding
from app.routes.create_post import create_post
from app.routes.profile import profile
from app.routes.profile_edit import profile_edit
from app.routes.delete import delete