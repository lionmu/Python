

age_under_12=150
age_between_12_to_18=250
age_18_and_above=500
photo_bill=50

print('WELCOME TO CRUSTY KRUB JOY RIDE')
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
        elif photo_input=='no':                                     #when you use elif means you are having more than one condition YES AND NO
           print('PLEASE PROCEED WITH PAYMENT AND RIDE')

    elif age<=18:
        print('YOU ARE PAYING 200rs')      
        photo_input=input('DO YOU WANT TO TAKE A PHOTO:').lower ()
        if photo_input=='yes':
            billed_amount=age_between_12_to_18+photo_bill
            print(f'{billed_amount}rs WILL BE YOUR TOTAL BILL')
        else:#when using else means you want to use only one condition but i think by default it will cater for the other condition in this case its NO
            

            print('PLEASE PROCEED WITH YOUR RIDE')
    else:
        print('PAY 500Rs')
        photo_input=input('DO YOU WANT TO TAKE A PHOTO:').lower ()
        if photo_input=='yes':
            billed_amount=age_18_and_above+photo_bill
            print(f'{billed_amount}rs WILL BE YOUR TOTAL BILL')
        else:
            print('PLEASE PROCEED WITH YOUR RIDE')
else:
    print('YOU DONT MEET MATCH REQUIREMENTS')  
    print('YOU CANT BOARD THE RIDE') 

