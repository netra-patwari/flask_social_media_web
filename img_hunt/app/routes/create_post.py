
from app.all_routes import *

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    user_id = session.get('user_id')
    user = Users.query.filter_by(id=user_id).first()
    if not user:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        url = request.form['url']
        caption = request.form['caption']  
        if url.startswith('https://i.pinimg.com/'):
            post = Post(
                url=url,
                caption=caption,
                users_id=user.id
            )
            db.session.add(post)
            db.session.commit()
            print(caption)
            return redirect(url_for('home'))
        else :
            flash('Image must be from Pintrest' , 'error')
        
    return render_template('pages/create_post.html', user=user)
