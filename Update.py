# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root", database="learnpython")
cur = myconn.cursor()

#Update record ***********************
updateq= "update learnpython.student set name =%s where Id =%s"
value= ("adaresh",1)
cur.execute(updateq,value)
print("update record")
myconn.commit()