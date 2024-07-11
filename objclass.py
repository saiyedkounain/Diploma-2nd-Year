#objects and class
def displayStudents(name1,name2,name3):
    name1.displayStudent()
    name2.displayStudent()
    name3.displayStudent()
    

    
    
class Student ():
    ls = []
    #Constructor
    def __init__(self,name,age,reg,marks1,marks2):
        self.name = name
        self.age =age
        self.reg = reg
        self.marks1 = marks1
        self.marks2 = marks2
    #Method to accept data
        
    def accept (name,rn,marks1,marks2):
        
        ob = Student (name,rn,amrks1,marks2)
        self.displayStudent()
        ls.append(ob)
    #Method to display Student Info
    def displayStudent(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Register Number: ",self.reg)
        print("Marks M1: ",self.marks1)
        print("Marks M2: ",self.marks2)
    


        

sk = Student("Saiyed K",17,51,98,97)
rs = Student ("Raseena",17,54,99,98)
st = Student ("Stuff",17,55,87,67)
oper = int (input("Enter 1.To Display 2.To Add: "))
if (oper==1):
    displayStudents(sk,rs,st)
elif (oper ==2):
    name = input("Enter name: ")
    rn = int(input("Enter reg: "))
    marks1 = int(input("Enter Marks1: "))
    marks2 = int(input("Enter Marks2: "))
    Student.accept(name,rn,marks1,marks2)
    
    
