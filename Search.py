# create connection 
import mysql.connector
myconn =mysql.connector.connect(host="localhost",password="root",user="root", database="learnpython")
cur = myconn.cursor()
cur.execute("select * from student")
#fetch data by for loop***************
# print("Id  Name  Age")
# for x in cur:
#     print(x)

#for one data fetch*******************
# s_data = cur.fetchone()

#for all data fetch*******************
s_data = cur.fetchall()
print(s_data)
myconn.close()
