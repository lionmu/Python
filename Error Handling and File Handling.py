a=5
b=2

try:
    print("OPEN RESOURCE")
    a=int (input("ENTER THE VALUE OF A:"))
    b=int (input("ENTER THE VALUE OF B:"))
    print (a/b)
except ZeroDivisionError:
 print("SOMETHING WENT WRONG")
finally:
 print ("RESOURCE CLOSED")

