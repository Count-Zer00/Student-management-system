import mysql.connector 
import datetime
from tabulate import tabulate 

print("-"*50)
print("STUDENT MANAGEMENT STYSTEM")

now = datetime.datetime.now()
print("Date and time: ", end='')
print(now.strftime("%Y-%M-%D"))

database = input("Enter Name for the database: ")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    charset = "utf8"
)

mycursor = mydb.cursor()

query1 = "create database if not exists %s"%(database,)
mycursor.execute(query1)
print("Database created")
mycursor=mydb.cursor()
mycursor.execute("use "+database)

#table
table = input("Enter table name: ")
query2 = "create table if not exists "+table+" (GRNO int(5) primary key, Name varchar(15), Class varchar (4), Division char, DOB date, Address varchar(30), Contact_info int(10), Email_id varchar(50))"
print("table "+table+" created successfully")
mycursor.execute(query2)

def add():
  try:
    print("Enter Student Information\n")
    GRNO=int(input("Enter Roll Number: "))
    Name=input("Enter Name: ")
    Class=input("Enter Class: ")
    Division=input("Enter Division: ")
    DOB = input("Input date of birth: ")
    Address = input("Input address: ")
    Contact_info = int(input("Input contact info: "))
    Email_id = input("Enter mail id: ")


    record=(GRNO, Name, Class, Division, DOB, Address, Contact_info, Email_id)

    query3="insert into "+table+" values (%s, %s, %s, %s, %s, %s, %s, %s)"
    print(query3)
    mycursor.execute(query3, record)
    mydb.commit()
  except Exception as e:
    print("Wrong Values Entered", e)


def show():
    try:
        query4 = "select * from "+table
        print(query4)
        mycursor.execute(query4)

        print(tabulate(mycursor, headers = ["GRNO", "Name", "Class", "Division", "DOB", "Address", "Contact-info", "Email-id"]))
        record = mycursor.fetchall()
        for i in record:
            print(record)
    
    except Exception as e:
        print("wrong values entered", e)

def search():

    try:
        r = input("Enter GRNO to be shown: ")
        query5 =  "select * from "+table+" where GRNO=" +r
        print(query5)

        mycursor.execute(query5)
        record = mycursor.fetchone()

        print("Record of the stdent: "+r)
        print(record)

        result = mycursor.rowcount
        if result == 1:
            print("Not found")
    except Exception as e:
        print("Wrong values entered",e)
    
def delete():
    try:
        r = input("Enter GRNO to be deleted: ")
        query6 = "delete from "+table+" where GRNO=" +r
        print(query6)
        mycursor.execute(query6)
        mydb.commit()
        result = mycursor.rowcount
        
        if result > 0:
            print("The data has been removed")
        else:
            print("GRNO not found")

    except Exception as e:
        print("Wrong value",e)

while True:
    print("-"*50)
    print("1 - Add New Student")
    print("2 - Display Student Details")
    print("3 - search Student")
    print("4 - delete Student Details")
    print("5 - Exit")
    print("-"*50)
    
    ch=int(input("Select any option from 1 to 6: "))
    if ch==1:
        add()
    elif ch==2:
        show()
    elif ch == 3:
        search()
    elif ch == 4:
        delete()
    else:
        break