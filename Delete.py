# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root",database="learnpython")
cur = myconn.cursor()

#Query for delete 1 record *************
deleteq="delete from learnpython.student where name=%s"
value= ("adaresh",)
cur.execute(deleteq,value)
myconn.commit()
print("record deleted...")