from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
from otp_manager import otp

class User:

    def start_session(self, user):
        del user['password']
        del user['products']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):

        # Create the user object    
        otp_ = request.form.get('otp')
        mail = request.form.get('email')

        o = otp.OTP()
        res = o.verify_otp(mail,otp_)
        if res['status']:

            user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": mail,
            "password": request.form.get('password'),
            "products":[],
            "p_limit":5
            }
            
            # Check for existing email address
            # if db.users.find_one({ "email": user['email'] }):
            #     return jsonify({ "error": "Email address already in use" }), 400

            # Encrypt the password
            user['password'] = pbkdf2_sha256.encrypt(user['password'])
            if db.users.insert_one(user):
                return self.start_session(user)

            return jsonify({ "error": "Signup failed" }), 401

        else:
            return jsonify({"error":res['error']}), 401


    def signout(self):
        session.clear()
        return redirect('/')
    
    def login(self):

        user = db.users.find_one({
        "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        
        return jsonify({ "error": "Invalid login credentials" }), 401

    def send_signup_otp(self):
        email = request.get_json()['mail']
        if db.users.find_one({ "email": email }):
            return jsonify({'error':'email already exists'}),401

        o = otp.OTP()
        res = o.send_otp(to = email)

        return jsonify(res)

    def check_mail(self):
        mail = request.form.get('email')
        if db.users.find_one({ "email": mail }):
            print("sending otp ....")
            o = otp.OTP()
            o.send_otp(to=mail)
            return jsonify({'mail':True})

        return jsonify({'error':'user does not exists'}),401
    
    def update_pass(self):
        o = otp.OTP()
        mail = request.form.get('email')
        otp_ = request.form.get('otp')
        new_pass = pbkdf2_sha256.encrypt(request.form.get('pass'))

        res = o.verify_otp(mail,otp_)
        print(res)
        if res['status']:
            db.users.update_one({'email':mail},{'$set':{'password':new_pass}})
            return jsonify({'pass_update':True})
        return jsonify({'padd_update':False}),401

