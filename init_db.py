import mysql.connector

def connect():
    mydb = mysql.connector.connect(host='127.0.0.1',user='root', password = "p@ssword")
    mycursor = mydb.cursor()
    print('here')
    mycursor.execute("CREATE DATABASE Python")

def add_data():
    mydb = mysql.connector.connect(host='127.0.0.1',user='root', password = "p@ssword",database="Python")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE user( uid int NOT NULL AUTO_INCREMENT,  name varchar(45) NOT NULL, city varchar(35) NOT NULL,  age int NOT NULL,  PRIMARY KEY (uid)  );")
    sql = "INSERT INTO user (name, city,age) VALUES (%s, %s,%s)"
    val = ("Yash", "Vadodara",21)
    mycursor.execute(sql, val)
    mydb.commit()