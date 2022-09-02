import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
from DAFunction import dfAllTests, engagedStudents


# read csv and clean names
dfStudentRates = pd.read_csv('DataFiles/StudentRate.csv')
dfStudentRates.drop(dfStudentRates.columns[1:3], axis=1, inplace=True)
dfStudentRates.drop(dfStudentRates.columns[2:], axis=1, inplace=True)
dfStudentRates.columns = ['research_id', 'self_rate']
# print(dfStudentRates)

# copying the dfAllTests into a df and ordering by descending summative grade
dfTests = dfAllTests().copy()
dfTests.sort_values('sum_test_grade', ascending=False, inplace=True)

# excluding disengaged students from this df
dfEngaged = engagedStudents(dfTests)
# print(dfEngaged)

# merging data from the dataframe onto the .csv file
mergedData = pd.merge(dfEngaged, dfStudentRates, on='research_id', how='inner')
# print(mergedData)

# viewing the df of students with specific self ratings
ratings = ['Below beginner', 'Beginner']
dfBeginnersAndBelow = mergedData[mergedData['self_rate'].isin(ratings)]
# print(dfBeginnersAndBelow)

def getHardworking(df):
    """ Returns the results of hardworking students"""
    hardworking = df[df['sum_test_grade'] >= 60]
    df_drop = hardworking.drop(hardworking.columns[[1, 2, 3, 4, 5]], axis=1)
    df_index = df_drop.reset_index().drop(['index'], axis=1)
    hardworkers = df_index
    # print(hardworkers)
    return hardworkers


# calling the function within the file for testing.
if __name__ == "__main__":
    dfHardworkers = getHardworking(dfBeginnersAndBelow)
    print(dfHardworkers)