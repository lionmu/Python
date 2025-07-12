#Arithmetic operators perform arithmetic operations +-X/

# + operator Adds two numerals and concatinates or joins sequencies (they can be in form of strings,list,tuple etc)
#a=10
#b=20
#d=bool (True+False)
#c=a+b
#d="MYLAB"+"16.4"
#print(c,sep="/n")
#print (d)

#-operator subttracts two numerals
#a=10-5
#print (a)

# * operator performs two operations multiplying numbers
#calculate the area of a triangle

#Base=float (input("Enter Base in CM:"))
#Height=float (input("Enter Height in CM:"))
#Area=1/2*Base*Height
#print(Area,"CM")

#list1=[0]*10
#print(list1)

#logical Operators used to combine statements or boolean expressions
#THese Logical And Logical Or and Logical Not

#Loical And :Both expressions have to be true for the result to be true else false.
#Example
a,b= 5,6
c=True
print(a>4 and b<10) #Both conditions are true so it will print TRUE as output

#Logical Or :Either of the expressions has to be true  so as for the condition to be true but of both conditions are  false
#then Expression will be false.
#Example
print (a>4 or b<2)
#logical Not : Will give the opposite of the output. if true it will return false and the reverse is true
#Example
print(not c)
#Bitwise Operators: these are operators that work on binary numbers

#Bitwise And &: if both bits are 1 then the expression with return 1 else it will return 0
#example
print(a & b) #binary 5 is 0101 binary 6 is 0110

#bitwise or |: if both bits are 0 the expression will return 0 else if any bit is 1 the
#expression will return 1
#Example
print(a | b ) # binary 5 is 0101 binary 6 is 0110

#Bitwise Xor ^ if both bits are the same the expression will return 0 else if they are different
#expressio will return 1

#Example
print (a^b) #binary 5 is 0101 binary 6 is 0110

#Bitwise not (Compliment ~): Bits are converted to 1s complement then 2s compliment.
#Original Bit minus the 2s complement. Bitwise not is used to store negative numbers
print(~a)

#left shift Operators <<: Shifts bits to the left by n number and adds 0s in the places where the bits
#shifted. can also be expressed as X*2n X times 2 to the power n. n being the bits to shift and X being the
# Variable
#example
print(a<<2)

#right Shift Operator >>: looses bits to the right hand side and replaces them with the bits before.
#the shifted bits are replaced by 0s.can also be expressed as X/2n n being the bits to shift and X
#being the variable
#Example
print (a>>2)

#identity operators: these operators compare objects to their memory addresses. if the objects are the same
#same memory is shared. if different then memory address will be different.
#Example is
print(a is b) #will return false because dont share the same memory address.
print(id(a)) #memory ID is different
print (id(b)) #memory ID is different.
print(a is not b) #will return true since the memory ID for a is not the same with that of B


d=5
d=8
print (id(d))
print (d is d)

#Membership Operator:
