from app.all_routes import *
import base64
 

@app.route('/<username>/profile_onboarding' ,methods=['GET', 'POST'] )
def profile_onboarding(username):
    # print(username)

    user = Users.query.filter_by(username=username).first()
    if user.location != None:
        return redirect(url_for('home'))
    if user:
        print(user)
        if request.method == 'POST':
            name = request.form['name']
            location = request.form['location']
            avatar = request.files['avatar']
            print(avatar)
            bio = request.form['bio']
            print(f'{location , name , bio}')
            image_string = "data:image/jpeg;base64," + base64.b64encode(avatar.read()).decode('utf-8')
            # print(image_string)
            user.name = name
            user.location = location
            user.bio = bio
            user.avatar = image_string
            db.session.commit()
            session['user_id'] = user.id
            return redirect(url_for('home'))
        
            
            
    else:
        return redirect(url_for('login'))

    return render_template('pages/profile_onboarding.html' , user=user)
