import mysql.connector
import datetime
from tabulate import tabulate

print("STUDENT MANAGEMENT SYSTEM")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="ISD",
    charset="utf8"
 )

mydb.autocommit = True


def add_record():
    mycursor = mydb.cursor()

    GRNO = int(input("Enter Gr.No of the student: "))
    Name = input("Enter name of student: ")
    Class = int(input("Enter class of student: "))
    Division = input("Enter Division: ")
    DOB = input("date of birth: ")
    address = input("Input address: ")
    Contact_info = int(input("Enter mobile number: "))
    Email_id = input("Enter Email address: ")

    query1 = "insert into student values ({}, '{}', {}, '{}', '{}', '{}', {}, '{}')".format(GRNO, Name, Class, Division, DOB, address, Contact_info, Email_id)

    mycursor.execute(query1)
    mydb.commit
    print("Record added successfully!")
    print("-"*50)

def show_record():
    mycursor = mydb.cursor()

    mycursor.execute("select * from student")
    print(tabulate(mycursor, headers = ['GRNO', 'Name', 'Class', 'Division', 'DOB', 'address', 'Contact_info', 'Email_id']))
    result = mycursor.fetchall()
    for i in result:
        print(i)

def delete_record():
    mycursor = mydb.cursor()

    GRNO = int(input("Enter GRNO. of the Student to be removed=  "))
    query3 = "DELETE FROM STUDENT WHERE GRNO = {}".format(GRNO)
    mycursor.execute(query3)
    mydb.commit()
    print("Record deleted.")

def search_record():
    mycursor = mydb.cursor()

    GRNO = int(input("Enter GRNO. of the Student to be searched:  "))
    query4 = "SELECT * FROM STUDENT WHERE GRNO = {}".format(GRNO)
    mycursor.execute(query4)
    result = mycursor.fetchall()
    for i in result:
        print(i)


while True:
  print("-"*50)
  print("1 - Add New Student")
  print("2 - Display Student Details")
 #print("3 - Update Student")
  print("3 - Delete Student")
  print("4 - Search Student Details")
  print("5 - Exit")
  print("-"*50)

  ch=int(input("Select any option from 1 to 6: "))
  if ch==1:
      add_record()
  elif ch==2:
      show_record()
  elif ch == 3:
      delete_record()
  elif ch == 4:
      search_record()
  else:
      break
