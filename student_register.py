'''This programme allows the user to register students for an exam venue,
by enetering their name and ID numbers.
This program also runs to create a sperate text file that dtore the student ID numbers,
and a dotted line space to sign.'''
# The lines below are my pseudocode:
# Diplay open line explaining required info/use.
# Input interger line asking user to eneter the number of students registering.
# While loop to run according to the entered number with the following commands:
    # Open a new text file creation with writing access mode.
    # Ask user to enter student number.
    # write each enetered entry into the created text file and a dotted line below for each.


print("Complete this sheet for exam venue student registartions by entering the requseted details.")
total_number = input("Enter the total number of students registering: \n")
total_number = int(total_number)
i = 1

while i <= total_number:
    student_id = input("Enter ID number for student:\n")
    i += 1
    with open('reg_form.txt', 'a+') as txt_file:
        txt_file.write("\n" + student_id + "\n" + "........................")
print("Thank you for registering, please see attached (reg_form) for registered student details and signing.")