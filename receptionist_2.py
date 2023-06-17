import mysql.connector as mysql 

class receptionist_2:

    # constructor ======================================================================================
    def __init__(self):
        self.data_base = mysql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="infinityacademy")
        self.cur = self.data_base.cursor()

    # fees submittion ======================================================================================
    def fees_submission(self,class_student):
        student_id = input("Enter id of student : ")
        query = f"select * from class_{class_student} where id='{student_id}'"
        self.cur.execute(query)
        check = False
        if len(student_id)==0:
            print("\n\tERROR ::: Field is empty")
        else:
            for i in self.cur:
                print(f"Name : {i[1]}")
                print(f"Fees : {i[6]}")
                print(f"Status : {i[7]}")
                check = True
            
            
            if check == True:
                print("Fees submitted completely? y or n : ",end="")
                dec = input("")
                if dec == "y":
                    query = f"update class_{class_student} set fees_status='1' where id='{student_id}'"
                    self.cur.execute(query)
                    self.data_base.commit()
                    print(f"\n\tTransaction successfully received of student with id ({student_id}) of class ({class_student})")
                elif dec == "n":
                    print("How much balance remaining? : ",end="")
                    balance = input("")
                    query = f"update class_{class_student} set balance={balance} where id='{student_id}'"
                    self.cur.execute(query)
                    self.data_base.commit()
                    print(f"\n\tTransaction of student with id ({student_id}) received and balance ({balance}) is pending")
                else:
                    print("\n\tERROR ::: Invalid choice.Try again!")
            else:
                print(f"\n\tERROR ::: Student with id {student_id} not exist in class {class_student}")
            
    # no fees submit =================================================================================
    def no_fees(self,class_student):
        query = f"select * from class_{class_student}"
        self.cur.execute(query)
        a = 0
        b = 1
        for i in self.cur:
            if i[7] == "0" and i[8]=="0":
                a=a+1  
                print(a,".....",f"Id : {i[0]}",",",f"Name : {i[1]}")
            elif i[7]=="0" and i[8]!="0":
                c=a+1
                a=a+1
                print(c,".....",f"Id : {i[0]}",",",f"Name : {i[1]}",",", f"Balance remaining : {i[8]}")
            b = b+1
            
        print("")
        print(f"Total students are {b}")
    
    # yes fees submit ======================================================================================
    def yes_fees(self,class_student):
        query = f"select * from class_{class_student}"
        self.cur.execute(query)
        a = 0
        b=1
        for i in self.cur:
            if i[7] == "1" and i[8] == 0:
                a = a+1
                print(a,".....",f"Id : {i[0]}",",",f"Name : {i[1]}")
            else:
                pass
            b = b+1
        print("")
        print(f"Total students are {b}")

    # balance remaining ======================================================================================
    def how_balance(self,class_student):
        query = f"select * from class_{class_student}"
        self.cur.execute(query)
        a = 0
        b = 1 
        for i in self.cur:
            if i[8] == 0 : 
                pass      
            else:
                a=a+1
                print(a,".....",f"Id : {i[0]}",",",f"Name : {i[1]}",",", f"Balance remaining : {i[8]}")
            b=b+1
        print("")
        print(f"Total students are {b}")

    # delete record ======================================================================================
    def all_delete(self,class_student):
        query = f"update class_{class_student} set fees_status='0',balance=0"
        self.cur.execute(query)
        self.data_base.commit()
        print(f"\n\tFees record of class {class_student} successfully deleted")

# end