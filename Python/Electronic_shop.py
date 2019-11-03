#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    answer = -1;
    for key in keyboards:
        for driv in drives:
            tot_sum = key + driv;
            if tot_sum <= b:
                answer = max(answer,tot_sum);
    return answer;            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = raw_input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = map(int, raw_input().rstrip().split())

    drives = map(int, raw_input().rstrip().split())

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

