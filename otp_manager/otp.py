from app import db
from mail_manager.mail import send_mail
from flask import jsonify
import random as r
# page refresh hone par delete kr do db mei email
class OTP:

    def send_otp(self,to):
        otp = ""
        for i in range(6):
            otp += str(r.randint(1,9))



        # step 1 - check in db if email already exists update otp
        if db.otp.find_one({'email':to}):
            try:
                # update otp to db
                db.otp.update_one({'email':to},{'$set':{'otp':otp}})
                # send otp email
                print("em-1")
                return send_mail(otp=otp,to=to)
            except Exception as e:
                return { "status":False, "error": "Sorry, but we can't process your accound at the moment..." ,"er":e}
        else:
            doc = {
                    'email':to,
                    'otp': otp
                }
            try:
                if db.otp.insert_one(doc):
                    # send otp to email
                    print('em-2')
                    return send_mail(otp=otp,to=to)
            except Exception as e:
                return { "status":False, "error": "Sorry, but we can't process your accound at the moment...","e":e }


    def verify_otp(self,email,otp):
        # step - 1 check if opt is matched as db otp
        main_otp = db.otp.find_one({'email':email})['otp']
        if otp == main_otp:
            db.otp.delete_one({'email':email})
            return {'status':True}

        return {'status':False,"error":"wrong otp!"}
        # if yes # logged in success # delete otp from db
        # else otp incorrect


