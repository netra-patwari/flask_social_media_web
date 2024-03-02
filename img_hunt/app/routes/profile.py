from app.all_routes import * 


@app.route('/profile' ,  methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    user = Users.query.filter_by(id = user_id).first()
    if not user:
        return redirect(url_for('home'))
    
    return render_template('pages/profile.html',user=user)