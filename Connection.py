# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root")
print("connection established....")