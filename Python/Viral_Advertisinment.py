#Viral Advertisinment

#!/bin/python3
 
import math
import os
import random
import re
import sys
 
# Complete the viralAdvertising function below.
def viralAdvertising(n):
   notitfy_people = 0;
   share = 5;
   loop_end = n + 1;
   turn = 1;
   while turn < loop_end:
       likes_it = share //2;
       notitfy_people += likes_it;
       share = likes_it*3;
       turn = turn + 1;
   return notitfy_people;   
 
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
   n = int(input())
 
   result = viralAdvertising(n)
 
   fptr.write(str(result) + '\n')
 
   fptr.close()
