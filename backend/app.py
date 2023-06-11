from flask import Blueprint, Response, request, jsonify, Flask, make_response

import datetime
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from functools import wraps
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.config['SECRET_KEY'] = "databasesql2022"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:databasesql2022@localhost/mydb2"

session = sessionmaker(bind=engine)
ss = session()
counter = ss.query(User).count() + 1
orders = ss.query(Order).count() + 1
products = ss.query(Product).count() + 1
used_tokens = []
current_user = ''


@app.route('/user', methods=['POST'])
def create_user():
    global counter
    data = request.get_json(force=True)
    db_user = ss.query(User).filter_by(username=data['username']).first()
    db_email = ss.query(User).filter_by(email=data['email']).first()

    if db_user:
        return make_response('User with such username already exists', 405)

    if db_email:
        return make_response('User with such email already exists', 405)

    try:
        hashed_password = data["password"]
        data['isAdmin'] = False
        data["phone"] = 0
        new_user = User(counter, data['isAdmin'], data["username"],
                        data["email"], hashed_password, data["phone"])

    except:
        return Response(status=400, response='Invalid user supplied')

    counter += 1
    ss.add(new_user)
    ss.commit()
    return Response(status=200, response='successful operation')


@app.route('/user/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    user = ss.query(User).filter_by(username=username).first()
    if not user:
        return make_response('Incorrect username', 404)
    global current_user
    if user.password != password:
        return make_response('Incorrect password', 401)

    if user.password == password:
        current_user = user
        print(current_user)
        return jsonify({"res": current_user.id}), 200
    return Response(status=200, response='Successful operation ;)')


@app.route('/user/logout', methods=['GET'])
def logout():
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
        used_tokens.append(token)
    return Response(status='default', response='successful operation')


@app.route('/user/<userId>', methods=['PUT'])
def put_user(userId):
    data = request.get_json(force=True)
    users = ss.query(User).filter(User.id == userId).first()
    if not users:
        return Response(status=404, response='User not found')
    try:
        if ("username" in list(data)):
            db_user = ss.query(User).filter_by(
                username=data['username']).first()
            if db_user:
                return Response(status=405, response='User with such username already exists.')
            users.username = data['username']

        if ('email' in list(data)):
            db_user = ss.query(User).filter_by(username=data['email']).first()
            if db_user:
                return Response(status=405, response='User with such email already exists.')
            users.email = data['email']
        if ('password' in list(data)):
            hashed_password = data["password"]
            users.password = hashed_password
        if ('phone' in list(data)):
            db_user = ss.query(User).filter_by(username=data['phone']).first()
            if db_user:
                return Response(status=405, response='User with such phone already exists.')
            users.phone = data['phone']
    except:
        return Response(status=400, response='Invalid user suplied')
    ss.commit()
    state_data = {'id': userId}
    return jsonify({"user": state_data}), 200


@app.route('/user/<userId>', methods=['GET'])
def get_user(userId):
    try:
        user = ss.query(User).filter(User.id == userId).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not user:
        return Response(status=404, response='User not found')
    if not current_user.id == user.id and not current_user.isAdmin:
        return make_response('User can be seen only by the owner and admin')
    user_data = {"UserId": user.id, "username": user.username,
                 "email": user.email, "password": user.password, "phone": user.phone}
    return jsonify({"user": user_data}), 200


@app.route('/user/<userId>', methods=['DELETE'])
def delete_user(userId):
    try:
        user = ss.query(User).filter(User.id == userId).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not user:
        return Response(status=404, response='User not found')
    if not current_user.id == user.id and not current_user.isAdmin:
        return make_response("Only owner can delete the account(or admin)")
    ss.delete(user)
    ss.commit()
    return Response(status='200', response='successful operation')


# Product
@app.route('/product', methods=['POST'])
def create_product():
    if not current_user.isAdmin:
        return make_response('U have not permission to post products')
    global products
    try:
        data = request.get_json(force=True)
        new_product = Product(
            products, data["name"], data["category"], data["quantity"], data["status"])
    except:
        return Response(status=400, response='Invalid product suplied')
    products += 1
    ss.add(new_product)
    ss.commit()
    return Response(status=200, response='successful operation')


@app.route('/product/<productId>', methods=['PUT'])
def put_product(productId):
    if not current_user.isAdmin:
        return make_response('U have not permission to post products')
    data = request.get_json(force=True)
    product = ss.query(Product).filter(Product.id == productId).first()

    if not product:
        return Response(status=404, response='Product not found')
    try:
        if ("name" in list(data)):
            product.name = data['name']
        if ('category' in list(data)):
            product.category = data['category']
        if ('quantity' in list(data)):
            product.quantity = data['quantity']
        if ('status' in list(data)):
            product.status = data['status']
    except:
        return Response(status=400, response='Invalid product supplied')
    ss.commit()
    state_data = {"name": product.name, "category": product.category,
                  "quantity": product.quantity, "status": product.status}
    return jsonify({"product": state_data}), 200


@app.route('/product/<productId>', methods=['GET'])
def get_product(productId):
    try:
        product = ss.query(Product).filter(Product.id == productId).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not product:
        return Response(status=404, response='Product not found')
    product_data = {"id": product.id, "name": product.name, "category": product.category,
                    "quantity": product.quantity, "status": product.status, "img": product.img, "description": product.description}
    return jsonify({"item": product_data}), 200


@app.route('/products', methods=['GET'])
def get_products():
    products = ss.query(Product).all()
    items = []
    for product in products:
        # print(product)
        # product_data = {"id" : product.id, "name" : product.name, "category" : product.category, "quantity" : product.quantity, "status" : product.status, "img": product.img, "description": product.description}
        product_data = {"id": product.id, "name": product.name,
                        "category": product.category, "status": product.status, "img": product.img}
        items.append(product_data)
    return jsonify({"items": items}), 200


@app.route('/product/<productId>', methods=['DELETE'])
def delete_product(productId):
    if not current_user.isAdmin:
        return make_response('U have not permission to delete products')

    try:
        product = ss.query(Product).filter(Product.id == productId).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not product:
        return Response(status=404, response='Product not found')
    ss.delete(product)
    ss.commit()
    return Response(status='200', response='successful operation')


# #Order
@app.route('/store/order', methods=['POST'])
def make_order():
    global orders
    data = request.get_json(force=True)
    try:
        product = ss.query(Product).filter(
            Product.id == data['productId']).first()
        user = ss.query(User).filter(User.id == data['userId']).first()
    except:
        return Response(status='400', response="Invalid response supplied")
    if (not product) or (not user):
        return Response(status='404', response="Product or User not found")
    order = Order(orders, data['quantity'],
                  data['status'], data['userId'], data['productId'])

    if (int(product.quantity) <= int(data['quantity'])):
        return Response(status='405', response="The product is not available in quantity that u want")

    ss.add(order)
    product.quantity -= int(data['quantity'])
    ss.commit()
    orders += 1
    return jsonify({"res": 'successfull operation ;)'}), 200


@app.route('/store/order/<orderId>', methods=['GET'])
def get_order(orderId):
    try:
        order = ss.query(Order).filter(Order.id == orderId).first()
        if not current_user.id == order.User_idUser or current_user.isAdmin:
            return make_response('Orders can see only their owners or admins')
    except:
        return Response(status='400', response="Invalid ID supplied")
    if not order:
        return Response(status='404', response="Order not found")
    order_data = {"OrderId": order.id, "quantity": order.quantity, "status": order.status,
                  "userId": order.User_idUser, "productId": order.Product_IdProduct}
    return jsonify({"transfer": order_data}), 200


@app.route('/store/order/<orderId>', methods=['DELETE'])
def delete_order(orderId):
    if not current_user.isAdmin:
        return make_response('Orders can be deleted only by admins')
    try:
        order = ss.query(Order).filter(Order.id == orderId).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not order:
        return Response(status=404, response='Order not found')
    ss.delete(order)
    ss.commit()
    return Response(status='200', response='successful operation')


if __name__ == 'main':
    app.run(debug=True)
