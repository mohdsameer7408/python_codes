import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="12345")
mydata = db.cursor()
mydata.execute("SHOW DATABASES")
for i in mydata:
    print(i, end=" ")
