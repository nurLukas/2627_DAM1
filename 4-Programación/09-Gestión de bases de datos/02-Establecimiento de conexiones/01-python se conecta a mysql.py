# Windows: pip install mysql-connector-python
# Linux: pip3 install mysql-connector-python --break-system-packages
import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='programacion2627',
  password='tame123$',
  database='programacion2627'
)
if connection.is_connected():
  print("Connected to MySQL database")
  
connection.close()