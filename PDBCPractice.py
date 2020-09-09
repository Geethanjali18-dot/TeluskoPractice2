import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="telusko",auth_plugin="caching_sha2_password")
mysqlcursor=mydb.cursor()
mysqlcursor.execute("show databases")
for i in mysqlcursor:
    print(i)