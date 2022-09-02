import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from DAFunction import dfAllTests, engagedStudents

# ===== EXCLUSIVELY FOR PYCHARM, PLEASE IGNORE =====
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# ==================================================


# Copying as dataframe and storing into variable
dfTests = dfAllTests().copy()
dfTests.sort_values('sum_test_grade', ascending=True, inplace=True)

# I test with the dataframe that excludes disengaged students, a function
# which I created in DAFunctions

# # checking df for rows which contains NA values in its columns, = the candidate not taking the test
# print(dfTests[dfTests.isna().any(axis=1)])

# # checking number null values of each row
# print(dfTests.isnull().sum(axis=1))


def getPerformance(df):
    """ Returns the performance of each student
    and adds the column to the dataframe """
    performance = df.iloc[:, 1:7].mean(axis=1).round(2)
    df['performance'] = performance
    add_performance = df
    # print(add_performance)
    return add_performance

def getUnderperformers(df):
    """ Returns the dataframe of underperforming students.
    My criteria is the average of the total grade,
    inclusive of mock test with results of 50 and below"""
    min_formative = df.iloc[:,1:8].min(axis = 1)
    df['lowest_formative_grade'] = min_formative
    underperformers = df[df['performance'] <= 50]
    print(underperformers)
    return underperformers

def underperformViz(df):
    """ Bar chart visualisation for the given dataframe"""
    # df_trans = df.T
    bar = df.plot(x='research_id', kind='bar')
    plt.title('Underperforming Students')
    plt.xlabel('Student ID')
    plt.ylabel('Grades')
    plt.yticks(rotation=None)
    plt.xticks(rotation=360)
    plt.legend(['Mock Test',
                'Test 1',
                'Test 2',
                'Test 3',
                'Test 4',
                'Summative Test',
                'Overall Performance'])
    plt.show()

# calling the function within the file for testing.
if __name__ == "__main__":
    dfEngagedStudents = engagedStudents(dfTests)
    dfWithPerformance = getPerformance(dfEngagedStudents)
    dfUnderperfomers = getUnderperformers(dfWithPerformance)
    underperformViz(dfUnderperfomers)

