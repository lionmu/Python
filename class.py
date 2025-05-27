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
a=str(65)
b=str(1.5)
c=str(1+2j)
d=str("LONE RANGER")

print (a,b,c,d,type(a),type(b),type(c),type(d),sep=":" "\n")
