
#Create a simple Python program that manages student data in a file. The program should allow the following operations: 
#Add a student: The user should be able to add a new student's information (roll number, name, and grade) to the file students.txt. 
# The data should be appended to the file.
#  Delete a student:
#  The user should be able to delete a student from the file by entering the student's roll number. 
# The program should search for the roll number in the file and remove that student's record. 
#Exit: The program should allow the user to exit the program.

print("***********************WELCOME TO OUR CHESTAMORE UNVERSITY STUDENT PORTAL*********************************"  ,sep="\n")
print("PLEASE PRESSE ENTER YOUR STUDENT DETAILS")
Roll_number=(input("Enter Roll Number:"))
Grade=(input("Enter Grade:"))
Name=(input("Enter Student Name:"))


print("Student Name:",Name)
print("Student Roll Number:",Roll_number)
print("Student Grade:" ,Grade)

#creating the file called student.text file creating it in append mode so that new entry will be written at the end. Data entered should save automatically in the student.txt
open('student.txt', 'a')

#student.txt created in the default folder next command is to store the details received  from the variables having the fil. the input will be written.

with open('student.txt', 'a') as file:
    file.write(f"Name: {Roll_number}, Roll: {Grade}, Grade: {Name}\n")

print("THE STUDENT HAS BEEN ADDED SUCCESSFULLY TO THE DATABASE")


