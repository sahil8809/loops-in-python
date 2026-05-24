# num = int(input("Enter number :"))
# is_prime = True
# for i in range (2,int(num**0.5)+1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print (num,"is a prime number !!")
# else :
#     print (num,"is not a prime a number!!")





# %%%%%%%%%%%%%%%%%%%%%%%%%%%% 💖 CREATING A HEART 💖 %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

import math
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12 * math.cos(k) - 5 * \
           math.cos(2*k) - 2 * \
           math.cos(3*k) - \
           math.cos(4*k) 

speed (0)
bgcolor("black")
for i in range (6000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range (1):
        color("red")
    dot () #DRAW A DOT AT CURRENT POSITion

goto (0,0)
done ()

