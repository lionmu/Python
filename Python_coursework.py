
#Create a simple Python program that manages student data in a file. The program should allow the following operations: 
#Add a student: The user should be able to add a new student's information (roll number, name, and grade) to the file students.txt. 
# The data should be appended to the file.
#  Delete a student:
#  The user should be able to delete a student from the file by entering the student's roll number. 
# The program should search for the roll number in the file and remove that student's record. 
#Exit: The program should allow the user to exit the program.

print("***********************WELCOME TO OUR CHESTAMORE UNVERSITY STUDENT PORTAL*********************************"  ,sep="\n")
print("PLEASE PRESSE ENTER YOUR STUDENT DETAILS")
Roll_Number=(input("Enter Roll Number:"))
Course=(input("Enter Course:"))
Name=(input("Enter Student Name:"))


print("Student Name:",Name)
print("Student Roll Number:",Roll_Number)
print("Student Course:" ,Course)

#creating the file called student.text file creating it in append mode so that new entry will be written at the end. Data entered should save automatically in the student.txt
open('student.txt', 'a')

#student.txt created in the default folder next command is to store the details received  from the variables having the fil. the input will be written.

with open('student.txt', 'a') as file:
    file.write(f"Student_Roll_Number: {Roll_Number}, Student_Course {Course}, Student_Name: {Name}\n")
    #Displaying all students
print("\n--- STUDENT LIST ---")
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())
#Adding the Delete Function using the roll number.
print("DELETE RECORDS")
delete_choice=input("DO YOU WANT TO DELETE A RECORD? (yes/no)").lower()
if delete_choice == 'yes':
    deleting_roll = input("ENTER ROLL NUMBER TO DELETE: ")
   #Reading all records stored in studdent.text 
    with open("student.txt", "r") as file:
        student_records = file.readlines()
    
    with open("student.txt", "w") as file:
        for student in student_records:
            if not student.startswith(f"Student_Roll_Number: {deleting_roll},"):
                file.write(student)
    
    print(f"Roll Number {deleting_roll} Deleted Successfully!")

elif delete_choice == 'no':
    print("Goodbye!")
else:
    print("Invalid Input. Please Enter 'yes' or 'no'.")
