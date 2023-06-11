from sqlalchemy import create_engine, MetaData
from config import SERVER, USERNAME, PASSWORD, DB

metadata = MetaData()
# engine = create_engine(f"mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}")
# engine = create_engine("mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{SERVER}/{DB}", echo=True)
engine = create_engine(
    "mysql+mysqlconnector://root:databasesql2022@127.0.0.1:3306/mydb2", echo=True)
