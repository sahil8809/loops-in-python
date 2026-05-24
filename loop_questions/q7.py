# FIBONACCI SERIES IS PREVIOUS 2 NUMBERS 0 , 1 ADDITION (0+1=1),0,1,1,2,3,5,8,13,21.....
# PEHLA 2 NUMBERS KA SUM 
# Q = 7 <<< WAP TO PRINT THE FIRST 10 TERMS OF FIBONACCI SERIES 

# a = 0
# b = 1
# print (a,b , end=" ")
# for _ in range (50):
#     next_term = a + b
#     print (next_term , end=" ")
#     a,b = b,next_term


####### TYPECASTING ########
# TWO TYPES OF TYPECASTING 1. EXPLICIT TYPECASTING , 2. IMPLICIT TYPECASTING 



          #  1. EXPLICIT TYPECASTING

a = "15"        # this is a string data type it is not any integer at this time

number = 10

string_to_integer = int(a)
print (f"That string < {a} > is now become an integer data type < {string_to_integer} >. After doing typecasting :",string_to_integer)

print (type(a))        # used to see the actual data type of "A"
print (type(number))


sum_of_str_and_number = (int(a)+number)
print(sum_of_str_and_number)






                    # 2. IMPLICIT TYPECASTING 

# THE CONVERSION THAT DONE THROUGH THE PYTHON IS CALLED IMPLICIT TYPECONVERSION  

c = 9.5

d = 3 

print(c+d)

# python automatically converts 
# A to int 

a = 7
print (type(a))

#python automaticalluy convert b to float

b = 3.17
print (type(b))

#python automatically converts c to float as it is a float adddition 

c = a+b
print (type(c))

#SHOW output 
print (c)