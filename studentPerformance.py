import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from testResults import dfTestResults, getStudentTestResults

# getting individual df for each test with absolute values
connection = sql.connect('ResultDatabase.db')
dfMockTestAbs = pd.read_sql(
    'SELECT research_id, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10 FROM FormativeMockTest',
    connection)
dfTest1Abs = pd.read_sql(
    'SELECT research_id, q_1, q_2, q_3, q_4, q_5, q_6 FROM FormativeTest1',
    connection)
dfTest2Abs = pd.read_sql(
    'SELECT research_id, q_1, q_2, q_3, q_4, q_5, q_6 FROM FormativeTest2',
    connection)
dfTest3Abs = pd.read_sql(
    'SELECT research_id, q_1, q_2, q_3, q_4, q_5, q_6 FROM FormativeTest3',
    connection)
dfTest4Abs = pd.read_sql(
    'SELECT research_id, q_1, q_2 FROM FormativeTest4',
    connection)
dfSumTestAbs = pd.read_sql(
    'SELECT research_id, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10, q_11, q_12, q_13 FROM SummativeTest',
    connection)

connection.close()

# creating a dataframe with relative values
dfMockTestRel = dfMockTestAbs.copy(deep=True)
dfMockTestRel.iloc[:, 1:] = dfMockTestRel.iloc[:, 1:].apply(
    lambda row: row - row.mean().round(2))

dfTest1Rel = dfTest1Abs.copy(deep=True)
dfTest1Rel.iloc[0:, 1:] = dfTest1Rel.iloc[0:, 1:].apply(
    lambda row: row - row.mean().round(2))

dfTest2Rel = dfTest2Abs.copy(deep=True)
dfTest2Rel.iloc[:, 1:] = dfTest2Rel.iloc[:, 1:].apply(
    lambda row: row - row.mean().round(2))

dfTest3Rel = dfTest3Abs.copy(deep=True)
dfTest3Rel.iloc[:, 1:] = dfTest3Rel.iloc[:, 1:].apply(
    lambda row: row - row.mean().round(2))

dfTest4Rel = dfTest4Abs.copy(deep=True)
dfTest4Rel.iloc[:, 1:] = dfTest4Rel.iloc[:, 1:].apply(
    lambda row: row - row.mean().round(2))

dfSumTestRel = dfSumTestAbs.copy(deep=True)
dfSumTestRel.iloc[:, 1:] = dfSumTestRel.iloc[:, 1:].apply(
    lambda row: row - row.mean().round(2))


def dfAbsolute(test):
    """ Returns the absolute performance dataframe for the given test number. """
    if test == 0:
        test = dfMockTestAbs
        return dfMockTestAbs
    elif test == 1:
        test = dfTest1Abs
        return dfTest1Abs
    elif test == 2:
        test = dfTest2Abs
        return dfTest2Abs
    elif test == 3:
        test = dfTest3Abs
        return dfTest3Abs
    elif test == 4:
        test = dfTest4Abs
        return dfTest4Abs
    elif test == 5:
        test = dfSumTestAbs
        return dfSumTestAbs
    else:
        print('Please try again, input 0 - 6 to select the test')

def dfRelative(test):
    """ Returns the relative performance dataframe for the given test number. """
    if test == 0:
        test = dfMockTestRel
        return dfMockTestRel
    elif test == 1:
        test = dfTest1Rel
        return dfTest1Rel
    elif test == 2:
        test = dfTest2Rel
        return dfTest2Rel
    elif test == 3:
        test = dfTest3Rel
        return dfTest3Rel
    elif test == 4:
        test = dfTest4Rel
        return dfTest4Rel
    elif test == 5:
        test = dfSumTestRel
        return dfSumTestRel
    else:
        print('Please try again, input 0 - 6 to select the test')


def getStudentPerformance(student_id, test):
    """ Returns absolute and relative performance dataframes for
    the given student id and the """
    if student_id in dfAbsolute(test).iloc[:, 0] and student_id in dfRelative(test).iloc[:, 0]:
        resultsAbs = dfAbsolute(test).loc[dfAbsolute(test)['research_id'] == student_id]
        resultsRel = dfRelative(test).loc[dfRelative(test)['research_id'] == student_id]
        print("Absolute Performance")
        print(resultsAbs)
        print("Relative Performance")
        print(resultsRel)

        return resultsAbs, resultsRel

# The code below was an attempt to handle given test that do not exist in the dataframes
    # else:
    #     test not in dfAbsolute(test) and test not in dfRelative(test)
    #     print('The student did not attempt this test')

def studentPerformanceViz(df1, df2):
    """ Produces stacked bar chart visualisation of the 2 dataframes"""
    df1 = df1.drop(df1.columns[0], axis=1)
    df2 = df2.drop(df2.columns[0], axis=1)
    df1_trans = df1.T
    df2_trans = df2.T
    abs = df1_trans.plot(kind='bar', color='#B70062')
    df2_trans.plot(kind='bar', ax=abs, color='#330066')
    plt.title("Absolute vs. Relative Performance")
    plt.ylabel("Marks")
    plt.xlabel("Questions")
    plt.yticks(rotation=None)
    plt.xticks(rotation=360)
    plt.legend(['Absolute', 'Relative'])

    plt.show()


# calling the function within the file for testing.
if __name__ == "__main__":
    student_id = int(input(('Please enter student id: ')))
    test = int(input("0 - Mock Test\n1 - Test 1\n2 - Test 2\n3 - Test 3\n4 - Test 4\n5 - Summative Test\n"
                     "Please enter a number to choose a test: "))
    df1, df2 = getStudentPerformance(student_id, test)
    studentPerformanceViz(df1, df2)