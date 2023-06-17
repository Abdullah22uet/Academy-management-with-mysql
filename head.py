import mysql.connector as mysql

class head_section:
 
    # constructor ======================================================================================
    def __init__(self):
        self.data_base = mysql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="infinityacademy")
        self.cur = self.data_base.cursor()

    # individual class details =========================================================================
    def class_detalis(self,class_student):
        query = f"select * from class_{class_student}"
        self.cur.execute(query)
        sum = 0
        a = 0
        for roe in self.cur:
            a = a + 1
            sum = sum + int(roe[6])
        print("")
        print(f"Total students are {a}")
        print(f"Total fees budget from class {class_student} is {sum}")

    # whole academy detalis ==============================================================================
    def whole_details(self):
        query= "select * from class_9"
        self.cur.execute(query)
        a1,a2,a3,a4 = 0,0,0,0
        sum1,sum2,sum3,sum4 = 0,0,0,0
        
        for row in self.cur:
            a1 = a1 + 1
            sum1 = sum1 + int(row[6])
        
        query = "select * from class_10"
        self.cur.execute(query)
        for row in self.cur:
            a2 = a2 + 1
            sum2 = sum2 + int(row[6])

        query = "select * from class_11"
        self.cur.execute(query)
        for row in self.cur:
            a3 = a3 + 1
            sum3 = sum3 + int(row[6])

        query = "select * from class_12"
        self.cur.execute(query)
        for row in self.cur:
            a4 = a4 + 1
            sum4 = sum4 + int(row[6])
        
        sum = sum1 + sum2 + sum3 + sum4
        a = a1 + a2 + a3 + a4
        print("")
        print(f"Total students are {a}")
        print(f"Total earining is {sum}")
# end