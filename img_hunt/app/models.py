from app import db 

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    join_dt = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False , default='none')
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    verification_hash = db.Column(db.String(255), default='pending_verification')
    verified_at = db.Column(db.String(255))
    avatar = db.Column(db.Text()  , default='https://i.pinimg.com/564x/f7/58/d1/f758d179886f5a81f47eef9e7605d9b9.jpg')
    otp_verified = db.Column(db.String(255) , default = 'no')
    bio = db.Column(db.Text()) 
    posts = db.Column(db.String(255)) #number of posts
    is_verified = db.Column(db.Boolean() , default=False )
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    def __init__(self , join_dt , username , email, password, verification_hash) :
        self.join_dt = join_dt
        self.username = username
        self.email = email
        self.password = password
        self.verification_hash = verification_hash
        

class Otp(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    time_stamp = db.Column(db.Date, nullable=False)
    otp = db.Column(db.Integer , nullable=False)
    otp_generated_datetime = db.Column(db.String(255) , nullable=False )
    otp_expiration_time = db.Column(db.String(255) , nullable=False )
    
    def __init__(self, user_id, email , time_stamp , otp  , otp_generated_datetime , otp_expiration_time):
      self.user_id = user_id
      self.email = email
      self.time_stamp = time_stamp
      self.otp = otp
      self.otp_generated_datetime = otp_generated_datetime
      self.otp_expiration_time =otp_expiration_time
      
class LoginInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_agent = db.Column(db.Text)
    os = db.Column(db.Text)
    city = db.Column(db.Text)
    telecom_service_provider = db.Column(db.Text)
    country = db.Column(db.Text)
    region = db.Column(db.Text)
    ip_address = db.Column(db.Text)
    timestamp = db.Column(db.Text)  # Add the new column

    def __init__(self, users_id, user_agent, os, city, telecom_service_provider, country, region, ip_address, timestamp):
        self.users_id = users_id
        self.user_agent = user_agent
        self.os = os
        self.city = city
        self.telecom_service_provider = telecom_service_provider
        self.country = country
        self.region = region
        self.ip_address = ip_address
        self.timestamp = timestamp
        
class Post(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.Text)
    caption = db.Column(db.Text)
    
    def __init__(self, users_id, url, caption):
        self.users_id = users_id
        self.url = url
        self.caption = caption
