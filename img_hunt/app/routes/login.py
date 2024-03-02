
from app.all_routes import *
import requests

def get_location(ip_address):
    access_token = '560450c74485ed'
    response = requests.get(f'http://ipinfo.io/{ip_address}/json?token={access_token}')
    data = response.json()

    city = data.get('city', 'Unknown')
    region = data.get('region', 'Unknown')
    country = data.get('country', 'Unknown')
    org = data.get('org', 'Unknown')
    return [city, region, country, org]

def extract_info(str):
    start_pos = str.find('(') + 1
    end_pos = str.find(')')

    if start_pos != -1 and end_pos != -1:
        device_info = str[start_pos:end_pos]
        os = device_info.split(';')[1].strip()
        user_agent = str[end_pos + 1:].strip()
        return os, user_agent
    else:
        return "Unknown Device", "Unknown User Agent"

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']

        user = Users.query.filter((Users.email == identifier) | (Users.username == identifier)).first()

        if user and bcrypt.check_password_hash(user.password, password) and user.otp_verified == 'true':
            session['logged_in'] = True
            session['user_id'] = user.id 
            session['username'] = user.username
            session['email'] = user.email
            
            user_agent_str = request.headers.get('User-Agent')
            os ,  user_agent = extract_info(user_agent_str)
            login_time = datetime.now()

            ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            location = get_location(ip)
        
            login_info = LoginInfo(
                users_id = user.id,
                user_agent = user_agent,
                os=os,
                city=location[0],
                region=location[1],
                country=location[2],
                telecom_service_provider=location[3],
                ip_address=ip,
                timestamp=login_time
            )
        
            db.session.add(login_info)
            db.session.commit()
            
            return redirect(url_for('home'))


        else:
            flash('Login failed. Check your email/username and password.', 'danger')

    return render_template('pages/login.html')

