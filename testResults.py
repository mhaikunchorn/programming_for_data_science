import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

def dfTestResults():
    """ Returns a dataframe of research id and grades of each test """
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

    dfTestResults = pd.merge(dfMockTest, dfTest1, on='research_id', how='outer')
    dfTestResults = pd.merge(dfTestResults, dfTest2, on='research_id', how='outer')
    dfTestResults = pd.merge(dfTestResults, dfTest3, on='research_id', how='outer')
    dfTestResults = pd.merge(dfTestResults, dfTest4, on='research_id', how='outer')
    dfTestResults = pd.merge(dfTestResults, dfSumTest, on='research_id', how='outer')

    dfTestResults.fillna(0, inplace=True)

    return dfTestResults

def getStudentTestResults(student_id):
    """ Matches student id to the research id in the dataframe
    and returns df with test results of each test"""
    if student_id in dfTestResults().iloc[:,0]:
        results = dfTestResults().loc[dfTestResults()['research_id'] == student_id]
        print(results)

        return results

    else:
        print("Sorry, this student does not exist.")

def getViz(df):
    """ Produces a bar chart representing the results of each test
    including labels and annotations """
    try:
        df.drop('research_id', inplace=True, axis=1)
        df.columns = ['Formative Mock \n Test', 'Formative \n Test 1',
                  'Formative \n Test 2', 'Formative \n Test 3', 'Formative \n Test 4', 'Summative \n Test']
        df_trans = df.T
        df_trans.reset_index(inplace=True)
        # print(df_trans)
        bar = df_trans.plot(x='index',
                        kind='bar',
                        figsize=(10, 10),
                        color='#330066',
                        legend = None)
        plt.title("Student Test Results")
        plt.ylabel("Grade")
        plt.xlabel("Tests")
        plt.yticks(rotation=None)
        plt.xticks(rotation=360)
        plt.ylim(0, 105)
        plt.bar_label(bar.containers[0], size=10, fmt='%.2f')

        plt.show()

    except AttributeError:
        print("Try again.")

# calling the function within the file for testing.
if __name__ == "__main__":
    student_id = int(input('Please enter the student id number: '))
    results = getStudentTestResults(student_id)
    getViz(results)
