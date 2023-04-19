# Collin Shook
# Pandas


import numpy as np
import matplotlib as mpl
import sys
import pandas as pd
from matplotlib import pyplot as plt


temps = [24,27,36,44,53,59,66,65,55,43,32,24]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']



tempDataSet = list(zip(temps, months))
def main():
    Part1()
    Part2()



def Part1():
    df = pd.DataFrame(tempDataSet, columns=["Temperatures", "Months"])

    maxTemp = df["Temperatures"].max()
    minTemp = df["Temperatures"].min()
    meanTemp = df["Temperatures"].mean()

    print(f"""
Max Temp: {maxTemp}
Min Temp: {minTemp}
Mean Temp: {meanTemp}
    """)

    plt.xlabel("Months")
    plt.ylabel("Temperature (F)")
    plt.title("Average Temperature Per Month in Kalispell, MT")
    plt.ylim(0, maxTemp * 1.1)

    plt.bar(df["Months"], df["Temperatures"])
    plt.show()

def Part2():
    arr = np.array([[31, 36, 46, 57, 66, 73, 82, 81, 70, 55, 40, 30],
                    [24, 27, 36, 44, 53, 59, 66, 65, 55, 43, 32, 24],
                    [19, 21, 28, 34, 41, 47, 51, 49, 42, 33, 26, 19]])

    df = pd.DataFrame(arr, index=["High Temp", "Median Temp", "Low Temp"], columns= months)

    print(df.loc[:, ['Jan', 'Feb', 'Mar']])
    print(df.loc[:, ['Oct', 'Nov', 'Dec']])
    
    print(df.tail(3))

    print(df.loc["Low Temp"])

    print(df.transpose())

    for r in range(df.index.size):
        for c in range(df.columns.size):
            sys.stdout.write(str(df.iloc[r][c]) + " ")
        print()

    df = df.T
    df.plot(kind='line')

    plt.xlabel('Months')
    plt.ylabel('Temperature (F)')
    plt.title(label='High, Low, and Median Temperatures in Kalispell, MT', loc='center')
   
    plt.show()
main()