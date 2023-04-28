print("Problem 02 ~ Assignment 4".center(42, "="))
print("\033[95m=" * 42)
print("\033[92mCMPE-103-MODULE-2-FILE-HANDLING-IN-PYTHON")
print("\033[95m=" * 42)

# write a python program that contains 20 students with their general weighted average, then, read the text file
# and create a program that will output the name of the student which have the highest gwa,
# including its grades in the output.

# pseudocode
# create a text file that contains names and gwa of 20 students
# open the text file and read it
with open("students_name_gwa.txt", "r") as problem_two_numbers_file:
# set the variables
     highest_general_weighted_average = 5.0
     name_student = ""
# construct the loop with related various methods
     for line in problem_two_numbers_file:
          student_gwa = line.strip().split(",")
     # recognize each line having two variables
       if len(student_gwa) !=2:
            continue
     # establish the two variables to one
       name, gwa = student_gwa
     # convert the gwa to float
       gwa = float(gwa)
# check the gwa line by line to get the highest gwa and its name of the student
# define the variables
# run the program
# print the output