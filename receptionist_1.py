import mysql.connector as mysql 

def hash():
    print("--------------------------------------------------------------------------------------------------------------------")

class receptionist_1_student_section:

    # constructor ======================================================================================
    def __init__(self):
        self.data_base = mysql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="infinityacademy")
        cur = self.data_base.cursor()

    # Add student ======================================================================================
    def add_student(self,class_student):
        print("")
        id = input("Enter  id :")                                           # varchar(20)
        name = input("Enter name : ")                                       # varchar(50)
        f_name = input("Enter father name : ")                              # varchar(50)
        addmission = input("Addmission date (dd-mm-yyyy): ")                # varchar(50) 
        address = input("Enter address : ")                                 # varchar(250)
        contact = input("Enter contact no : ")                              # varchar(20)
        fees = int(input("Enter fees : "))                                       # varchar(20)
        if id == "" or name=="" or f_name=="" or addmission=="" or address=="" or contact=="" or fees=="":
            print("\n\tERROR ::: ANY field is missing")
        else:
            cur = self.data_base.cursor()
            query = f"select * from class_{class_student} where id='{id}'"
            cur.execute(query)
            check = True
            for row in cur:
                check = False
            if check ==  False:
                print(f"\n\t ERROR ::: Student with this id ({id}) already exist.Id must be unique.So give it another (ID)")
            else: 
                cur = self.data_base.cursor()
                query = f"insert into class_{class_student} (id,name,father,addmission,address,contact,fees,fees_status,balance) values ('{id}','{name}','{f_name}','{addmission}','{address}','{contact}',{fees},'0',0)"
                cur = self.data_base.cursor()
                cur.execute(query)
                self.data_base.commit()
                print(f"\n\tstudent {name} added successfully in class {class_student}th")

    # Search student ======================================================================================
    def search_student(self,class_student):
        id = input("Enter id of student : ")
        if id == "":
            print("\n\tERROR ::: Field is missing.Try again!")
        else:
            query = f"select * from class_{class_student} where id='{id}'"
            cur = self.data_base.cursor()
            cur.execute(query)                        
            check = True
            for row in cur:
                print("")
                print("Student detalis :---")
                print("Name of student is : ",row[1])
                print("Father name of student is : ",row[2])
                print("Addmission date : ",row[3])
                print("Address of student is : ",row[4])
                print("Contact of student is : ",row[5])
                print("Fees : ",row[6])
                check = False
            if check == True:
                print(f"\n\tERROR ::: Student of {id} not found in class {class_student}")
        
    # Update student ======================================================================================
    def update_student(self,class_student):
        id = input("Enter id of student : ")
        if id == "":
            print("\n\t ERROR ::: Field is missing.Try again!")
        else:
            query = f"select * from class_{class_student} where id='{id}'"
            cur = self.data_base.cursor()
            cur.execute(query)
            check = False
            for row in cur:
                print("Student detalis :---")
                print("Name of student is : ",row[1])
                print("Father name of student is : ",row[2])
                print("Addmission date : ",row[3])
                print("Address of student is : ",row[4])
                print("Contact of student is : ",row[5])
                print("Fees : ",row[6])
                check = True
            if check == True:
                print("")
                hash()
                print("1. Update particular field of record")
                print("2. Update whole record")
                hash()
                update_choice = int(input("\tEnter your decision : "))
                if update_choice == int():
                    print("\n\tERROR ::: You do not enter any decision")
                else:
                    if update_choice == 2:
                        print("Enter new details :---")
                        new_name = input("Enter student name : ")
                        new_f_name = input("Enter father name : ")
                        new_addmission = input("Enter addmission date (dd-mm-yyyy) : ")            
                        new_address = input("Enter address : ")                                 
                        new_contact = input("Enter contact no : ")                              
                        new_fees = int(input("Enter fees : "))
                        if new_name == "" or new_f_name == "" or new_addmission == "" or new_address == "" or new_contact == "":
                            print("\n\tERROR ::: Any field is missing")
                        else:
                            query = f"update class_{class_student} set name='{new_name}',father='{new_f_name}',addmission = '{new_addmission}',address='{new_address}',contact='{new_contact}',fees={new_fees} where id='{id}'"
                            cur = self.data_base.cursor()
                            cur.execute(query)
                            self.data_base.commit()
                            print("\n\tStudent successfully updated")
                    elif update_choice == 1:
                        print("")
                        hash()
                        print("1. Edit student name  ")
                        print("2. Edit father name  ")
                        print("3. Edit addmission date ")
                        print("4. Edit address")
                        print("5. Edit contact")
                        print("6. Edit fees")
                        hash()
                        up = int(input("\tEnter your decision : "))
                        if up == 1:
                            new_name = input("Enter name : ")
                            if new_name == "":
                                print("\n\tERROR ::: Field is missing")
                            else:
                                query = f"update class_{class_student} set name='{new_name}' where id ='{id}'" 
                                cur = self.data_base.cursor()
                                cur.execute(query)
                                self.data_base.commit()
                                print("\n\tStudent (name) successfully updated")
                        elif up == 2:
                            new_f_name = input("Enter father name : ")
                            if new_f_name == "":
                                print("\n\tERROR ::: Field is missing")
                            else:
                                query = f"update class_{class_student} set father='{new_f_name}' where id='{id}'"
                                cur = self.data_base.cursor()
                                cur.execute(query)
                                self.data_base.commit()
                                print("\n\tStudent (father name) is successfully updated")
                        elif up == 3:
                            new_addmission_date = input("Enter addmission date (dd-mm-yyyy) : ")
                            if new_addmission_date == "":
                                print("\n\tERROR ::: Field is missing")
                            else:
                                query = f"update class_{class_student} set addmission='{new_addmission_date}' where id='{id}'"
                                cur = self.data_base.cursor()
                                cur.execute(query)
                                self.data_base.commit()
                                print("\n\t Student (addmission date) is successfully updated")
                        elif up == 4:
                            new_address = input("Enter address : ")
                            if new_address == "":
                                print("\n\tERROR ::: Field is missing")
                            else:
                                query = f"update class_{class_student} set address='{new_address}' where id='{id}'"
                                cur = self.data_base.cursor()
                                cur.execute(query)
                                self.data_base.commit()
                                print("\n\tStudent (address) successfully updated")
                        elif up == 5:
                            new_contact = input("Enter contact : ")
                            if new_contact == "":
                                print("\n\tERROR ::: Field is missing")
                            else:
                                query = f"update class_{class_student} set contact='{new_contact}' where id='{id}'"
                                cur = self.data_base.cursor()
                                cur.execute(query)
                                self.data_base.commit()
                                print("\n\tStudent (contact) successfully updated")
                        elif up == 6:
                            new_fees = int(input("Enter fees : "))
                            if new_fees == "":
                                print("\n\tERROR ::: Field is missing")
                            else:
                                query = f"update class_{class_student} set fees={new_fees} where id='{id}'"
                                cur = self.data_base.cursor()
                                cur.execute(query)
                                self.data_base.commit()
                                print("\n\tStudent (fees) successfully updated")
                        else:
                            print("\n\tERROR ::: Invalid choice")
                    else:
                        print("\n\tERROR ::: Invalid choice")
            else:
                print(f"\n\tERROR ::: Student of {id} not found in class {class_student}")            

    # Delete student ======================================================================================
    def delete_student(self,class_student):
        print("")
        hash()
        print(f"1. Delete one student from class {class_student}th")
        print(f"2. Delete all students from class {class_student}th")
        hash()
        delete_choice = int(input("\tEnter your decision : "))
        if delete_choice == "":
            print("\n\tERROR ::: You do not enter any decision")
        else:
            if delete_choice == 1:
                id = input("Enter id of student : ")
                if id == "":
                    print("\n\tERROR ::: Field is missing.Try again!")
                query = f"select * from class_{class_student} where id='{id}'"
                cur = self.data_base.cursor()
                cur.execute(query)
                check = False
                for row in cur:
                    check = True
                if check == True:
                    query = f"delete from class_{class_student} where id='{id}'"
                    cur = self.data_base.cursor()
                    cur.execute(query)
                    self.data_base.commit()
                    print(f"\n\tStudent with id ({id}) successfully deleted")
                else:
                    print(f"\n\tERROR ::: Student with id ({id}) not exist")
            elif delete_choice == 2:
                query = f"delete from class_{class_student}"
                cur = self.data_base.cursor()
                cur.execute(query)
                self.data_base.commit()
                print(f"\n\tAll students from ({class_student}) successfully deleted")
            else:
                print("\n\tERROR ::: Invalid choice")


    # Fees submission ======================================================================================
    def show_students(self,class_student):
        cur = self.data_base.cursor()
        query = f"select * from class_{class_student}"
        cur.execute(query)
        k=0
        print("     Id , Name , Father , Addmission_date , Address , Contact , Fees")
        for row in cur:
            k = k+1
            print("")
            print(f"{k} ... {row[0]} , {row[1]} , {row[2]} , {row[3]} , {row[4]} , {row[5]} , {row[6]}")

# end