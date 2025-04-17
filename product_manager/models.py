from turtle import title
from flask import Flask, jsonify, request, session, redirect
from urllib.parse import urlparse
from passlib.hash import pbkdf2_sha256
from app import db
import re
import uuid
from services.amazon_traker import a_tracker
from services.myntr_traker import m_tracker
class Product:

    def add_product(self):
        
        allowed_hosts = ['www.amazon.in','www.myntra.com']
        user = session['user']
        p_l = db.users.find_one({'_id':user['_id']})['p_limit']
        if p_l > 0:
            p_url = request.form.get('p_url')
            p_price = request.form.get('base_price')
            host_name = urlparse(p_url).netloc
            if host_name in allowed_hosts:
                if host_name == 'www.myntra.com':
                    title = m_tracker.Tracker(p_url).get_title()
                else:
                    title = a_tracker.Tracker(p_url).get_title()

                if title['status']:
                    title = title['title']
                else:
                    # print("Unable to fetch product title :/")
                    title = ""
                u_id = user['_id']
                p_id = uuid.uuid4().hex
                db.users.update_one({'_id':u_id},{'$push':{'products':{'_id':p_id,'title':title,'base_price':p_price,'url':p_url,'done':False}}})
                db.users.update_one({'_id':u_id},{'$set':{'p_limit':p_l-1}})

                payload = {'_id':p_id,'title':title,'base_price':p_price,'p_url':p_url}

                return jsonify(payload), 200
            else:
                return jsonify({'error':'Sorry but we only accept myntra and amazon urls'}), 401

        else:
            return jsonify({"error":"Product add limit reached!"}), 401

    
    def edit_product(self):
        data = request.get_json()
        curr_price = data['price']
        p_id = data['p_id'][3:]

        try:
            res = db.users.update_one(
                {'_id':session['user']['_id'], 'products._id':p_id},
                {'$set':{"products.$.base_price":curr_price}}
                )
            return jsonify({'done':True}),200
        except Exception as e:
            return jsonify({ "error": "Can't update at a moment!" }), 401
    
    def del_product(self):
        data = request.get_json()
        p_id = data['p_id'][3:]
        u_id = session['user']['_id']
        p_l = db.users.find_one({'_id':u_id})['p_limit']
        try:
            db.users.update_one({'_id':u_id},{'$set':{'p_limit':p_l+1}})
            db.users.update_one(
                {'_id':u_id},
                {'$pull':{'products':{'_id':p_id } } },
                False,
                True,
                )
            return jsonify({'ok':True}),200
            
        except Exception as e:
            return jsonify({'error':"Can't remove this product at a moment","e":e}),401




    