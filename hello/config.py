import os 
from dotenv import load_dotenv
import psycopg2
load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    #postgresql://blog_postgresql_blogy_user:7WdM3m8fkGkZaIil02WgWkHAjSikufjO@dpg-cqlh9tbv2p9s73areeog-a.oregon-postgres.render.com/blog_postgresql_blogy
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME= os.getenv("EMAIL_ADDRESS")
    MAIL_PASSWORD= os.getenv("EMAIL_PASS")