from flask import Flask, jsonify, redirect,render_template,request,session
from app import app
from app import db
from users.models import User
from otp_manager import otp






# @app.route('/emai/verify/otp',methods=['POST'])
# def verify():
#     otp = request.form.get('otp')
#     email = request.form.get('email')
#     main_otp = db.otp.find_one({'email':email})['otp']
#     if otp == main_otp:
#         db.otp.remove({'email':email})
#     else:
#         return jsonify({'error':'varification error'})


