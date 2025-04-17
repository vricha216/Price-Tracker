from flask import Flask, jsonify, redirect,render_template,request,session
from app import app
from app import db
from users.models import User

# TOKEN = "1766289JKDHWKH8717X" 


@app.route('/user/signup',methods=['POST','GET'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST','GET'])
def login():
    if 'logged_in' in session:
        return redirect('/dashboard')
    if request.method == "POST":
        return User().login()
    return render_template('login.html')



@app.route('/email/send/otp',methods=['POST'])
def sendotp():
    print("hey helo")
    return User().send_signup_otp()

@app.route('/user/pass/reset', methods=['GET'])
def pass_reset():
    return render_template('update_pass.html')

@app.route('/user/check_email', methods=['POST'])
def check_mail():
    return User().check_mail()

@app.route('/user/pass/update', methods=['POST'])
def update_pass():
    return User().update_pass()
