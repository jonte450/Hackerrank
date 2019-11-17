#Beautiful Days at the movies

#!/bin/python3
 
import math
import os
import random
import re
import sys
 
# Complete the beautifulDays function below.

def beautifulDays(i, j, k):

   loop_length = j + 1;
   count_b_days = 0;
   while i < loop_length:
       convert_to_string = str(i);
       get_reversed = convert_to_string[::-1];
       print(get_reversed);
       if abs((i-int(get_reversed))% k == 0):
           count_b_days = count_b_days + 1;
       i = i + 1;
   return count_b_days;
       
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
   ijk = input().split()
 
   i = int(ijk[0])
 
   j = int(ijk[1])
 
   k = int(ijk[2])
 
   result = beautifulDays(i, j, k)
 
   fptr.write(str(result) + '\n')
 
   fptr.close()
