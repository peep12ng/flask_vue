import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:7950@localhost:3306/aramgg'
SQLALCHEMY_TRACK_MODIFICATIONS = False