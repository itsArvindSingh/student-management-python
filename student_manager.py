import csv
import os

file_exists=os.path.isfile("students.csv")
with open("students.csv","a",newline="") as f:
    print("---Running Code---")
    writer=csv.writer(f)
    if not file_exists:
        writer.writerow(["Name","Division","semester","State","District","Contact No.","Gr No.","Enrollment No.","Gender","Degree"])
def display():
    with open("students.csv","r") as f:
        print("---Running Code---")
        reader=csv.DictReader(f)
        print("Enter Gr Number : ")
        gr_num=int(input())
        for row in reader:
            if str(gr_num) in row["Gr No."]:
                print(row)
def insert():
    with open("students.csv","a",newline="") as f:
        writer=csv.writer(f)
        Stu_Data=[]
        print("Enter Student Name : ")
        name=input()
        print("Enter division: ")
        division=input()
        print("Enter semester: ")
        semester=input()
        print("Enter State : ")
        state=input()
        print("Enter District : ")
        District=input()
        print("Enter Contact No. :")
        Contactno=int(input())
        print("Enter Gr. Number : ")
        GRnumber=int(input())
        print("Enter Enrollment Number : ")
        Enrollnumber=int(input())
        print("Enter Gender : ")
        gender=input()
        print("Enter Degree(BTECH CSE AI&ML OR BTECH CSE AI&DS :)")
        degree=input()  
        Stu_Data=[name,division,semester,state,District,Contactno,GRnumber,Enrollnumber,gender,degree]
        writer.writerow(Stu_Data)
        print("Student Added Succesfullly.")
def delete():
    with open("students.csv","r") as f:
        reader=csv.DictReader(f)
        updated_data=[]
        gr_num=input("Enter gr number to delete student record: ")
        for row in reader:
            if row["GRnumber"] != gr_num:
                updated_data.append(row)
    with open("students.csv","w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["Name","Division","semester","State","District","Contact No.","Gr No.","Enrollment No.","Gender","Degree"])
        writer.writeheader()
        writer.writerows(updated_data)
        print("Student record deleted successfully.") 
def update():
    with open("students.csv","r",newline="") as f:
        reader=csv.DictReader(f)
        updated_data=[]
        gr_num=input("Enter gr number to update student record: ")
        for row in reader:
            if row["Gr No."]==gr_num:
                print("Enter new details for the student:")
                Stu_Data=[]
                print("Enter Student Name : ")
                name=input()
                print("Enter division: ")
                division=input()
                print("Enter semester: ")
                semester=input()
                print("Enter State : ")
                state=input()
                print("Enter District : ")
                District=input()
                print("Enter Contact No. :")
                Contactno=int(input())
                print("Enter Gr. Number : ")
                GRnumber=int(input())
                print("Enter Enrollment Number : ")
                Enrollnumber=int(input())
                print("Enter Gender : ")
                gender=input()
                print("Enter Degree(BTECH CSE AI&ML OR BTECH CSE AI&DS :)")
                degree=input()
                Stu_Data={"Name":name,"Division":division,"semester":semester,"State":state,"District":District,"Contact No.":Contactno,"Gr No.":GRnumber,"Enrollment No.":Enrollnumber,"Gender":gender,"Degree":degree}
                updated_data.append(Stu_Data)
            else:
                updated_data.append(row)
    with open("students.csv","w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["Name","Division","semester","State","District","Contact No.","Gr No.","Enrollment No.","Gender","Degree"])
        writer.writeheader()
        writer.writerows(updated_data)
        print("Student record updated successfully.")
def menu():
    while True:
        print("""
              --- --- --- --- --- Menu --- --- --- --- ---
              1. Display Student Record
              2. Add Student Record
              3. Delete Student Record
              4. Update Student Record 
              5. Exit

              Enter Choice(1/2/3/4/5) : """)
        choice=int(input())
        if choice==1:
            display()
        elif choice==2:
            insert()
        elif choice==3:
            delete()
        elif choice==4:
            update()
        elif choice==5:
            print("Exit successfully")
            break
        else :
            print("Invalid Choice.")
        
menu()
        
