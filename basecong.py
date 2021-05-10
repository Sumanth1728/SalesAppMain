import os
from flask import Flask
from flask_mysqldb import MySQL
from flask_mail import *
######################################
#### SET UP OUR Mail server #####
###################################

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'bankapplication24@gmail.com'
app.config['MAIL_PASSWORD'] = 'Vkollab@1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


######################################
#### SET UP OUR DATABASE #####
##################################

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sumanth@89'
app.config['MYSQL_DB'] = 'new_schema'

mysql = MySQL(app)


# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'
