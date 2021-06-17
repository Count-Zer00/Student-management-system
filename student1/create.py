import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

mycursor = mydb.cursor()
mydb.autocommit = True

mycursor.execute("CREATE DATABASE ISD")
mycursor.execute("USE ISD")
mycursor.execute("create table student(GRNO int(5) primary key, Name varchar(15), Class varchar (4), Division char, DOB date, address varchar(30), Contact_info int(10), Email_id varchar(50))")
#mycursor.execute('insert into student values (1, "Guru", 12, "A", "1779-12-31","Muscat", 999999999, "xyz@gmail.com")')
