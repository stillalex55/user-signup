from flask import Flask, request
import re

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{ 
                color:Red; 
                display: inline-block;
                float:left;
                }}
            label {{
                width:125px;
                clear:left;
                text-align:left;
                padding-right:10px;
                margin: 3px;
                }}
            input, label {{
                float:left;
                }}
        </style>
    </head>
    <body>
        <h1>Signup</h1>
        <form method='POST'>
        <label>Username</label> 
            <input type="text" name="fullname" value = />
            <p class="error">{name_error}</p>
            <br>
        <label>Password</label> 
            <input type="password" name="password" value='{password}'/>
            <p class="error">{password_error}</p><br>
        <label>Verify Password</label> 
            <input type="password" name="verify-password" value='{verify_password}'/>
            <p class="error">{verify_error}<br>
        <label>Email</label> 
            <input type="text" name="email" value='{email}'/>
            <p class="error">{email_error}</p>
            <br><br><br>
        <input type="submit" value="Submit Query">
        </form> 
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format(user_error='', password_error='', verify_error='', email_error='')

# def verified(text):
#     if len(text) >= 3 and len(text) <= 20 and not ' ' in text:
#         return True
#     else:
#         return False


# @app.route("/", methods=['POST'])
# def signup():
    
#     user = request.form['name']
#     password = request.form['password']
#     verify_password = request.form['verify_password']
#     email = request.form['email']

#     user_error = ''
#     password_error = ''
#     verify_error = ''
#     email_error = ''
    
    
#     if not verified(user):
#         user_error = "Must enter an acceptable username"
#         user = ''
#     else:
#         user = user
#         user = ''

#     if not verified(password):
#         password_error = "Must enter acceptable password"
#         password = ''
#     else:
#         password = password
#         password = ''

#     if password != verify_password:
#         verify_error = "Password must match"
#         verify_error = ''
#     else:
#         verify_password = verify_password
#         verify_password = ''


#     if len(email) > 7:
#         if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
#             return True
#         else:
#             return False

#     if email("my.email@gmail.com") == False:
#         email_error = "This is not a valid email address"
#         email_error
#     else:
#         email = ''

#     if not user_error and not password_error and not verify_error and not email_error:
#         return '<p>HELLO</p>'
#     else:
#         return form.format(user_error=user_error, 
#         password_error=password_error,
#         verify_error=verify_error, 
#         email_error=email_error)

app.run()