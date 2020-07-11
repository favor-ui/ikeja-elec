import os

basedir = os.path.abspath(os.path.dirname(__file__))


# creating a configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-be-guest'\

    MONGO_URI = os.environ.get('MONGO_URI') or os.environ.get("MONGO_URI")


    
