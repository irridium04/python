import numpy as np
import sys


def main():
    numpyDemo()


def numpyDemo():
    arr = np.array([[100,3434,344,577],[4545,323123,2331,2343],[233,6653,545435,124]])
    
    rows = 3
    cols = 4


    for row in range(rows):
        for col in range(cols):
            sys.stdout.write(str(arr[row, col]) + ' ')
        print()


    yy = arr[1,2]
    
    sum = 0
    for row in range(rows):
        for col in range(cols):
            sum += arr[row, col]
    
    print(sum)

    maxNum = arr[0,0]
    for row in range(rows):
        for col in range(cols):
            if(arr[row,col] > maxNum):
                maxNum = arr[row, col]

    print(maxNum)

main()




