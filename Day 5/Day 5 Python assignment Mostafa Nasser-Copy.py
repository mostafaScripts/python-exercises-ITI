
"""1- Create class employee with the following characteristics:
●Attributes:
    ○ First_name
    ○ Last_name
    ○ Age
    ○ Department
    ○ Salary
    ○ Static list contains all employee
●Methods:
    ○ constructor
        ■ Assign values to the instance attributes
        ■ Insert the created object to the list
        ■ Insert new record in table employee in database
    ○ transfer()
        ■ Change employee department
        ■ Update the database record with the update
    ○ fire()
        ■ Remove the employee from the shared list
        ■ Delete its record from the database
    ○ show()
        ■ Prints all employee data
    ○ List_employees()
        ■ Select all employees and print their data"""



import mysql.connector

class Employee():        

    def __init__(self):
        self.myCon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2512",
        database="employees")
        print("Connected Successfully")
        self.myCon.commit()
        self.myCon.close()
    
    def createTable(self):
        mycursor = self.myCon.cursor()
        mycursor.execute('''create table emp_info(
                    fname char(50),
                    lname char(50),
                     age int not null,
                     department char(50),
                     salary int
                     );''')
        print('Table Created successfully')
        self.myCon.commit()
        self.myCon.close()
    

    def addEmployee(self):
        mycursor= self.myCon.cursor()
        mycursor.execute('''INSERT INTO emp_info
        VALUES ("mostafa", "nasser", 23, "engineering",8000);''')
        print('Record inserted successfully')
        mycursor.execute('''INSERT INTO emp_info
        VALUES ("Amr", "Salama", 25, "Business Development",5000);''')
        mycursor.execute('''INSERT INTO emp_info
        VALUES ("radwan", "mansor", 50, "Managment",20000);''')
        mycursor.execute('''INSERT INTO emp_info
        VALUES ("marwa", "el-sayed", 35, "HR",6500);''')
        mycursor.execute('''INSERT INTO emp_info
        VALUES ("maged", "asaadi", 45, "Managment",12000);''')

        print('Record inserted successfully')
        mycursor.execute('''select * from emp_info;''')
        rows = mycursor.fetchall()
        # print(rows)
        for row in rows:
            print(row)
        self.myCon.commit()
        self.myCon.close()




    def transfer(self):
        mycursor= self.myCon.cursor()
        mycursor.execute('''update emp_info
                            set department = "Accounting"
                            where fname    = "Amr" ;''')

        print("Department Updated successfully")
        mycursor.execute('''select * from emp_info;''')
        rows = mycursor.fetchall()
        # print(rows)
        for row in rows:
            print(row)
        self.myCon.commit()
        self.myCon.close()   



    def showAll(self):
        mycursor= self.myCon.cursor()
        mycursor.execute('''SELECT * FROM emp_info;''')
        rows = mycursor.fetchall()
        print("Selection completed successfully")
        for row in rows:
            print(row)
        self.myCon.close()




    def fire(self):
        mycursor= self.myCon.cursor()
        mycursor.execute('''DELETE FROM emp_info WHERE age = "45";''')
        rows = mycursor.fetchall()
        print("row deleted successfully")
        mycursor.execute('''select * from emp_info;''')
        rows = mycursor.fetchall()
        # print(rows)
        for row in rows:
            print(row)
        self.myCon.close()





