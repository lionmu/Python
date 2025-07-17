from sidework import total_bill

age_under_12=150
age_between_12_to_18=250
age_18_and_above=500
photo_bill=50


print('WELCOME TO CRUSTY CRUB JOY RIDE')
height=int(input('PLEASE ENTER YOUR HEIGHT IN METERS:'))
if height>=3:
    print('PLEASE PROCEED WITH ENTERING YOUR AGE')
    age=int(input('ENTER YOUR AGE:'))
    if age<=12:
        print('PAY 150 RUPEES')
        photo_input=input('DO YOU WANT TO TAKE A PHOTO:').lower()
        if photo_input=='yes':
            billed_amount=photo_bill+age_under_12
            print(f'{billed_amount}rs WILL BE YOUR TOTAL BILL')
        else:
            print('PLEASE PROCEED AND ENJOY YOUR RIDE')

    elif age <=18:
        print('PAY 250 RUPEES')
        photo_input=input('DO YOU WANT TO TAKE A PHOTO:').lower()
        if photo_input=='yes':
            billed_amount=photo_bill+age_18_and_above
            print(f'{billed_amount}rs WILL BE YOUR TOTAL BILL')
        else:
              print('PLEASE PROCEED AND ENJOY THE RIDE')

    else:
           print('PAY 500 RUPEES')
           photo_input=input('DO YOU WANT TO TAKE A PHOTO:').lower()
           if photo_input=='yes':
              billed_amount = photo_bill + age_18_and_above
              print (f'{billed_amount} WILL BE YOUR TOTAL FARE')
           else:
              print('PLEASE PROCEED AND ENJOY THE RIDE')

else:
 print('YOU ARE NOT QUALIFIED TO RIDE PLEASE COME AGAIN')
 print('BYE AND COME AGAIN NEXT TIME')