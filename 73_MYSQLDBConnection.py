import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="telusko",auth_plugin="caching_sha2_password")
mycursor=mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)

mycursor.execute("select * from Student")
for i in mycursor:
    print(i)

result=mycursor.fetchall()
print(result)

#result1=mycursor.fetchone()
#print(result1)