# from sqlalchemy import create_engine, engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import sessionmaker
# from models import *



# session = sessionmaker(bind=engine)

# add_user = User(user_id=1, firstName="Aass",lastName="ss", email="Porebryk@gmail.com", password="1234", phone="091234")
# add_user2 = User(user_id=2, firstName="Fasd",lastName="ss", email="Vasyliev@gmail.com", password="12341234", phone="12341234")


# add_purse = Purse( purse_id=1, funds=1000, user_id=1)
# add_purse2 = Purse( purse_id=2, funds=4000, user_id=2)

# add_transfer = Transfer(transfer_id=1, quantity_funds=10, date='21.09.2020', purse_id_from=1,purse_id_to=2)
# add_transfer2 = Transfer(transfer_id=2, quantity_funds= 200,  date='21.09.2021', purse_id_from=2,purse_id_to=1)
# add_transfer3 = Transfer(transfer_id=3, quantity_funds= 100,  date='24.09.2021', purse_id_from=1,purse_id_to=2)
# ss = session()
 
# ss.add(add_user)
# ss.add(add_user2)
# ss.add(add_purse)
# ss.add(add_purse2)
# ss.commit()
# ss.add(add_transfer)
# ss.add(add_transfer2)
# ss.add(add_transfer3)

# ss.commit()
from pickle import TRUE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


session = sessionmaker(bind=engine)
ss = session()
# user1 = User(id=1, username='Summer', isAdmin=False,  email='name_lastname@lpnu.ua', password='0000', phone='0987654321')
# user2 = User(id=2, username='Winter', isAdmin=True, email='name_lastname2@lpnu.ua', password='0000', phone='0987654311')
# ss.add(user1)
# ss.add(user2)

# book = Product(id=4, name='Red  Riding Hood', category='fairy tales', quantity=4, status='available', img='cover_10.jpeg', description='Once upon a time there lived in a certain village a little country girl, the prettiest creature who was ever seen. Her mother was excessively fond of her; and her grandmother doted on her still more.')
# ss.add(book)
# book = Product(id=5, name='SnowWhite', category='fairy tales', quantity=10, status='available', img='cover_11.jpg', description='Once upon a time, a princess named Snow White lived in a castle with her father, the King, and her stepmother, the Queen. Her father had always said to his daughter that she must be fair')
# ss.add(book)
book = Product(id=4, name='The Hobbit Timbertant', category='fairy tales', quantity=0, status='sold', img='cover_13.jpg',description='In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole')
ss.add(book)

book = Product(id=5, name='The Chronicles of Narnia', category='fairy tales', quantity=10, status='available', img='cover_12.jpg', description='ONCE there were four children whose names were Peter, Susan, Edmund and Lucy. This story is about something that happened to them when they were sent away from London during the war')
ss.add(book)

book = Product(id=6, name='Alice in Wonderland', category='fairy tales', quantity=10, status='available', img='cover_14.jpg', description='Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading')


ss.add(book)

# ss.add(car1)
ss.commit()

# ss.add(order)
# ss.commit()

ss.close()
