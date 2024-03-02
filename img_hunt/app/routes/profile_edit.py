from app.all_routes import *
import base64

@app.route('/profile_edit', methods=['GET', 'POST'])
def profile_edit():
    user_id = session.get('user_id')
    user = Users.query.filter_by(id=user_id).first()
    
    if not user:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        bio = request.form['bio']
        avatar = request.files['avatar']
        image_string = "data:image/jpeg;base64," + base64.b64encode(avatar.read()).decode('utf-8')
        user.avatar = image_string
        
        user.name = name
        user.location = location
        user.bio = bio
        db.session.commit()
        session['user_id'] = user.id
        return redirect(url_for('home'))
    
    return render_template('pages/profile_edit.html', user=user)
