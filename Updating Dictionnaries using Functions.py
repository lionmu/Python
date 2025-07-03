def adding_family_member(my_family,role,name):
    my_family[role]=name 
 
my_family={'Fathers_Name':'Lionel Ssengooba Musoke'}
print(my_family)
#defining function called addin_family_member with add_member as a place holder, roll as the key and name as the value
my_family.update({'Mother_name':'Nabisere Maria'})
print(my_family)


    
adding_family_member(my_family,'Daughter4','Michel')
adding_family_member(my_family,'Daughter5','Hudais')
print (my_family)
#my_family.popitem()
#print (my_family)
    