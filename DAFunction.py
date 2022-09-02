import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

def dfAllTests():
    """This returns dataframes from the database
    of each test with NA values that indicates
    the student did not attempt the test """
    connection = sql.connect('ResultDatabase.db')
    dfMockTest = pd.read_sql('SELECT research_id, grade FROM FormativeMockTest', connection)
    dfTest1 = pd.read_sql('SELECT research_id, grade FROM FormativeTest1', connection)
    dfTest2 = pd.read_sql('SELECT research_id, grade FROM FormativeTest2', connection)
    dfTest3 = pd.read_sql('SELECT research_id, grade FROM FormativeTest3', connection)
    dfTest4 = pd.read_sql('SELECT research_id, grade FROM FormativeTest4', connection)
    dfSumTest = pd.read_sql('SELECT research_id, grade FROM SummativeTest', connection)

    connection.close()

    dfMockTest.rename(columns={'grade': 'mock_test_grade'}, inplace=True)
    dfTest1.rename(columns={'grade': 'test1_grade'}, inplace=True)
    dfTest2.rename(columns={'grade': 'test2_grade'}, inplace=True)
    dfTest3.rename(columns={'grade': 'test3_grade'}, inplace=True)
    dfTest4.rename(columns={'grade': 'test4_grade'}, inplace=True)
    dfSumTest.rename(columns={'grade': 'sum_test_grade'}, inplace=True)

    dfAllTests = pd.merge(dfMockTest, dfTest1, on='research_id', how='outer')
    dfAllTests = pd.merge(dfAllTests, dfTest2, on='research_id', how='outer')
    dfAllTests = pd.merge(dfAllTests, dfTest3, on='research_id', how='outer')
    dfAllTests = pd.merge(dfAllTests, dfTest4, on='research_id', how='outer')
    dfAllTests = pd.merge(dfAllTests, dfSumTest, on='research_id', how='outer')

    return dfAllTests

def engagedStudents(df):
    """filters and removes the disenagged students with the criteria
    of more than 3 no attempts on formative tests including the mock """
    df['no_attempts'] = df.iloc[:, 1:7].isnull().sum(axis=1)
    disengaged = df[df['no_attempts'] >= 3].index
    drop_disengaged = df.drop(disengaged)
    index_disenagaged = drop_disengaged.reset_index()
    drop_cols = index_disenagaged.drop(['index', 'no_attempts'], axis=1)
    engaged = drop_cols
    # print(engaged)
    return engaged