from app.all_routes import *

@app.route('/logout' ,  methods=['POST'])
def logout():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    session.pop('user_id')
    return redirect('home')