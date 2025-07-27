#A random module is a predfined module that helps with running pseudo algorithm i.e it helps in running 
#random algorithms for a program
#in order to use the random module it has to be imported
#syntax import random

import random
#randomization functions
#randint. will return a random integer between 1 and 3
a=random.randint (1,3)
print (a)

#randrange will print a number between the range of 1 and 3 but not 3
a=random.randrange (1,3)
print (a)
#random.random
#prints floating number between 0 and 1.0
a=random.random()
print (a)
#random.uniform prints random floating numbers basing on the range given but not 3
a=random.uniform(1,3)
print (a)
#random.choice prints a random element from  a list dictionnary etc
a=[10,20,30,40,50,-6,-10.4]
a=random.choice (a)
print (a)

#ramdom.shuffle will shuffle all the elements in the set ,tuple etc
a=[10,20,30,40,50,-6,-10.4]
random.shuffle(a)
print (a)
#
random.sample(a)
print (a)
