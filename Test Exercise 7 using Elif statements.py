#Exercise 7: Calculate the BMI for a person and specify where they fall that is Normal Over weight UNder weigh
#obese

print("Measure your BMI here")
Weight=float(input('Enter your Weight in Kgs:'))
Height=float (input("Enter your Height in Meters:"))
BMI=round(Weight/Height ** 2)
#print('YOUR BMI IS', BMI)


if 18.5<=BMI<=24.9:
      print(f'YOUR BMI IS {BMI} AND YOU ARE NORMAL')
elif 16.0 <= BMI <= 16.9: #if you want to look for values within a range use Variable should in between the operators.
      print(f'YOUR BMI IS {BMI} AND YOU ARE MODERATELY THIN')
elif  17.0<= BMI <=18.4:
      print(f'YOUR BMI IS {BMI} AND YOU ARE MILDLY THIN')
elif BMI<=16.0:
      print(f'YOUR BMI IS {BMI} AND YOU ARE SEVERELY THIN')
elif 25.0<=BMI<=29.9:
      print(f'YOUR BMI IS {BMI} AND YOU ARE OVER WEIGHT')
elif 30.0<=BMI<=29.0:
      print(f'YOUR BMI IS {BMI} AND YOU ARE OBESE CLASS ONE')
elif 35.0<=BMI<=39.9:
       print(f'YOUR BMI IS {BMI} AND YOU ARE OBESE CLASS TWO')
else:
       print(f'YOUR NEED TO SEE A DOCTOR AS YOUR BODY MASS INDEX IS {BMI} WHICH IS  ABNORMAL')

       print(f'IF YOUR BODY MASS INDEX IS  MORE THAT 30 YOU ARE NOT HEALTHY. VISIT THE MEDICAL FACILITY')

       print('THANK YOU')