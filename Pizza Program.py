print('WELCOME TO THE PIZZA HUT RESTAURANT')
print('**************PLEASE SELECT FROM OUR MENU*****************')
print('OPTION 1 SMALL SIZE PIZZA AT 100Rs')
print('OPTION 2 MEDIUM PIZZA AT 200Rs ')
pepperoni_for_small_pizza = 30
peperoni_for_medium_or_large=50
small_size_pizza = 100
medium_pizza=200
extra_cheese=20
option = int(input('CHOOSE OPTION:'))

if option == 1:
    print('YOUR PIZZA WILL COST 100Rs')
    Pepperoni_small=input('DO YOU REQUIRE PEPPERONI:').lower()
    if Pepperoni_small =='yes':
       print('YOU WILL BE CHARGED AN EXTRA 30Rs')
       total_cost=pepperoni_for_small_pizza+small_size_pizza
       print(f'AND YOUR TOTAL BILL WILL BE {total_cost} Rs')
       addition_cheese=input('DO YOU WANT EXTRA CHEESE').lower()
    if extra_cheese=='yes':
        print('EXTRA CHEESE WILL COST 20Rs')
        total_cost=medium_pizza
        print(f'PIZZA WILL COST{total_cost}')


else:
    print('THANK YOU')

