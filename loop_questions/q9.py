# # ##Q = 9 << WAP TO PRINT A NUMBER INPUT FROM THE USER IS PRIME NUMBER OR NOTT [PRIME NO. = THIS IS ONLY DIVISIBLE BY OWN NUMBER AND 1 ]
# while True:
#  num = int (input("enter number :"))

# #  if num<1:
# #     print (num,"is not a prime number !")
# #  else :
#  is_prime = True
#  for i in range (2,int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
        
#  if is_prime:
#         print(num,"is a prime number !!")
#  else :
#         print (num,"is not a prime number !!")
        
     
     


while True:

 num = int(input("Enter a number = "))
 is_prime = True

 for i in range (2,int(num**0.5)+1):
       if num%i==0:
              is_prime = False
 if is_prime and num >=1:
        print (num,"is a PRIME number!!")
 else:
        print (num,"is NOT a PRIME number!!")