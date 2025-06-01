#input Function input()

#a=input("Enter the Value of A:")
#print ("The Value of A IS:" , a)
#print("And its of: " ,type (a))

#number_A=input("ENter Number A:")
#number_B=input("ENter Number B:")
#sum=number_A+number_B
#print("The Numbers were:", number_A , number_B)
#print ("And the Answer will be ",sum)

#Type Conversion or Type Casting:  Converting from one data type to another
#Syntax 1:   int(value)----converts a float to an integer
#a=12.54
#b=int(a)
#print (a,b ,type(a),type(b))
#a=int (True) #binary representation of true is 1
#b=int (False) # binary representation of false is 0
#print(a,b, type(a),type(b))

#syntax 2 int(value,base=10) THis one is used when converting a string in different bases to base 10
#Bases go from 2-36 (from base 10 should start with A 10 B 11 till Z 35)
#pefixes like "0x" for hex or "0b" for binary are NOT allowed when specifying base
#a=int("0b1010" ,2)
#print(a)
#hex_number=input("Enter Hex number:")
#binary_number=int(hex_number ,16)
#print("The conversion to base 16 is" ,binary_number)

#float() converts int, bool, string to float
#syntax float()
#a=23
#c=True
#d=float(c)
#b=float(a)
#print(d,b ,type(b),type(d))

#complex used to convert bool int float string to complex format
#syntax 1 complex(real=0 ,imag=0)
#complex (value)

#syntax 1 complex(value) having user input
#a=complex (input("Enter Complex NUmber:"))
#b=complex(1)
#c=complex(True)
#print(a,b,c,sep="\n")
#print(type(a) ,type(b) ,type(c))

#syntax 2 complex(real=0 imag=0)
#d=complex (real=1, imag=2)
#print (d,type(d))

#boolean bool() converts int, float,boolean to boolean
#a=bool(True)
#b=bool(False)
#c=bool(1)
#d=bool(0)
#rint (a,b,c,d, type(a),type(b),type(c),type(d),sep="\n")

#string str() converts other data types to string
#a=str(65)
#b=str(1.5)
#c=str(1+2j)
#d=str("LONE RANGER")

#print (a,b,c,d,type(a),type(b),type(c),type(d),sep=":" "\n")

#Relational operators Aka known as ternary operators used to evaluate expression basing on conditions
# < less than
# > greater than
#  >= greater than or equal to
# <= less than or equal to
#  == equal or equal to
#  =! not equal to
#syntax comparing two conditions
#a=int(input("Enter Number 1:"))
#b=int(input("Enter NUmber 2:"))
#print( "Greater than")if a>b else print("Less Than")

#c=int(input("Enter NUmber 3:"))
#d=int(input("Enter Number 4:"))
#print("Equal to") if c==d else print("Not Equal")

#e=int(input("Enter Number 5:"))
#print("odd")if e%5==0 else print("even")

#logical operators these are used to combine boolean expressions
#and all boolean expressions have to be true so as the result to be true else false
#or one of the boolean expressions have to be true as the result to be true else false
#not is the opposite of the boolean expression


#a=int(input("Enter Roll Number:"))
#b=input("Enter Name:")
#c=int(input("Enter Marks for Course A:"))
#d=int(input("Enter MArks for Course B:"))
#print("Passed Exam" ,sep="\n")if c>=50 and d>=50 else print("Failed Exam")

#a=int(input("Enter Roll Number:"))
#b=input("Enter Name:")
#c=int(input("Enter Marks for Course A:"))
#d=int(input("Enter MArks for Course B:"))
#print("Passed Exam" ,sep="\n")if c>=50 or d>=50 else print("Failed Exam")

#a=int(input("Enter Roll Number:"))
#b=input("Enter Name:")
#c=int(input("Enter Marks for Course A:"))
#d=int(input("Enter MArks for Course B:"))
#print("Passed Exam" ,sep="\n")if c>=50 and not d>=50 else print("Failed Exam")

# Bitwise OPerators THese are used to convert Data into 0s and 1s
#types of bit operators

#>> Right Shift operator shifts bits to the right filling the left hand side with 0s (for positive integers)
#syntax
#a=10
#b=a>>2
#print(b)
#10 in binary is 1010 discard the last two bits and replace with 0 outout will be 10  00 which is 2 in binary
#a>>2 is the same as a//2n where n is the shift amount

#<<Left Shift operator shifts bits to the left side filing the right hand side with 0s
#a=10
#b=a<<3
#print(b)
#10 in binary is 1010 shift all the bits to the left by adding 3 0s as the shift is 3 which will becomw 1010 000
#a<<3 is the same as a*2n where n is the shift amount
#which is binary 80
#& bitwise and operator: the and operator returns the first falsy value if one exists, otherwise it returns the last truthy value.
#a=20
#b=30
#c=a and b
#print (a,b,c)
#print (bin(a),bin(b),bin(c),sep=":") will print the values in binary
#^ logical or and
#~
