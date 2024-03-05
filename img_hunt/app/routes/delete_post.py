from app.all_routes import *

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return redirect(url_for('home'))

    if post.users_id != session['user_id']:
        return redirect(url_for('home'))

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))
