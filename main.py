from flask import Flask, request, redirect, render_template
import cgi
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', user='', user_error='', password_error='', verify_error='', email='', email_error='')

def verified(text):
    if len(text) >= 3 and len(text) <= 20 and not ' ' in text:
        return True
    else:
        return False

@app.route("/", methods=['POST'])
def signup():
    
    user = request.form['fullname']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if len(user)==0:
        user_error = "Must not be blank"
    elif not verified(user):
        user_error = "Must enter an acceptable username"
        user = user
    else:
        user = user

    if len(password)==0:
        password_error = "Password is blank"
    elif not verified(password):
        password_error = "Must enter acceptable password"
    else:
        password = password

    if password != verify_password:
        verify_error = "Password must match"
    else:
        verify_password = verify_password

    if len(email)==0:
        email=email
    elif not verified(email) or not '@' in email or not '.' in email:
        email_error = "This is not a valid email address"
        email=email
    else:
        email = email

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', user=user)
    else:
        return render_template('index.html', user=user, 
        user_error=user_error, 
        password_error=password_error,
        verify_error=verify_error, 
        email=email, 
        email_error=email_error)

app.run()