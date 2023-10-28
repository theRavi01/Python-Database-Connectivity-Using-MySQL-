# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root")
cur = myconn.cursor()

#create new database ***********************
# cur.execute("create database LearnPython")

#show databases*****************************
cur.execute("show databases")
for x in cur :
    print(x)
print("create database || show databases....")