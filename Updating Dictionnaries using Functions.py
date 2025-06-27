my_family={'Fathers_Name':'Lionel Ssengooba Musoke'}
print(my_family)
#defining function called addin_family_member with add_member as a place holder, roll as the key and name as the value
def adding_family_member(add_member,role,name):
    add_member[role]=name
    print(f"Added {'name'}")
    
    adding_family_member(my_family,'Daughter4','Michel')
    print (my_family)
    