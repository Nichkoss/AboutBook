from flask import Blueprint, Response, request, jsonify, Flask
from marshmallow import ValidationError
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

app.config['SECRET_KEY'] = "1111"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:databasesql2022@localhost/mydb2"

# counter = 1
# session = sessionmaker(bind=engine)
# ss = session()
# purses = 1
# transfers = 1

# @app.route('/user', methods=['POST'])
# def create_user():
#     global counter
#     try:
#         data = request.get_json(force=True)
#         hashed_password = data["password"]
#         new_user = User(counter, data["firstName"], data["lastName"], data["email"], hashed_password, data["phone"])
#     except:
#         return Response(status = 400, response = 'Invalid user suplied')
#     counter += 1
#     ss.add(new_user)
#     ss.commit()
#     return Response(status = 200,response = 'successful operation')

# @app.route('/user', methods = ['PUT'])
# def get_user():
#     data = request.get_json(force=True)
#     users = User.query.filter_by(user_id=data['user_id']).first()
#     if not users:
#         return Response(status = 404, response = 'User not found')
#     try:
#         if("firstName" in list(data)):
#             users.firstName = data['firstName']
#         if('lastName' in list(data)):
#             users.lastName = data['lastName']
#         if('email' in list(data)):
#             users.email = data['email']
#         if('password' in list(data)):
#            users.password = data['password']
#         if('phone' in list(data)):
#             users.phone = data['phone']
#     except:
#         return Response(status = 400, response = 'Invalid user suplied')
#     ss.commit()
#     state_data = {"firstName" : users.firstName, "lastName" : users.lastName, "email" : users.email, "phone" : users.phone}
#     return jsonify({"user": state_data}), 200

# @app.route('/user/login', methods = ['GET'])
# def login():
#     data = request.get_json(force=True)
#     print(data);
#     users = User.query.filter_by(phone=data['phone']).first()
#     if not users:
#         return Response(status = 400, response = 'Invalid phone/password supplied')
#     if((users.password == data['password']) == False):
#         return Response(status = 400, response = 'Invalid phone/password supplied')
#     return Response(status = 200, response = 'successful operation')

# @app.route('/user/logout', methods = ['GET'])
# def logout():
#     return Response(status = 'default',response = 'successful operation')

# @app.route('/user/<phones>', methods = ['DELETE'])
# def delete_user(phones):
#     try:
#         users = ss.query(User).filter(User.phone==phones).first()
#     except:
#         return Response(status = 400, response = 'Invalid userphone supplied')
#     if not users:
#         return Response(status = 404, response = 'User not found')
#     ss.delete(users)
#     ss.commit()
#     return Response(status = '200',response = 'successful operation')

# # @app.route('/user/<phone>', methods = ['POST'])
# # def create_purse(phone):
# #     global purses
# #     data = request.get_json(force=True)
# #     users = User.query.filter_by(phone=phone).first()
# #     if not users:
# #         return Response(status = 404, response = 'User not found')
# #     try:
# #         pursess = Purse(purses, data['funds'], data['userId'])
# #     except:
# #         return Response(status = 405 ,response = 'Invalid input')
# #     purse_data = {"PurseId" : purses, "userId" : data['userId'], "funds" : data['funds']}
# #     ss.add(pursess)
# #     ss.commit()
# #     purses += 1
# #     return jsonify({"purse": purse_data}), 200


# if __name__ == 'main':
#     app.run(debug=True)
