from app.all_routes import * 

@app.route('/signup' ,  methods=['GET', 'POST'])
def signup():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            username = request.form['username']
            print(f'{email}-{username}-{password}')
            
            existing_email = Users.query.filter_by(email=email).first()
            existing_user_username = Users.query.filter_by(username=username).first()
            
            if existing_email:
                flash('Email is already taken. Please choose another.', 'error')
            elif existing_user_username:
                flash('Username is already taken. Please choose another.', 'error')
                
            else:
                session['email'] =email
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                join_dt = datetime.now()
                verification_hash = secrets.token_urlsafe(16)
                otp_num , otp_generated_datetime , otp_expiration_time = generate_otp()
                
                user = Users(
                    join_dt = join_dt,
                    username = username,
                    email = email,
                    password = hashed_password,
                    verification_hash = verification_hash,
                )
                db.session.add(user)
                db.session.commit()
                
                user = Users.query.filter_by(email=email).first()
                session['user_id'] = user.id
                send_verification_email(user.id , otp_num)
                otp = Otp(user_id=user.id , email=user.email , time_stamp=datetime.now() , otp=otp_num, otp_generated_datetime=otp_generated_datetime , otp_expiration_time=otp_expiration_time)
                db.session.add(otp)
                db.session.commit()
                return redirect(url_for('please_verify_email'))
                
                
                
            
            # flash('Login successful!', 'success')
            
        return render_template('pages/signup.html')
    

def generate_otp():
    now = datetime.now()
    otp = random.randint(100000, 999999)
    current_time = now.strftime("%H:%M:%S")
    a = now + timedelta(minutes=1, seconds=30)
    otp_expiration_time = a

    return otp, current_time , otp_expiration_time

def send_verification_email(user_id, verification_otp):
    user = Users.query.get(user_id)
    if user:
        verification_url = url_for('verify_email', verification_hash=user.verification_hash, _external=True)
        subject = 'Email Verification for Your Account'
        body = f'Thank you for registering! Please click the following link to verify your email:\n\n{verification_url}\n\nYour verification OTP is: {verification_otp}'

        send_email(user.email, subject, body)

def send_email(email, subject, body):
    msg = Message(subject, recipients=[email], body=body)
    mail.send(msg)