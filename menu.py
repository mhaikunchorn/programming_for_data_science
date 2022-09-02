import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from testResults import dfTestResults, getStudentTestResults, getViz
from studentPerformance import *
from underperformingStudents import *
from hardworkingStudents import *
from DAFunction import dfAllTests, engagedStudents

# ===== EXCLUSIVELY FOR PYCHARM, PLEASE IGNORE =====
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# ==================================================

def selectMenu():
    """ Menu Options """
    print("==================== Menu ====================")
    print("(t) Test Results")
    print("(s) Student's Performance")
    print("(u) Underperforming Students")
    print("(h) Hardworking Students")
    print("(x) Exit")
    print("\n")

# the code will execute according to user's input from the menu selection
# if user input is incorrect they will be prompted and allow to try again
# it will also end the session if user chooses to.
while True:
    selectMenu()
    option = input("Please select an option: ")
    if option == "t":
        print("\n==================== Test Results ====================\n")
        student_id = int(input('Please enter the student id number: '))
        results = getStudentTestResults(student_id)
        getViz(results)

    elif option == "s":
        print("\n==================== Student's Performance ====================\n")
        student_id = int(input(('Please enter student id: ')))
        test = int(input("0 - Mock Test\n"
                         "1 - Test 1\n"
                         "2 - Test 2\n"
                         "3 - Test 3\n"
                         "4 - Test 4\n"
                         "5 - Summative Test\n"
                         "Please select a test: "))
        df1, df2 = getStudentPerformance(student_id, test)
        studentPerformanceViz(df1, df2)

    elif option == "u":
        print("\n==================== Underperforming Students ====================\n")
        dfEngagedStudents = (engagedStudents(dfTests))
        dfWithPerformance = getPerformance(dfEngagedStudents)
        dfUnderperfomers = getUnderperformers(dfWithPerformance)
        underperformViz(dfUnderperfomers)

    elif option == "h":
        print("\n==================== Hardworking Students ====================\n")
        dfHardworkers = getHardworking(dfBeginnersAndBelow)
        print(dfHardworkers)

    elif option == "x":
        print("You have ended this session.")
        break

    else:
        print("That option does not exist, please try again.\n")


# ===================== TO VIEW GUI PLEASE COMMENT THE CODE ABOVE THIS LINE =====================

# ==================== TO VIEW GUI PLEASE UNCOMMENT THE CODE BELOW THIS LINE ====================
# from tkinter import *
# from hardworkingStudents import *
# from underperformingStudents import *
# from DAFunction import *

# from tkinter import ttk

# def underperformingButton():
#     dfEngagedStudents = (engagedStudents(dfTests))
#     dfWithPerformance = getPerformance(dfEngagedStudents)
#     dfUnderperfomers = getUnderperformers(dfWithPerformance)
#     underperformViz(dfUnderperfomers)
# def hardworkingButton():
#     dfHardworkers = getHardworking(dfBeginnersAndBelow)
#     print(dfHardworkers)

# # setting up the window
# window = Tk()
# window.title("Student Monitoring System")
# window.configure(background='white')
# window.geometry("750x500")

# # creating student id title
# student_id = Label(window,
#                    text="Student ID",
#                    background="white",
#                    font=("DIN Condensed", "20"))
# student_id.pack(pady = 10)


# # creating student id entry box
# student_id_no = IntVar()
# student_id_input = Entry(window, width=24, textvariable=student_id_no)
# # student_id_input.grid(row=1, column=1)
# student_id_input.pack(pady=10)


# #  buttons for different functions
# results_button = Button(window, text="Test\n Results",
#                         bg="black",
#                         fg="black",
#                         font="Helvetica 10 bold",
#                         command="")
# results_button.pack(pady=10)


# performance_button = Button(window, text="Student's\n Performance",
#                             bg="black",
#                             fg="black",
#                             font="Helvetica 10 bold",
#                             command="")
# performance_button.pack(pady=10)


# under_button = Button(window, text="Underperforming\n Students",
#                       bg="black",
#                       fg="black",
#                       font="Helvetica 10 bold",
#                       command=underperformingButton)
# under_button.pack(pady=10)


# hard_button = Button(window, text="Hardworking\n Students",
#                      bg="black",
#                      fg="black",
#                      font="Helvetica 10 bold",
#                      command=hardworkingButton())
# hard_button.pack(pady=10)

# # display the window
# window.mainloop()