
# # Q = 8 <<  WAP TO CALCULATE FACTORIAL OF A NUMBER GIVEN BY USER 
# print ("||__WELCOME TO FACTORIAL FINDER __||")
# while True:   # while True ki wajah se baar baar hamara code input lete rahega >>>
#  n = int(input("enter a number :"))
    
#  factorial = 1
#  for i in range (1,n+1):
#     factorial*=i
#  print (f"Factorial of '{n}' is = {factorial}")


import sys 
import os 
sys.path.append(os.path.abspath("."))
from JasiqLab.phase1.function import calculater
from JasiqLab.phase1.function_loop import check_password

result = calculater()     # function calling 
print ("RESULT IS :" , result)