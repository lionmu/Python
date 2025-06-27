#A dictionary is a mapped collection and Data is Organised in Key value pairs
#A key in dictionary cannot be dublicated but can have more than one value
#represented by curly braces {} key and value separated by : 
#Syntax dictionary name ={'Keyname:'value','keyname':'value' ,'keyname':'value'}
#example
my_family={'Father_Name':'Lionel Musoke Ssengooba'
           ,'Mothers_Name':'Nabisere Maria'
           ,'Daughter1 Name':'Michaela hava',
           'Daughter2 Name':'Namagembe Heidi'}
print (my_family)
#reading a single element from the dictionary specify the element using [] braces
print(my_family['Father_Name'])
#Reading using the for loop for i in dictionary name print i  
#for name  in my_family:
#print(name)
 
 #using the update operation for modifying the dictionary should be placed ({'updated key':'value'})
my_family.update({'Daughter3':'Hudais'})
print(my_family)

#deletion operations
#using Del()
del my_family['Daughter3']
print(my_family)

#using popitem(). A dictionary operates on LIFO basis so the last item to come in will be popped first
# and can be used in stack mode.
my_family.popitem()
print(my_family)
#created a variable called A that will store the value that has been popped then output it.
a=my_family.popitem()
print(a)
#using the Clear() deletes all the elements in the dictionary leaving it empty {}
my_family.clear()
print(my_family)

#updating Dictionary using functions
#insert_item Function

