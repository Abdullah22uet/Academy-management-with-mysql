# giving usernames to user who check the working of program
print("FOR demo only...")
print("head user name = head")
print("head password = 123")
print("reptionist 1 username = employee1")
print("reptionist 1 password = 123")
print("reptionist 2 username = employee2")
print("reptionist 3 password = 123")
print("")
print("")

import mysql.connector as mysql 
data_base = mysql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="infinityacademy")

# importing receptionist 1 file
# importing student section file
from receptionist_1 import receptionist_1_student_section
obj_receptionist_1_student = receptionist_1_student_section()

# importing receptionist 2 file
from receptionist_2 import receptionist_2
obj_receptionist_2 = receptionist_2()

# importing head file
from head import head_section
obj_head = head_section()

# for presentation only
def hash():
    print("--------------------------------------------------------------------------------------------------------------------")

# class 
class deal: 

    # receptionist 1
    def receptionist_1(self):
        while 1:

            # main section  =========================================================
            hash()
            print("")
            print("1. Student section")
            print("2. Teacher section")
            print("3. Logout")
            print("")
            hash()
            try:
                choice = int(input("\tEnter your decision : "))
                if choice == 1:
                    while 1:

                # student section ==================================================
                        print("")
                        hash()
                        print("1. Add student")
                        print("2. Search student")
                        print("3. Update student record")
                        print("4. Delete student record")
                        print("5. Show all students")
                        print("6. Logout")
                        print("")
                        hash()
                        try:
                            dec = int(input("\tEnter your decision : "))
                            
                            if dec == 1:    # add student ==========================
                                while 1:

                                    print("")
                                    hash()
                                    print("select class???")
                                    print("1. 9th")
                                    print("2. 10th")
                                    print("3. 11th")
                                    print("4. 12th")
                                    print("5. Logout")
                                    print("")
                                    hash()
                                    try:
                                        class_dec = int(input("\tEnter your decision :  "))
                                        if class_dec == 1:
                                            obj_receptionist_1_student.add_student(9)
                                        elif class_dec ==2 :
                                            obj_receptionist_1_student.add_student(10)
                                        elif class_dec == 3:
                                            obj_receptionist_1_student.add_student(11)
                                        elif class_dec == 4:
                                            obj_receptionist_1_student.add_student(12)
                                        elif class_dec == 5:
                                            print("\n\tsuccessfully exit")
                                            break
                                        else:
                                            print("\n\tERROR ::: Invalid choice")
                                    except ValueError:
                                        print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                            
                            elif dec == 2:      # search student ========================
                                while 1:
                                    print("")
                                    hash()
                                    print("select class???")
                                    print("1. 9th")
                                    print("2. 10th")
                                    print("3. 11th")
                                    print("4. 12th")
                                    print("5. Logout")
                                    print("")
                                    hash()
                                    try:
                                        class_dec = int(input("\tEnter your decision :  "))
                                        if class_dec == 1:
                                            obj_receptionist_1_student.search_student(9)
                                        elif class_dec ==2 :
                                            obj_receptionist_1_student.search_student(10)
                                        elif class_dec == 3:
                                            obj_receptionist_1_student.search_student(11)
                                        elif class_dec == 4:
                                            obj_receptionist_1_student.search_student(12)
                                        elif class_dec == 5:
                                            print("\n\tsuccessfully exit")
                                            break
                                        else:
                                            print("\n\tERROR ::: Invalid choice")
                                    except ValueError:
                                        print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                            
                            elif dec == 3:      # update student ======================================
                                while 1:
                                    print("")
                                    hash()
                                    print("select class???")
                                    print("1. 9th")
                                    print("2. 10th")
                                    print("3. 11th")
                                    print("4. 12th")
                                    print("5. Logout")
                                    print("")
                                    hash()
                                    try:
                                        class_dec = int(input("\tEnter your decision :  "))
                                        if class_dec == 1:
                                            obj_receptionist_1_student.update_student(9)
                                        elif class_dec ==2 :
                                            obj_receptionist_1_student.update_student(10)
                                        elif class_dec == 3:
                                            obj_receptionist_1_student.update_student(11)
                                        elif class_dec == 4:
                                            obj_receptionist_1_student.update_student(12)
                                        elif class_dec == 5:
                                            print("\n\tsuccessfully exit")
                                            break
                                        else:
                                            print("\n\tERROR ::: Invalid choice")
                                    except ValueError:
                                        print("ERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                            
                            elif dec == 4:      # delete student =================================
                                while 1:
                                    print("")
                                    hash()
                                    print("select class???")
                                    print("1. 9th")
                                    print("2. 10th")
                                    print("3. 11th")
                                    print("4. 12th")
                                    print("5. Logout")
                                    print("")
                                    hash()
                                    try:
                                        class_dec = int(input("\nEnter your decision :  "))
                                        if class_dec == 1:
                                            obj_receptionist_1_student.delete_student(9)
                                        elif class_dec ==2 :
                                            obj_receptionist_1_student.delete_student(10)
                                        elif class_dec == 3:
                                            obj_receptionist_1_student.delete_student(11)
                                        elif class_dec == 4:
                                            obj_receptionist_1_student.delete_student(12)
                                        elif class_dec == 5:
                                            print("\n\tsuccessfully exit")
                                            break
                                        else:
                                            print("\n\tERROR ::: Invalid choice")
                                    except ValueError:
                                        print("ERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                            
                            elif dec == 5:      # show students ===================================
                                while 1:
                                    print("")
                                    hash()
                                    print("select class???")
                                    print("1. 9th")
                                    print("2. 10th")
                                    print("3. 11th")
                                    print("4. 12th")
                                    print("5. Logout")
                                    print("")
                                    hash()
                                    try:
                                        class_dec = int(input("\tEnter your decision :  "))
                                        if class_dec == 1:
                                            obj_receptionist_1_student.show_students(9)
                                        elif class_dec ==2:
                                            obj_receptionist_1_student.show_students(10)
                                        elif class_dec == 3:
                                            obj_receptionist_1_student.show_students(11)
                                        elif class_dec == 4:
                                            obj_receptionist_1_student.show_students(12)
                                        elif class_dec == 5:
                                            print("\n\tsuccessfully exit")
                                            break
                                        else:
                                            print("\n\tERROR ::: Invalid choice")
                                    except ValueError:
                                        print("ERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                                                        
                            elif dec == 6:      # logout ==============================================
                                print("\n\t Receptionist 1 successfully logout from student section")
                                break
                            
                            else:
                                print("\n\t ERROR ::: Invalid choice")
                        except ValueError:
                            print("ERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")

                elif choice == 2:
                
                # Teacher section ===================================================================
                    while 1:
                        print("")
                        hash()
                        print("1. Add Teacher")
                        print("2. Search Teacher")
                        print("3. Update teacher record")
                        print("4. Delete teacher record")
                        print("5. Check what classes the teacher teach")
                        print("6. Show all teachers")
                        print("7. Logout")
                        hash()
                        try:
                            dec = int(input("\tEnter your decision : "))
                            # add teacher =======================================================
                            if dec == 1: 
                                print("") 
                                t_id = input("Enter id : ")                 # varchar(50)
                                t_name = input("Enter name : ")             # varchar(50)
                                t_address = input("Enter address : ")       # varchar(50)
                                t_contact = input("Enter contact : ")       # varchar(50)
                                t_salary = int(input("Enter salary : "))    # int
                                print("")
                                print("Classes which teacher teach???")
                                t_class1 = input("Class 1 : ")              # varchar(50)
                                t_subject1 = input("Subject :")             # varchar(50)
                                t_class2 = input("Class 2 : ")              # varchar(50)
                                t_subject2 = input("Subject :")             # varchar(50)
                                t_class3 = input("Class 3 : ")              # varchar(50)
                                t_subject3 = input("Subject :")             # varchar(50)
                                t_class4 = input("Class 4 : ")              # varchar(50)
                                t_subject4 = input("Subject :")             # varchar(50)
                                t_class5 = input("Class 5 : ")              # varchar(50)
                                t_subject5 = input("Subject :")             # varchar(50)
                                if t_id == "" or t_name == "" or t_address == "" or t_contact == "" or (t_class1 == "" and t_subject1 ==  "" and t_class2 == "" and t_subject2 ==  "" and t_class3 == "" and t_subject3 ==  "" and t_class4 == "" and t_subject4 ==  "" and t_class5 == "" and t_subject5 ==  "" ):
                                    print("\n\tERROR ::: It seems that any field is missing or it may be that you dont enter any class for teacher. Teacher must atleast one class")
                                    break
                                if t_class1 == "9" or t_class1 == "10" or t_class1 == "11" or t_class1 == "12" or t_class1=="": 
                                    if t_class2 == "9" or t_class2 == "10" or t_class2 == "11" or t_class2 == "12" or t_class2=="":
                                        if t_class3 == "9" or t_class3 == "10" or t_class3 == "11" or t_class3 == "12" or t_class3=="":
                                            if t_class4 == "9" or t_class4 == "10" or t_class4 == "11" or t_class4 == "12" or t_class4=="":
                                                if t_class5 == "9" or t_class5 == "10" or t_class5 == "11" or t_class5 == "12" or t_class5=="":
                                                    if t_class1=="" and t_class2=="" and t_class3=="" and t_class4=="" and t_class5 == "":
                                                        print("\n\tERROR ::: Teacher much atleast one class.Try again!")
                                                    else:
                                                        cur = data_base.cursor()
                                                        query = f"select * from teacher where id='{t_id}'"
                                                        cur.execute(query)
                                                        check = True
                                                        for row in cur:
                                                            check = False
                                                        if check ==  False:
                                                            print(f"\n\tTeacher with this id ({t_id}) already exist.Id must be unique.So use another (ID)")
                                                            break
                                                        if (len(t_class1)>0 and len(t_subject1)==0) or (len(t_class1)==0 and len(t_subject1)>0):
                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                            break
                                                        if (len(t_class2)>0 and len(t_subject2)==0) or (len(t_class2)==0 and len(t_subject2)>0):
                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                            break
                                                        if (len(t_class3)>0 and len(t_subject3)==0) or (len(t_class3)==0 and len(t_subject3)>0):
                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                            break
                                                        if (len(t_class4)>0 and len(t_subject4)==0) or (len(t_class4)==0 and len(t_subject4)>0):
                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                            break
                                                        if (len(t_class5)>0 and len(t_subject5)==0) or (len(t_class5)==0 and len(t_subject5)>0):
                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                            break
                                                        else: 
                                                            query = f"insert into teacher values ('{t_id}','{t_name}','{t_address}','{t_contact}',{t_salary},'{t_class1}','{t_subject1}','{t_class2}','{t_subject2}','{t_class3}','{t_subject3}','{t_class4}','{t_subject4}','{t_class5}','{t_subject5}')"
                                                            cur = data_base.cursor()
                                                            cur.execute(query)
                                                            data_base.commit()
                                                            print(f"\n\tTeacher {t_name} added successfully")
                                                else:
                                                    print("\n\tERROR ::: Wrong class")    
                                            else:
                                                print("\n\tERROR ::: Wrong class")
                                        else:
                                            print("\n\tERROR ::: Wrong class")
                                    else:
                                        print("\n\tERROR ::: Wrong class")
                                else:
                                    print("\n\tERROR ::: Wrong class")

                            # Search teacher =======================================================
                            elif dec == 2:
                                print("\n")
                                t_id = input("Enter id : ")
                                query = f"select * from teacher where id='{t_id}'"
                                cur = data_base.cursor()
                                cur.execute(query)
                                check = False
                                for row in cur:
                                    check = True
                                if check == False:
                                    print(f"\n\tTeacher with this id {t_id} not exist.Try again!")
                                else:
                                    print("")
                                    print("Details of teacher :---")
                                    print(f"Name : {row[1]}")
                                    print(f"Address : {row[2]}")
                                    print(f"Contact : {row[3]}")
                                    print(f"Salary : {row[4]}")
                                    print("")
                                    print("Teaching classes :---")
                                    print(f"Class 1 : {row[5]}",end="")
                                    print(f" , Subject : {row[6]}")
                                    print(f"Class 2 : {row[7]}",end="")
                                    print(f" , Subject : {row[8]}")
                                    print(f"Class 3 : {row[9]}",end="")
                                    print(f" , Subject : {row[10]}")
                                    print(f"Class 4 : {row[11]}",end="")
                                    print(f" , Subject : {row[12]}")
                                    print(f"Class 5 : {row[13]}",end="")
                                    print(f" , Subject : {row[14]}")
                                    
                            # update teacher =======================================================        
                            elif dec == 3:
                                print("")
                                t_id = input("Enter id : ")
                                query = f"select * from teacher where id='{t_id}'"
                                cur = data_base.cursor()
                                cur.execute(query)
                                check = False
                                print("Details of teacher are :---")
                                for row in cur:
                                    print(f"Name : {row[1]}")
                                    print(f"Address : {row[2]}")
                                    print(f"Contact : {row[3]}")
                                    print(f"Salary : {row[4]}")
                                    print(f"Class 1 : {row[5]}")
                                    print(f"Subject : {row[6]}")
                                    print(f"Class 2 : {row[7]}")
                                    print(f"Subject : {row[8]}")
                                    print(f"Class 3 : {row[9]}")
                                    print(f"Subject : {row[10]}")
                                    print(f"Class 4 : {row[11]}")
                                    print(f"Subject : {row[12]}")
                                    print(f"Class 5 : {row[13]}")
                                    print(f"Subject : {row[14]}")
                                    check = True
                                if check==True:
                                    print("")
                                    hash()
                                    print("Which field you want to update:---")
                                    print("1. Update all record")
                                    print("2. Update particular field of record")
                                    hash()
                                    try:
                                        dec = int(input("\tEnter decision : "))
                                        if dec == 1:
                                            print("Enter new details :---")
                                            n_tname = input("Name : ")
                                            n_taddress = input("Address : ")
                                            n_tcontact = input("Contact : ")
                                            n_salary = int(input("Salary : "))
                                            n_class1 = input("Class 1 : ")
                                            n_subject1 = input("Subject : ")
                                            n_class2 = input("Class 2 : ")
                                            n_subject2 = input("Subject : ")
                                            n_class3 = input("Class 3 : ")
                                            n_subject3 = input("Subject : ")
                                            n_class4 = input("Class 4 : ")
                                            n_subject4 = input("Subject : ")
                                            n_class5 = input("Class 5 : ")
                                            n_subject5 = input("Subject : ")
                                            if n_tname =="" or n_taddress == "" or n_tcontact == "" or n_salary=="" or (n_class1=="" and n_subject1=="" and n_class2=="" and n_subject2=="" and n_class3=="" and n_subject3=="" and n_class4=="" and n_subject4=="" and n_class5=="" and n_subject5==""):
                                                print("\n\tERROR ::: It seems that any field is missing or it may be that you dont enter any class for teacher. Teacher must atleast one class")
                                                break
                                            if n_class1 == "9" or n_class1 == "10" or n_class1 == "11" or n_class1 == "12" or n_class1=="": 
                                                if n_class2 == "9" or n_class2 == "10" or n_class2 == "11" or n_class2 == "12" or n_class2=="":
                                                    if n_class3 == "9" or n_class3 == "10" or n_class3 == "11" or n_class3 == "12" or n_class3=="":
                                                        if n_class4 == "9" or n_class4 == "10" or n_class4 == "11" or n_class4 == "12" or n_class4=="":
                                                            if n_class5 == "9" or n_class5 == "10" or n_class5 == "11" or n_class5 == "12" or n_class5=="":
                                                                if n_class1=="" and n_class2=="" and n_class3=="" and n_class4=="" and n_class5=="":
                                                                    print("\n\tERROR ::: Teacher much atleast one class.Try again!")
                                                                else:
                                                                    cur = data_base.cursor()
                                                                    query = f"select * from teacher where id='{t_id}'"
                                                                    cur.execute(query)
                                                                    check = True
                                                                    for row in cur:
                                                                        check = False
                                                                    if check ==  False:
                                                                        print(f"\n\tTeacher with this id ({t_id}) already exist.Id must be unique.So use another (ID)")
                                                                        break
                                                                    if (len(n_class1)>0 and len(n_subject1)==0) or (len(n_class1)==0 and len(n_subject1)>0):
                                                                        print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                        break
                                                                    if (len(n_class2)>0 and len(n_subject2)==0) or (len(n_class2)==0 and len(n_subject2)>0):
                                                                        print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                        break
                                                                    if (len(n_class3)>0 and len(n_subject3)==0) or (len(n_class3)==0 and len(n_subject3)>0):
                                                                        print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                        break
                                                                    if (len(n_class4)>0 and len(n_subject4)==0) or (len(n_class4)==0 and len(n_subject4)>0):
                                                                        print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                        break
                                                                    if (len(n_class5)>0 and len(n_subject5)==0) or (len(n_class5)==0 and len(n_subject5)>0):
                                                                        print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                        break
                                                                    else: 
                                                                        query = f"update teacher set name='{n_tname}' and address='{n_taddress}' and contact='{n_tcontact}' and salary={n_salary} and class_1='{n_class1}' and subject_1='{n_subject1}' and class_2='{n_class2}' and subject_2='{n_subject2}' and class_3='{n_class3}' and subject_3='{n_subject3}' and class_4='{n_class4}' and subject_4='{n_subject4}' and class_5='{n_class5}' and subject_5='{n_subject5}' where id='{t_id}'"
                                                                        cur.execute(query)
                                                                        data_base.commit()
                                                                        print(f"\n\tTeacher with id ({t_id}) successfully updated")
                                                            else:
                                                                print("\n\tERROR ::: Wrong class")
                                                        else:
                                                            print("\n\tERROR ::: Wrong class")
                                                    else:
                                                        print("\n\tERROR ::: Wrong class")
                                                else:
                                                    print("\n\tERROR ::: Wrong class")
                                            else:
                                                print("\n\tERROR ::: Wrong class")

                                                
                                        elif dec == 2:
                                            print("")
                                            hash()
                                            print("Which field you want to update:---")
                                            print("1. Name")
                                            print("2. Address")
                                            print("3. Contact")
                                            print("4. Salary")
                                            print("5. Classes")
                                            print("")
                                            hash()
                                            choice=int(input("\tEnter your decision : "))
                                            if choice==1:
                                                print("")
                                                new_name = input("Enter new name : ")
                                                if new_name == "":
                                                    print("\n\tERROR ::: Field is empty")
                                                else:
                                                    query = f"update teacher set name='{new_name}' where id='{t_id}'"
                                                    cur = data_base.cursor()
                                                    cur.execute(query)
                                                    data_base.commit()
                                                    print("Teacher (name) successfully updated")
                                            elif choice==2:
                                                print("")
                                                new_address = input("Enter new address : ")
                                                if new_address == "":
                                                    print("\n\tERROR ::: Field is empty")
                                                else:
                                                    query = f"update teacher set address='{new_address}' where id='{t_id}'"
                                                    cur = data_base.cursor()
                                                    cur.execute(query)
                                                    data_base.commit()
                                                    print("Teacher (address) successfully updated")
                                            elif choice==3:
                                                print("")
                                                new_contact = input("Enter new contact : ")
                                                if new_contact == "":
                                                    print("\n\tERROR ::: Field is empty")
                                                else:
                                                    query = f"update teacher set contact='{new_contact}' where id='{t_id}'"
                                                    cur = data_base.cursor()
                                                    cur.execute(query)
                                                    data_base.commit()
                                                    print("Teacher (contact) successfully updated")
                                            elif choice==4:
                                                print("")
                                                new_salary = input("Enter new salary : ")
                                                if new_salary == "":
                                                    print("\n\tERROR ::: Field is empty")
                                                else:
                                                    query = f"update teacher set salary={new_salary} where id='{t_id}'"
                                                    cur = data_base.cursor()
                                                    cur.execute(query)
                                                    data_base.commit()
                                                    print("Teacher (salary) successfully updated")
                                            elif choice==5:
                                                print("")
                                                n_class1 = input("Class 1 : ")
                                                n_subject1 = input("Subject : ")
                                                n_class2 = input("Class 2 : ")
                                                n_subject2 = input("Subject : ")
                                                n_class3 = input("Class 3 : ")
                                                n_subject3 = input("Subject : ")
                                                n_class4 = input("Class 4 : ")
                                                n_subject4 = input("Subject : ")
                                                n_class5 = input("Class 5 : ")
                                                n_subject5 = input("Subject : ")

                                                if n_class1=="" and n_subject1=="" and n_class2=="" and n_subject2=="" and n_class3=="" and n_subject3=="" and n_class4=="" and n_subject4=="" and n_class5=="" and n_subject5=="":
                                                    print("\n\tERROR ::: It seems that any field is missing or it may be that you dont enter any class for teacher. Teacher must atleast one class")
                                                    break
                                                if n_class1 == "9" or n_class1 == "10" or n_class1 == "11" or n_class1 == "12" or n_class1=="": 
                                                    if n_class2 == "9" or n_class2 == "10" or n_class2 == "11" or n_class2 == "12" or n_class2=="":
                                                        if n_class3 == "9" or n_class3 == "10" or n_class3 == "11" or n_class3 == "12" or n_class3=="":
                                                            if n_class4 == "9" or n_class4 == "10" or n_class4 == "11" or n_class4 == "12" or n_class4=="":
                                                                if n_class5 == "9" or n_class5 == "10" or n_class5 == "11" or n_class5 == "12" or n_class5=="":
                                                                    if n_class1=="" and n_class2=="" and n_class3=="" and n_class4=="" and n_class5=="":
                                                                        print("\n\tERROR ::: Teacher much atleast one class.Try again!")
                                                                    else:
                                                                        cur = data_base.cursor()
                                                                        query = f"select * from teacher where id='{t_id}'"
                                                                        cur.execute(query)
                                                                        check = True
                                                                        for row in cur:
                                                                            check = False
                                                                        if check ==  False:
                                                                            print(f"\n\tTeacher with this id ({t_id}) already exist.Id must be unique.So use another (ID)")
                                                                            break
                                                                        if (len(n_class1)>0 and len(n_subject1)==0) or (len(n_class1)==0 and len(n_subject1)>0):
                                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                            break
                                                                        if (len(n_class2)>0 and len(n_subject2)==0) or (len(n_class2)==0 and len(n_subject2)>0):
                                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                            break
                                                                        if (len(n_class3)>0 and len(n_subject3)==0) or (len(n_class3)==0 and len(n_subject3)>0):
                                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                            break
                                                                        if (len(n_class4)>0 and len(n_subject4)==0) or (len(n_class4)==0 and len(n_subject4)>0):
                                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                            break
                                                                        if (len(n_class5)>0 and len(n_subject5)==0) or (len(n_class5)==0 and len(n_subject5)>0):
                                                                            print("\n\tERROR ::: It seems that you enter class but not enter subject or it may be that you do not enter class but enter subject.Try again!")
                                                                            break
                                                                        else: 
                                                                            cur = data_base.cursor()
                                                                            query = f"update teacher set class_1='{n_class1}',subject_1='{n_subject1}',class_2='{n_class2}',subject_2='{n_subject2}', class_3='{n_class3}' ,subject_3='{n_subject3}', class_4='{n_class4}' ,subject_4='{n_subject4}' ,class_5='{n_class5}',subject_5='{n_subject5}' where id='{t_id}'"
                                                                            cur.execute(query)
                                                                            data_base.commit()
                                                                            print("Teacher (classes) successfully updated")
                                                                else:
                                                                    print("\n\tERROR ::: Wrong class")
                                                            else:
                                                                print("\n\tERROR ::: Wrong class")
                                                        else:
                                                            print("\n\tERROR ::: Wrong class")
                                                    else:
                                                        print("\n\tERROR ::: Wrong class")
                                                else:
                                                    print("\n\tERROR ::: Wrong class")
                                            else:
                                                print("\n\tERROR ::: INVALID CHOICE ::: Try again!")
                                        else:
                                            print("\n\tERROR ::: INVALID CHOICE ::: Try again!")
                                    except ValueError:
                                        print("ERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                                else:
                                    print(f"\n\tTeacher with id {t_id} not found")

                            # delete teacher =======================================================
                            elif dec == 4:
                                print("")
                                hash()
                                print("Which you want to do?")
                                print("1. Delete particular record")
                                print("2. Delete the record of all teachers")
                                print("")
                                hash()
                                
                                try:
                                    dec = int(input("\tEnter your decision : "))
                                    if dec == 1:
                                        print("")
                                        t_id = input("Enter id of teacher : ")
                                        query = f"select * from teacher where id='{t_id}'"
                                        cur = data_base.cursor()
                                        cur.execute(query)
                                        check = False
                                        for row in cur:
                                            check = True
                                        if check == True:
                                            query = f"delete from teacher where id='{t_id}'"
                                            cur = data_base.cursor()
                                            cur.execute(query)
                                            data_base.commit()
                                            print(f"\n\tTeacher with id {t_id} successfully deleted")
                                        else:
                                            print(f"\n\tERROR ::: Teacher with this id {t_id} not exist")
                                    elif dec == 2:
                                        query = "delete from teacher"
                                        cur = data_base.cursor()
                                        cur.execute(query)
                                        data_base.commit()
                                        print("\n\tAll teachers record successfully deleted")
                                    else:
                                        print("\n\tERROR ::: Invalid Choice")
                                except ValueError:
                                    print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")

                            # classes the teacher teach ================================================
                            elif dec == 5:
                                print("")
                                hash()
                                print("Which class you want to chooses?")
                                print("1. Class 9th")
                                print("2. Class 10th")
                                print("3. Class 11th")
                                print("4. Class 12th")
                                print("")
                                hash()
                                try:
                                    def classes(class_range):
                                                if row[5]==class_range:
                                                    one=row[6]
                                                    print(one)
                                                else:
                                                    one=""
                                                if row[7]==class_range:
                                                    two=row[8]
                                                    print(two)
                                                else:
                                                    two=""
                                                if row[9]==class_range:
                                                    three=row[10]
                                                    print(three)
                                                else:
                                                    three=""
                                                if row[11]==class_range:
                                                    four=row[12]
                                                    print(four)
                                                else:
                                                    four=""
                                                if row[13]==class_range:
                                                    five=row[14]
                                                    print(five)
                                                else:
                                                    five=""
                                                if one=="" and two=="" and three=="" and four=="" and five=="":
                                                    pass
                                                else:
                                                    print(f"Teacher id   : {row[0]}")
                                                    print(f"Teacher name : {row[1]}")
                                                    print("")    
                                    decc = int(input("\tEnter your decision : "))
                                    if decc == 1:
                                        cur = data_base.cursor()
                                        query = f"select * from teacher"
                                        cur.execute(query)
                                        for row in cur:
                                            classes("9")
                                    elif decc == 2:
                                        cur = data_base.cursor()
                                        query = f"select * from teacher"
                                        cur.execute(query)
                                        for row in cur:
                                            classes("10")
                                    elif decc == 3:
                                        cur = data_base.cursor()
                                        query = f"select * from teacher"
                                        cur.execute(query)
                                        for row in cur:
                                            classes("11")
                                    elif decc == 4:
                                        cur = data_base.cursor()
                                        query = f"select * from teacher"
                                        cur.execute(query)
                                        for row in cur:
                                            classes("12")
                                    else:
                                        print("\n\tERROR ::: Invalid choice")
                                            
                                except ValueError:
                                    print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")

                            # show all teachers ============================================
                            elif dec == 6:
                                query = f"select * from teacher"
                                cur = data_base.cursor()
                                cur.execute(query)
                                a = 0
                                for c in cur:
                                    a = a + 1
                                    print(a,".....",f"Id = {c[0]}",",",f"Name = {c[1]}",",",f"Salary = {c[4]}")

                            # logout =======================================================
                            elif dec == 7:
                                print("\n\tReceptionist 1 successfully logout from teacher section")
                                break
                            else:
                                print("\n\tERROR ::: Invalid choice")
                        except ValueError:
                            print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                
                # logout from student and teacher section ===========================================
                elif choice == 3:
                    print("\n\tsuccessfully logout")
                    break

                # else case of student and teacher section =========================================
                else:
                    print("\n\tERROR ::: Invalid choice")
            except ValueError:
                print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")

    # head section =================================================================================
    def head(self):
        while 1:
            print("")
            hash()
            print("1. Total earning")  
            print("2. Logout")
            print("")
            hash()
            try:
                dec = int(input("Enter your decision : "))  
                if dec == 1:
                    print("")
                    hash()
                    print("1. Total earning from 'Whole Academy'")
                    print("2. Total earning from 'Individual class'")
                    print("3. Logout")
                    print("")
                    hash()
                    try:
                        choice = int(input("\tEnter your decision : "))
                        if choice == 1:
                            obj_head.whole_details()
                        elif choice == 2:
                            print("")
                            hash()
                            print("Which class you want to choose?")
                            print("1. Class 9th")
                            print("2. Class 10th")
                            print("3. Class 11th")
                            print("4. Class 12th")
                            print("")
                            hash()
                            choice = int(input("\tEnter decision : "))
                            if choice == 1:
                                obj_head.class_detalis(9)
                            elif choice == 2:
                                obj_head.class_detalis(10)
                            elif choice == 3:
                                obj_head.class_detalis(11)
                            elif choice == 4:
                                obj_head.class_detalis(12)
                            else:
                                print("\n\tERROR ::: Invalid choice")
                        elif choice == 3:
                            print("\n\tSuccessfully logout")
                            break
                        else:
                            print("\n\tERROR ::: Invalid choice")
                    except ValueError:
                        print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
                elif dec == 2:
                    print("\n\tHead of academy successfully logout...")
                    break
                else:
                    print("\n\tERROR ::: Invalid choice")
            except ValueError:
                print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")                    

    # receptionist 2 ======================================================================================
    def receptionist_2(self):
        while 1:
            print("")
            hash()
            print("1. Fees submission")
            print("2. See students who don't submitted fees")
            print("3. See students who submit their fees")
            print("4. See students who have balance panding")
            print("5. Delete fees record")
            print("6. Logout")
            print("")
            hash()
            try:
                dec = int(input("\tEnter your decision : "))
                
                # Fees-------Submission ===========================================
                if dec == 1:
                    print("")
                    hash()
                    print("Student belongs to which class?")
                    print("1. Class 9th")
                    print("2. Class 10th")
                    print("3. Class 11th")
                    print("4. Class 12th")
                    print("")
                    hash()
                    choice = int(input("\tEnter decision : "))
                    if choice == 1:
                        obj_receptionist_2.fees_submission(9)
                    elif choice == 2:
                        obj_receptionist_2.fees_submission(10)
                    elif choice == 3:
                        obj_receptionist_2.fees_submission(11)
                    elif choice == 4:
                        obj_receptionist_2.fees_submission(12)
                    else:
                        print("\n\tERROR ::: Invalid choice")

                # Stdents not submit fees ===========================================
                elif dec == 2:
                    print("")
                    hash()
                    print("Student belongs to which class?")
                    print("1. Class 9th")
                    print("2. Class 10th")
                    print("3. Class 11th")
                    print("4. Class 12th")
                    print("")
                    hash()
                    choice = int(input("\tEnter decision : "))
                    if choice == 1:
                        obj_receptionist_2.no_fees(9)
                    elif choice == 2:
                        obj_receptionist_2.no_fees(10)
                    elif choice == 3:
                        obj_receptionist_2.no_fees(11)
                    elif choice == 4:
                        obj_receptionist_2.no_fees(12)
                    else:
                        print("\n\tERROR ::: Invalid choice")
                
                # Stdents submit fees ===========================================
                elif dec == 3:
                    print("")
                    hash()
                    print("Student belongs to which class?")
                    print("1. Class 9th")
                    print("2. Class 10th")
                    print("3. Class 11th")
                    print("4. Class 12th")
                    print("")
                    hash()
                    choice = int(input("\tEnter decision : "))
                    if choice == 1:
                        obj_receptionist_2.yes_fees(9)
                    elif choice == 2:
                        obj_receptionist_2.yes_fees(10)
                    elif choice == 3:
                        obj_receptionist_2.yes_fees(11)
                    elif choice == 4:
                        obj_receptionist_2.yes_fees(12)
                    else:
                        print("\n\tERROR ::: Invalid choice")

                # Balance remaining ===========================================
                elif dec == 4:
                    print("")
                    hash()
                    print("Student belongs to which class?")
                    print("1. Class 9th")
                    print("2. Class 10th")
                    print("3. Class 11th")
                    print("4. Class 12th")
                    print("")
                    hash()
                    choice = int(input("\tEnter decision : "))
                    if choice == 1:
                        obj_receptionist_2.how_balance(9)
                    elif choice == 2:
                        obj_receptionist_2.how_balance(10)
                    elif choice == 3:
                        obj_receptionist_2.how_balance(11)
                    elif choice == 4:
                        obj_receptionist_2.how_balance(12)
                    else:
                        print("\n\tERROR ::: Invalid choice")

                # Delete record ===========================================
                elif dec == 5:
                    print("")
                    hash()
                    print("1. Delete record of all classes")
                    print("2. Deleter record of particular class")
                    print("")
                    hash()
                    try:
                        choice = int(input("\tEnter your decision : "))
                        if choice == 1:
                            cur = data_base.cursor()
                            query = f"update class_9 set fees_status='0',balance='0'"
                            cur.execute(query)
                            data_base.commit()
                            query = f"update class_10 set fees_status='0',balance='0'"
                            cur.execute(query)
                            data_base.commit()
                            query = f"update class_11 set fees_status='0',balance='0'"
                            cur.execute(query)
                            data_base.commit()
                            query = f"update class_12 set fees_status='0',balance='0'"
                            cur.execute(query)
                            data_base.commit()
                            print("\n\tFees records of all classes successfully deleted")
                        elif choice == 2:
                            print("")
                            hash()
                            print("Select the class?")
                            print("1. Class 9th")
                            print("2. Class 10th")
                            print("3. Class 11th")
                            print("4. Class 12th")
                            print("")
                            hash()
                            dec = int(input("\tEnter decision : "))
                            if dec == 1:
                                obj_receptionist_2.all_delete(9)
                            elif dec == 2:
                                obj_receptionist_2.all_delete(10)
                            elif dec == 3:
                                obj_receptionist_2.all_delete(11)
                            elif dec == 4:
                                obj_receptionist_2.all_delete(12)
                            else:
                                print("\n\tERROR ::: Invalid choice")
                    
                    except ValueError:
                        print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")

                # Logout ==============================================================
                elif dec == 6:
                    print("\n\tReceptionist 2 successfully logout")
                    break
                else:
                    print("\n\tERROR ::: Invalid choice")
            except ValueError:
                print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")
obj = deal()


# main part of program ====================================================================
while 1:
    print("")
    hash()
    print("******************* Infinity Academy *******************")
    print("")
    print("1. Head of Academy ")
    print("2. Receptionist 'one'")
    print("3. Receptionist 'two'")
    print("4. Logout")
    hash()
    print("")
    try:
        choice = int(input("\tEnter your decision : "))
        if choice == 1:     # Head of academy ==============================================
            username = input("\n\tEnter user name : ")
            password = input("\tEnter password : ")
            if username == "head":
                if password == "123":
                    print("\tSuccessfully login")
                    obj.head()
                else:
                    print("\tYou put wrong data")
            else:
                print("\tYou put wrong data")
        
        elif choice == 2:       # receptionist 1 ===========================================
            Username = input("Enter user name : ")
            Password = input("Enter password : ")
            if Username == "employee1":
                if Password == "123":
                    print("\tSuccessfully login")
                    obj.receptionist_1()
                else:
                    print("\tYou put wrong data")
            else:
                print("\tYou put wrong data")

        elif choice == 3:       # receptionist 2 ===========================================
            uSername = input("Enter user name : ")
            pAssword = input("Enter password : ")
            if uSername == "employee2":
                if pAssword == "123":
                    print("\tSuccessfully login")
                    obj.receptionist_2()
                else:
                    print("\tYou put wrong data")
            else:
                print("\tYou put wrong data")
        
        elif choice == 4:       # logout ===================================================
            print("\n\tsuccessfully logout from system")
            break

        else:           # false case
            print("\tInvalid choice.Kindly right enter your decision...")
    except ValueError:
        print("\n\tERROR ::: It seems whether dont enter any decision or enter an alphabet instead of integer")