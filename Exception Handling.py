#exception Handling
try:
    a=int(input("Enter a number"))
    print(a)
except ValueError as e:
    print("Error Integer Only!!")
