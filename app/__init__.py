from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from datetime import datetime, date
from functools import wraps


app = Flask(__name__)



app.config.from_object(Config)

mongo = PyMongo(app)


def cur_time_and_date():
    now = datetime.utcnow()
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    tm = now.strftime("%H:%M:%S")
    return (d2 +' '+'at'+' '+tm)



from app import views
