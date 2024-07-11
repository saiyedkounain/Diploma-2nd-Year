#dictionary
import sys
d={1:"Saiyed", 2:"Kounain",3:"Khan"}
d[3]="Yo"
del d[1]
print(d)
d1=dict(Name="John", age = 36,country="sweden")
print(d1)
val=d1.values()
print(val)
fk=d.fromkeys("Kounain")
print(fk)
