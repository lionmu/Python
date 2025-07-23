#Create a program that books pizza
#small Pizza=100Rs Medium Pizza=200Rs Large Pizza=300Rs 
#Pepperoni for small Pizza=30
#Pepperoni for medium and large pizza=50
#Extra cheese for any pizza size=20
price_pepperoni_small=30
price_pizza_small=100
extra_cheese=20
price_pizza_medium=200
price_pizza_Large=300
price_pepperoni_medium_and_large=50



print('*******WELCOME TO PIZZA HUT CORNER***************')
print('PLEASE CHOOSE THE SIZE OF PIZZA')
print('OPTION 1 FOR SMALL PIZZA')
print('OPTION 2 FOR MEDIUM PIZZA')
print('OPTION 1 FOR LARGE PIZZA')
choice=input('PLEASE CHOOSE YOUR OPTION:')
#CHOICE OPTION 1
if choice =='1':
    print(f'YOUR PIZZA WILL COST {price_pizza_small} Rs')
    pepperoni_for_small=input('DO YOU REQUIRE PEPPERONI:')
    if pepperoni_for_small=='yes':
        print(f'AN EXTRA OF {price_pepperoni_small} Rs')
        total_cost=price_pepperoni_small+price_pizza_small
        print(f'AND YOUR TOTAL COST WILL BE {total_cost}Rs')
    else:
         print(f'YOUR BILL WILL BE {price_pizza_small}Rs')

    request_cheese=input('DO YOU NEED EXTRA CHEESE:') 
    if request_cheese=='yes':
        print(f'AN EXTRA OF {extra_cheese} Rs')    
        total_cost=extra_cheese+price_pizza_small
        print(f'AND YOUR TOTAL COST WILL BE {total_cost}Rs')
    else:
        print(f'YOUR BILL WILL BE {price_pizza_small}Rs')
#CHOICE OPTION 2
elif choice=='2':
    print(f'YOUR PIZZA WILL COST {price_pizza_medium}Rs')

    pepperoni_for_medium=input('DO YOU REQUIRE PEPPERONI:')
    if pepperoni_for_medium=='yes':
        print(f'AN EXTRA OF {price_pepperoni_medium_and_large} Rs')
        total_cost=price_pepperoni_medium_and_large+price_pizza_medium
        print(f'AND YOUR TOTAL COST WILL BE {total_cost}Rs')
    else:
         print(f'YOUR BILL WILL BE {price_pizza_medium}Rs')

         request_cheese=input('DO YOU NEED EXTRA CHEESE:') 
    if request_cheese=='yes':
        print(f'AN EXTRA OF {extra_cheese} Rs')    
        total_cost=extra_cheese+price_pizza_medium

        print(f'AND YOUR TOTAL COST WILL BE {total_cost}Rs')
    else:
        print(f'YOUR BILL WILL BE {price_pizza_medium}Rs')
#CHOICE OPTION 3
elif choice=='3':
    print(f'YOUR PIZZA WILL COST {price_pizza_Large}Rs')
    pepperoni_for_large=input('DO YOU REQUIRE PEPPERONI:')
    if pepperoni_for_large=='yes':
     print(f'AN EXTRA OF {price_pepperoni_medium_and_large} Rs')
     total_cost=price_pepperoni_medium_and_large+price_pizza_Large
     print(f'AND YOUR TOTAL COST WILL BE {total_cost}Rs')
    else:
     print(f'YOUR BILL WILL BE {price_pizza_Large}Rs')

     request_cheese=input('DO YOU NEED EXTRA CHEESE:') 
    if request_cheese=='yes':
        print(f'AN EXTRA OF {extra_cheese} Rs')    
        total_cost=extra_cheese+price_pizza_Large

        print(f'AND YOUR TOTAL COST WILL BE {total_cost}Rs')
    else:
        print(f'YOUR BILL WILL BE {price_pizza_Large}Rs')

else:
    print('THANK YOU AND COME AGAIN')