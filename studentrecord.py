# Student Records Using Basic DS
ls = []
class Student:
    #Constructor
    def __init__(self, name, age , marks):
        self.name = name
        self.age = age
        self.marks = marks
    def displayStudent(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Marks: ",self.marks)
        print("------------")
    
    def addStudent(self):
        ls.append(self)
    def deleteStudent(self):
        del ls[self] 
def displayStudents():
    for i in (ls):
        i.displayStudent()
        
    
print("Select 1.To Display 2.To Add 3.To Delete 4.To Quit")


sk = Student("Saiyed K", 17, 97)
zq = Student ("Zulfi", 17, 98)
ls.append(sk)
ls.append(zq)
while True:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("The Students")
        displayStudents()
    elif ch == 2:
            obj = input("Enter obj name: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            marks = int(input("Enter marks: "))
            obj = Student (name, age, marks)
            obj.addStudent()
            for i in (ls):
                i.displayStudent()
    elif ch == 3:
        break
    

                    
