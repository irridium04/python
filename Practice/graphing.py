import matplotlib as mpl
import sys
import pandas as pd
from matplotlib import pyplot as plt



def main():
    example1()


def example1():
    majors = ["Math", "English", "Chemistry", "Computer Science", "Business"]

    students =[10,25,20,50,5]

    majorDataSet = list(zip(majors, students))


    df = pd.DataFrame(majorDataSet, columns = ["Majors", "Students"])

    si = df.sort_values(["Majors"])


    si = df.sort_values(["Students"])


    mindf = df["Students"].min()
    maxdf = df["Students"].max()
    meandf = df["Students"].mean()
    meddf = df["Students"].median()
    stddf = df["Students"].std()


    print(f"""
    Min: {round(mindf, 2)}
    Max: {round(maxdf, 2)}
    Mean: {round(meandf, 2)}
    Median: {round(meddf, 2)}
    Standard Deviation: {round(stddf, 2)}
    """)


    # plt.xlabel("Major")
    # plt.ylabel("Average Class Size")
    plt.title("Average Class Sizes For Given Majors")
    plt.ylim(0, maxdf * 1.1)
    
    # plt.bar(df["Majors"], df["Students"])
    # plt.show()

    # plt.plot(df["Majors"], df["Students"])
    # plt.show()

    # plt.pie(df["Students"], labels=df["Majors"], autopct = "")
    # plt.show()

    explode = (.1, .1, .1, .1, .1)

    plt.pie(df["Students"], explode = explode, labels=df["Majors"], autopct="%1.2f%%")
    
    plt.legend(df["Majors"], loc = "lower right")
    plt.show()
    
main()


