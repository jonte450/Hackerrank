#The Hurdle Race

#!/bin/python3
 
import math
import os
import random
import re
import sys
 
# Complete the hurdleRace function below.

def hurdleRace(k, height):
   check_max = max(height);
   print(check_max);
   if check_max > k:
       return abs(k-check_max);
   else:
       return 0;
 
          
 
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
   nk = input().split()
 
   n = int(nk[0])
 
   k = int(nk[1])
 
   height = list(map(int, input().rstrip().split()))
 
   result = hurdleRace(k, height)
 
   fptr.write(str(result) + '\n')
 
   fptr.close()
