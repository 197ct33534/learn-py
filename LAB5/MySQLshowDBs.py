
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
)
cursor = mydb.cursor()
cursor.execute("SHOW DATABASES") 
print(cursor.fetchall())
mydb.close()