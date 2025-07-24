print('WELCOME TO THE PIZZA HUT RESTAURANT')
print('**************PLEASE SELECT FROM OUR MENU*****************')
print('OPTION 1 SMALL SIZE PIZZA')
print('OPTION 2 MEDIUM SIZE PIZZA')
print('OPTION 3 LARGE SIZE PIZZA')
option = int(input('CHOOSE OPTION:'))
intial_cost=0

if option == 1:
    intial_cost+=100
    print(f'YOUR PIZZA WILL COST {intial_cost}Rs')
    
elif option==2:
    intial_cost+=200
    print(f'PIZZA WILL COST{intial_cost}Rs')
    
else:
    intial_cost+=300
    print(f'PIZZA WILL COST {intial_cost}Rs')

additional_pepperoni=input('DO YOU WANR EXTRA PEPPERONI:').lower
if additional_pepperoni=='yes':
     if option==1:
      intial_cost+=30
    
else:
      intial_cost+=50
         
additional_cheese=input('DO YOU REQUIRE EXTRA CHEESE:').lower
if additional_cheese=='Yes':
     intial_cost+=20
          
print(f'YOUR TOTAL BILL WILL BE {intial_cost}Rs')  
print('THANK YOU')


