from tracemalloc import start
from flask import Flask, render_template, session, redirect,jsonify
from functools import wraps
import pymongo
import certifi
import time


app = Flask(__name__)
app.secret_key = b'\xb1o\x95\x95/\x89\xd3\x8e\xd2)\xc0\t\xf1Q\x0b\x18*\xa5\xf04#7\x1e\xec'


# Database
client = pymongo.MongoClient("Your MongoDb URI", tlsCAFile=certifi.where())
# MongoDb URI looks like this ->  mongodb+srv://username:passsword@cluster0.mongodb.net/API?retryWrites=true&w=majority”
db = client.track_budd



# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


# Routes
from users import routes
from product_manager import routes
from otp_manager import routes
from scheduler import scheduler
from otp_manager import otp


@app.route('/')
def home():
    
    # o = otp.OTP()
    # res = o.send_otp('issnehill@gmail.com')
    # print(res)

    db.otp.delete_one({'email':"t@t.com"})
    if 'logged_in' in session:
        products = db.users.find_one({'_id':session['user']['_id']})['products']
        payload = {"sesssion":True,'products':products}
        return render_template('home.html',payload = payload)
    return render_template('home.html')


