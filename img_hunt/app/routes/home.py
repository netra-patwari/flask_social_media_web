from app.all_routes import *
from sqlalchemy import desc

@app.route('/')

def home():
    user_id = session.get('user_id')
    user = Users.query.filter_by(id = user_id).first()
    posts = db.session.query(Post, Users.name, Users.username, Users.avatar).join(Users, Post.users_id == Users.id).order_by(desc(Post.id)).all()
    return render_template('pages/home.html' , user=user , posts=posts)
