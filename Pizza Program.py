print('WELCOME TO THE PIZZA HUT RESTAURANT')
print('**************PLEASE SELECT FROM OUR MENU*****************')
print('OPTION 1 SMALL SIZE PIZZA')
print('OPTION 2 MEDIUM SIZE PIZZA')
print('OPTION 3 LARGE SIZE PIZZA')
option = int(input('CHOOSE OPTION:'))

initial_cost=0

if option == 1:
    initial_cost+=100
    print(f'YOUR PIZZA WILL COST {initial_cost}Rs')
    
elif option==2:
    initial_cost+=200
    print(f'PIZZA WILL COST{initial_cost}Rs')

else:
    initial_cost+=300
    print(f'PIZZA WILL COST {initial_cost}Rs')

additional_pepperoni=input('EXTRA PEPPERONI (Y/N):')
if additional_pepperoni.lower()=='y':
 if option==1:
  initial_cost+=30
    
 else:
  initial_cost+=50
         
additional_cheese=input('EXTRA CHEESE (Y/N):')
if additional_cheese.lower()=='y':
 initial_cost+=20
          
print(f'YOUR TOTAL BILL WILL BE {initial_cost}Rs')
print('THANK YOU')

#else:
 #print('WRONG INPUT PLEASE TRY AGAIN')


