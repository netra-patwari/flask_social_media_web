# from app.all_routes import *

# @app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
# def edit_post(post_id):
#     if 'user_id' not in session:
#         return redirect(url_for('login'))

#     post = Post.query.get(post_id)
#     if post is None:
#         return redirect(url_for('home'))

#     if post.users_id != session['user_id']:
#         return redirect(url_for('home'))

#     if request.method == 'POST':
#         url = request.form['url']
#         caption = request.form['caption']
        
#         if url.startswith('https://i.pinimg.com/'):
#             post.url = url
#             post.caption = caption
#             db.session.commit()
#             flash('Post edited successfully.', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid URL.', 'error')

#     return render_template('pages/edit_post.html', post=post)


from app.all_routes import *

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    user_id = session['user_id']

    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return redirect(url_for('home'))

    if post.users_id != session['user_id']:
        return redirect(url_for('home'))

    user = Users.query.filter_by(id = user_id).first()
    if request.method == 'POST':
        url = request.form['url']
        caption = request.form['caption']
        
        if url.startswith('https://i.pinimg.com/'):
            post.url = url
            post.caption = caption
            db.session.commit()
            flash('Post edited successfully.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid URL.', 'error')

    return render_template('pages/edit_post.html', post=post , user=user)
