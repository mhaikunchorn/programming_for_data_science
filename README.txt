Please find below instructions on how to run the code for the following files.

--------------------
menu.py
--------------------
> This is a command line interface, please run as normal and follow the
instructions as it appears in the command line.

> When choosing (s) Student's Performance, you may find when checking for
 students who did not participate in a chosen test e.g. Student ID 5, Test 2, you
 will encounter an error which I struggled to handle within the studentPerformance.py.
 Please refresh/rerun the menu.py again to start over and continue
 to check the rest of the programme.

> Some selected options from the Menu should produce graphs and dataframes
in the command line at the same time.

> I am most proud about being able to create this and have an option which allows
users to end the programme.

> FOR GUI:
Please follow the instructions on line 71 - 73 to comment and uncomment in order
to test the GUI I attempted to build.
Note currently only 'Underperforming Students' button yields a visualisation.

> I am happy I tried to build the GUI, although I ran out of time for integration,
This will be something I will practice for my portfolio projects.

--------------------
testResults.py
--------------------
> When prompted, student id would need to be entered in order to retrieve the dataframe
and the visualisation of the information.
I have chosen the bar chart for its readability and the choice of colour is to reflect
the university's iconic purple.

> I feel I was successful with the way exceptions were handled in this file.

--------------------
studentPerformance.py
--------------------
> The way I coded in this file made it very difficult for me to rectify and do
exception handling for when the input is in correct and also for when the input
of student id does not exist in the test meaning the student did not attempt the test.

> In the future I would try create a function that takes the student id as an input
which will validate whether the student id is present in the test name the user has given
and then plot the graph if the results yields True, if False it notifies the user that the
student id does not exist in the test.

> I found this question to be the most challenging of all.

--------------------
underperformingStudents.py
--------------------
> My criteria for underperforming students were their average overall grades including mock
that were 50 or less.

--------------------
hardworkingStudents.py
--------------------
> I also reused function which returns to me the engaged students which
I returned the hardworking students results based on self rate of below beginner / beginner
who scored more than 60 in their summative test.

--------------------
DAFunctions.py
--------------------
> My criteria for disengaged are those who did not do 3 or more formative tests including Formative Mock Test
