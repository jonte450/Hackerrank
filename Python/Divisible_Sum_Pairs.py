#!/bin/python

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count_div = 0;
    for integer_1 in range(0,n):
        check_number = ar[integer_1];
        integer_2 = integer_1 + 1;
        while integer_2 < len(ar):
            sum = check_number + ar[integer_2];
            if sum % k == 0:
                count_div += 1;
            integer_2 += 1;

    return count_div;            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = map(int, raw_input().rstrip().split())

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

