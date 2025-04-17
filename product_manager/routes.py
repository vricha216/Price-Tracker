from flask import Flask, jsonify, redirect,render_template,request,session
from app import app,db,login_required
from product_manager.models import Product


@app.route('/user/product/add', methods=['POST'])
@login_required
def add_product():
    return Product().add_product()


@app.route('/user/product/edit', methods=['POST'])
@login_required
def edit_product():
    return Product().edit_product()
    

@app.route('/user/product/del', methods=['POST'])
@login_required
def del_product():
    return Product().del_product()



