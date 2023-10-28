# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root", database="learnpython")
cur = myconn.cursor()
#single record inserted
# cur.execute("insert into student(Id,Name,Age) values(%s,%s,%s)", (1,"Ravi",22))

#multiple record inserted
sql="insert into student(Id,Name,Age) values(%s,%s,%s)"
slist=[(2,"Mohit",21),(3,"Shubham",23),(4,"Sachin",22),(5,"Kapil",22)]
cur.executemany(sql,slist)
myconn.commit()
print(cur.rowcount, "Record inserted..")

