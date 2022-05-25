from time import *

def addstudent():
    print("This is for adding a new student!")
    sleep(1)
    stu_fname = input("Enter first name of student: ")
    stu_lname = input("Enter family name of student: ")
    stu_age = input("Enter the age of the student: ")
    stu_class = input("Enter the class of the stduent: ")
    stu_id = input("Enter ID of stdudent: ")
    sleep(1)
    file = open("students.txt", "a")
    file.write("Student name: " + stu_fname + stu_lname + "\nStudent age: " + stu_age + "\nStduent class: " + stu_class + "\nStduent id: " + stu_id + "\n+-----------------+\n")
    print("The student added successfully")
    print("+------------------------------+")
    file = open("students.txt", "r")
    print(file.read())
    return

def removestudent():
    print("This is for removing student!")
    sleep(1)
    rem_stu_class = input("Enter class of student: ")
    rem_id_stu = input("Enter id of stude: ")
    #code
    print("The student has deleted!")
    return

def editstudent():
    #under developing
    sleep(1)
    print("This is for editting student")
    stu_edit_name = input("Enter Student Name: ")
    file = open("students.txt", "a")
    text = file.write()
    cursor_index = text.find(stu_edit_name)
    file.seek(cursor_index)

    stu_fname_edit = input("Edit first name of student: ")
    stu_lname_edit = input("Edit family name of student: ")
    stu_age_edit = input("Edit the age of the student: ")
    stu_class_edit = input("Edit the class of the stduent: ")
    stu_id_edit = input("Edit ID of stdudent: ")

    file.write("Student name: " + stu_fname_edit + stu_lname_edit + "\nStudent age: " + stu_age_edit + "\nStduent class: " + stu_class_edit + "\nStduent id: " + stu_id_edit + "\n+-----------------+\n")

    return

def deleteAll():
    #under developing
    print("Delete All students")

def listAll():
    sleep(1)
    print("This is for shaw all student")
    file = open("students.txt", "r")
    print("This is the students: ")
    print("+-------------------------------+")
    sleep(1)
    print(file.read())
    return

print("Welcome To Admin Pannel Page!")
for i in range(100):
    sleep(1)
    username = input("Enter Username: ")
    if (username == "Adam123"):
        sleep(1)
        password = input("Enter Password: ")
        if (password == "Adam123"):
            print("Welcome Admin!")
            for i in range(100):
                print("Choose what you want to do: ")
                print("list = List all students")
                print("edit = Edit an student")
                print("rem =  Remove a student")
                print("add =  Add new student")
                print("delete = Delete all students")
                choose = input("<_: ")
                if (choose == "list"):
                    print(listAll())
                elif (choose == "delete"):
                    print(deleteAll())
                elif (choose == "edit"):
                    print(editstudent())
                elif (choose == "rem"):
                    print(removestudent())
                elif (choose == "add"):
                    print(addstudent())
                else:
                    print("Error")
                break
            else:
                print("Password Incorrect!")
        else:
            print("Username Is Incorrect")