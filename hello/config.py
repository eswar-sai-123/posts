import os 
from dotenv import load_dotenv
load_dotenv()
class Config:
    SECRET_KEY = "rammasiw"
    SECURITY_PASSWORD_SALT = "123243353fd"
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME= os.getenv("EMAIL_ADDRESS")
    MAIL_PASSWORD= os.getenv("EMAIL_PASS")