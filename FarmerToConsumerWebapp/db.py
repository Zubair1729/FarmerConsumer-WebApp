# db.py
from pymongo import MongoClient
from config import Config

# MongoDB setup
client = MongoClient(Config.MONGO_URI)
db = client.get_database('farm_fresh')

# Collections
farmers_collection = db.get_collection('farmers')
customers_collection = db.get_collection('customers')
vegetables_collection = db.get_collection('vegetables')
carts_collection = db.get_collection('carts')
history_collection = db.get_collection('history')
records_collection = db.get_collection('records')