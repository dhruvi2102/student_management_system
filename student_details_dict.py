studentManagement={}    #blank dictionary

"""
{
aa@gmail.com:
         {
              Roll no: 
              Name:
              subject:
              score:
              city:
         }
}
"""

def addstudent():
    email=input("Enter email: ")
    rollno=int(input("Enter roll no: "))
    name=input("enter name: ")
    subject=input("Enter subject: ")
    score=int(input("Enter score: "))
  #  city=input("Enter city: ")
    
    subject_dic={}
    no_of_subject =int(input("Enter no of subject you want: "))
    total=0
    for i in range(0,no_of_subject):
        subject = input("Enter subject : ")
        marks= int(input("Enter your marks: "))
        subject_dic[subject]=marks
        total+=marks
    per=total/no_of_subject

    studentDetails = {}  #sub dictionary

    studentDetails["rollno"]= rollno
    studentDetails["name"]= name
    studentDetails["subject"]= subject_dic
    studentDetails["total"]= total
    studentDetails["average"]=per
    #studentDetails["city"]= city

    #print(studentDetails)
    studentManagement[email]=studentDetails

def viewStudent():
    for k,sub in studentManagement.items():
        print("-------------------------------")
        print("Roll no: ",sub["rollno"])
        print("Email: ",k)
        print("Name: ",sub["name"])
        print("Subject: ",sub["subject"])
        print("Marks: ",sub["marks"])
        print("Average: ",sub["average"])

def deleteStudent():
    email= input("Enter student email address which you want to delete : ")
    if email in studentManagement.keys():
        del studentManagement[email]
    else:
        print("invalid email address")

        print("Successfully record deleted....")
        viewStudent()    

def searchStudent():
     email= input("Enter student email address which you want to search: ")
     if email in studentManagement.keys():
         print("Name: ",studentManagement[email]["name"])
         print("Subject: ",studentManagement[email]["subject"])
         print("Score: ",studentManagement[email]["score"])  

def menu():     #menu name function
    menu= """
                    MENU
            STUDENT MANAGEMENT SYSTEM    
         1)Add student
         2)View student
         3)Delete student
         4)Search student

    """
    print(menu)

    choice= int(input("Enter your choice: "))
    if choice==1:
        addstudent()
        print()   #blank line
        print("Successfully Data added....")
    elif choice==2:
        viewStudent()
    elif choice==3:
        deleteStudent()
    elif choice==4:
        searchStudent()      
    else:
        print("Thank you for visiting application")
            

status=True
while status:
    menu()    #calling

    exit=input("Do you want to continue? press y for yes & n for no: ")
    if exit=='y':
        status=True
    else:
        status=False    