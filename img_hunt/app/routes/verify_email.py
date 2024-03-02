from app.all_routes import * 

@app.route('/verify_email/<verification_hash>', methods=['GET' , 'POST'])
def verify_email(verification_hash):
    user = Users.query.filter_by(verification_hash=verification_hash).first()
    if not user:
        return redirect(url_for('login'))
    otp = Otp.query.filter_by(email=user.email).first()
    otp_generated_datetime = otp.otp_generated_datetime
    
    t1 = datetime.strptime(otp_generated_datetime, "%H:%M:%S")
    
    now = datetime.now()
    t2 = datetime.strptime(now.strftime("%H:%M:%S"), "%H:%M:%S")
    
    delta = t2 - t1
    seconds = delta.total_seconds()
    

    if request.method == 'POST' or request.form.get('_method') == 'PATCH':
        entered_otp = request.form['otp']
        stored_otp = otp.otp
    
        if stored_otp and entered_otp.isdigit() and int(entered_otp) == int(stored_otp) and seconds <= 90:
            user.verified_at = datetime.now()
            user.otp_verified = 'true'
            user.verification_hash = secrets.token_urlsafe(16)
            session['user_id'] = user.id
            db.session.commit()
            return redirect(url_for('profile_onboarding', username=user.username))
        else:
             flash('OTP not matched or expired', 'error')  

    return render_template('pages/otp_verification.html', user=user, otp_expiration_time=otp.otp_expiration_time)




@app.route('/resend/<verification_hash>', methods=['POST'])
def resend(verification_hash):
    if request.method == 'POST' or request.form.get('_method') == 'PATCH':
        user = Users.query.filter_by(verification_hash=verification_hash).first()
        otp = Otp.query.filter_by(email=user.email).first()
        otp_num, generated_otp_datetime, otp_expiration_time = generate_otp()

        otp.otp = otp_num
        otp.generated_otp_datetime = generated_otp_datetime
        otp.otp_expiration_time = otp_expiration_time
        db.session.commit()
        send_verification_email(user.id, otp_num)
        
        return redirect(url_for('please_verify_email'))

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

@app.route('/please_verify_email', methods=['GET'])
def please_verify_email():
    users_id = session.get('user_id')
    print(users_id)
    
    if users_id:
        user = Users.query.get(users_id)
        return render_template('pages/email_verification.html', user=user)
    else:
        return redirect(url_for('login'))
