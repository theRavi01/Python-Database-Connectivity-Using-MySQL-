# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root",database="learnpython")
cur = myconn.cursor()
#create table *********************
# cur.execute("create table Teacher(id int(20), name varchar(20),age int(20))")

#show tables***********************
cur.execute("show tables")
for x in cur:
    print(x)
print("Table created....")

