#Conditional statements are those that control the  flow of executions in a program.
#Conditional Statements are in 3 categories
#1 Conditional Control Statements which include if if-esle if-elif and nested if
#2 Branching Statements include pass return break continue
#3 Looping Statements include while and for

#conditional control
#IF statement
#has only one condition that needs to be met
#Example
a=4
if a<=3:
    print('wrong')

    #IF Else Statement: if else statement must meet two conditions.  First condition is true
  #  program should execute ELse condition is wrong program Terminates.

height=int (input("ENTER YOUR HEIGHT IN METERS:"))
if height>3:
      print('TALL')
else:
      print('TOO SHORT')

#Exercise 6 Request Data from user to check if number is even or odd
Number_checker=int (input('Enter Number Here:'))
if Number_checker %2==0:
    print('Even Number')
else:
    print('Odd Number')