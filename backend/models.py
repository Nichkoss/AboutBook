from typing import Text
from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    "mysql+mysqlconnector://root:databasesql2022@localhost/mydb2", echo=True)
Base = declarative_base()

metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    username = Column(String(45), nullable=True)
    isAdmin = Column(Boolean, nullable=True)
    email = Column(String(45), nullable=True)
    password = Column(String(100), nullable=True)
    phone = Column(String(45), nullable=True)

    def __repr__(self):
        return f"{self.id}, {self.isAdmin}, {self.username}, {self.email}, {self.password}, {self.phone}"

    def __init__(self, id, isAdmin, username, email, password, phone):
        self.id = id
        self.isAdmin = isAdmin
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    name = Column(String(45), nullable=True)
    category = Column(String(45), nullable=True)
    quantity = Column(Integer, nullable=True)
    status = Column(String(45), nullable=True)
    img = Column(String(200), nullable=True)
    description = Column(String(200), nullable=True)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.category}, {self.quantity}, {self.status}, {self.img}, {self.description}"

    def __init__(self, id, name, category, quantity, status, img, description):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.status = status
        self.img = img
        self.description = description


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    quantity = Column(Integer(), nullable=True)
    status = Column(String(45), nullable=True)
    User_idUser = Column(Integer(), ForeignKey('user.id'))
    Product_IdProduct = Column(Integer(),  ForeignKey('product.id'))

    def __init__(self, id, quantity, status, User_idUser, Product_IdProduct):
        self.id = id
        self.quantity = quantity
        self.status = status
        self.User_idUser = User_idUser
        self.Product_IdProduct = Product_IdProduct

    def __repr__(self):
        return f"{self.idAudience}, {self.number}, {self.amount_of_places}, {self.status}, self.Product_IdProduct= {self.User_idUser}"


"""" class OrderSchema(ma.SQLAlchemySchema):
  class Meta:
    model = Order

  id = ma.auto_field()
  quantity = ma.auto_field()
  status = ma.auto_field()
  User_idUser = ma.auto_field()
  Product_IdProduct = ma.auto_field()
"""


# class User(Base):
#     __tablename__ = 'user'
#     user_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
#     firstName = Column(String(45), nullable=True)
#     lastName = Column(String(45), nullable=True)
#     email = Column(String(45), nullable=True)
#     password = Column(String(45), nullable=True)
#     phone = Column(String(45), nullable=True)


# class Purse(Base):
#     __tablename__ = 'purse'
#     purse_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
#     funds = Column(Integer(), nullable=True)
#     user_id = Column(Integer(), ForeignKey('user.user_id'))
#     user = relationship("User")


# class Transfer(Base):
#     __tablename__ = 'transfer'
#     transfer_id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
#     quantity_funds = Column(Integer(),  nullable=True)
#     date = Column(Date(), nullable=True)
#     purse_id_from = Column(Integer(), ForeignKey('purse.purse_id'))
#     purse_id_to = Column(Integer(), ForeignKey('purse.purse_id'))


# from sqlalchemy import Column, Integer, String, Date, ForeignKey
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# engine = create_engine("mysql+mysqlconnector://root:databasesql2022@localhost/lab6", echo=True)

# Base = declarative_base()
# metadata = Base.metadata

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer(), primary_key=True, autoincrement=True)
#     username = Column(String(45), nullable=False)
#     first_name = Column(String(45), nullable=False)
#     last_name = Column(String(45), nullable=False)
#     email = Column(String(45), nullable=False)
#     password = Column(String(205), nullable=False)
#     phone = Column(String(20), nullable=False)
#     def __init__(self, user_id, username, first_name, last_name, email, password, phone):
#         self.id = user_id
#         self.username = username
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#         self.phone = phone

#     def repr(self):
#         return f"{self.id}, {self.username}, {self.first_name},{self.last_name}, {self.email}, {self.password}, {self.phone}"

#     def __str__(self):
#         return f"User ID      : {self.id}\n" \
#                f"Username     : {self.username}\n" \
#                f"First name   : {self.first_name}\n" \
#                f"Last name    : {self.last_name}\n" \
#                f"Email        : {self.email}\n" \
#                f"Phone        : {self.phone}\n"


# class Car(Base):
#     __tablename__ = 'car'
#     id = Column(Integer(), primary_key=True,  autoincrement=True)
#     name = Column(String(50), nullable=False)
#     descriptions = Column(String(300), nullable=True)
#     status = Column(String(45), nullable=False)
#     rented_dates = Column(String(45), nullable=False)
#     def __init__(self, car_id, name, descriptions, status, rented_dates):
#         self.id = car_id
#         self.name = name
#         self.descriptions = descriptions
#         self.status = status
#         self.rented_dates = rented_dates

#     def repr(self):
#         return f"{self.id}, {self.name}, {self.descriptions}, {self.status}, {self.rented_dates}"

# class Order(Base):
#     __tablename__ = 'order'
#     id = Column(Integer(), primary_key=True,  autoincrement=True, )
#     carId = Column(Integer(), ForeignKey('car.id'))
#     userId = Column(Integer(), ForeignKey('user.id'))
#     date_placed = Column(Date())
#     car = relationship("Car")
#     user = relationship("User")
#     def __init__(self, user_id, carId, userId, date_placed):
#         self.id = user_id
#         self.carId = carId
#         self.userId = userId
#         self.date_placed = date_placed


#     def repr(self):
#         return f"{self.id}, {self.carId}, {self.userId}, {self.date_placed}"
