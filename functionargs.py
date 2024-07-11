#function args kwargs and default
def greet(name,msg="How you doing?"):
    print("Hello!",name,msg)
greet("kounain")
#aargs (arbituary arguments) when we do not define how many parameters in a function
def adder (*num):
    sum=0
    for n in num:
        sum=sum+n
    print("The sum is: ",sum)
adder(5,10,10,12,13,15)
#kwaargs (keyword arbituary arguements) when we do not know the how many keywords are there for value of the parameter
def display_name(**kid):
    print("His last name is ",kid["lname"])
display_name(fname="Saiyed",lname="Kounain")
