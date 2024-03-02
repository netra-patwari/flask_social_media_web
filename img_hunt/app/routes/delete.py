from app.all_routes import *

@app.route('/delete', methods=['POST'])
def delete():
    
    user_id = session.get('user_id')
    user = Users.query.filter_by(id=user_id).first()
    
    if not user:
        return redirect(url_for('home'))
    
    otp = Otp.query.filter_by(user_id=user_id).all()
    login_info = LoginInfo.query.filter_by(users_id=user_id).all()
    posts = Post.query.filter_by(users_id=user_id).all()  # Corrected
    
    # Delete each instance one by one
    for post in posts:
        db.session.delete(post)
    for info in login_info:
        db.session.delete(info)
    for o in otp:
        db.session.delete(o)
    
    db.session.delete(user)
    db.session.commit()
    print('deleted')
    return redirect(url_for('home'))

