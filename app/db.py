from flask_mysqldb import MySQL
from app import app  # Import the Flask app after it's initialized

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'welfare_management_system_dev'

mysql = MySQL(app)