#   WAP TO PRINT NUMBERS FROM 1 TO 5 IN A ROW LIKE THIS :- 1,2,3,4,5


for i in range (1,6):      # 1 IS STARTING VALUE AND 6 = 6 - 1  IS LAST VALUE 
    print (i,end =" ")  # END =" " IS USED TO PRINT VALUE IN A SINGLE LINE 
print("\n"+"-"*50)   



# Q = 2 <<  WAP TO PRINT SQUARE OF THE NUMBERS 

for square in range (1,6):
    print (square**2 ,end=" ")   # heere we use an opeartor called square operator 
print("\n"+"-"*50)    

# Q = 3 << WAP TO PRINT ALLL EVEN NUMBERS FROM 1 TO 10 

for even in range (1,11):
 if even % 2 == 0:
     print (even,end=" ")
print("\n"+"-"*50)
     
     
#Q = 4 << WAP TO PRINT SUM FROM 1 TO 10 NUMBER 

total = 0
for i in range (1,11):
    total +=i
print ("sum is : ",total)
print ("_"*50)


# Q = 5 << WAP TO PRINT A WORD 'PYTHON' IN REVERSE USING A FOR LOOP 

word = 'python'
for i in range (len(word)-1,-1,-1):
    print (word[i],end=" ")
print ("\n"+"-"*50)



# q = 6 << wap to counr numbers of vowels in a string / word "education"

word = "education"
vowel = "aeiou"
start = 0

for char in word:
    if char in vowel:
        start+=1
print (f"total vowel in '{word}' is '{start}' ")
print ("-"*50)



# Q = 7 <<< WAP TO PRINT THE FIRST 10 TERMS OF FIBONACCI SERIES 

a = 0
b = 1
print (a,b , end=" ")
for _ in range (8):
    next_term = a + b
    print (next_term , end=" ")
    a,b = b,next_term
print("\n"+"-"*50)



# Q = 8 <<  WAP TO CALCULATE FACTORIAL OF A NUMBER GIVEN BY USER 

n = int(input("Enter a number = "))
fact = 1
# fact variale starts heere from 1
for i in range (1,n+1): #loop i start from 1 and goes upto n+1 (input number) 
    fact *= i
# fact multy by i (i from loop [1 to n+1]) if useer input 5 then is goes upto 6 , that runs upto 5.

print (f"Factorial of '{n}' is = {fact}")
print ("-"*50)



#Q = 9 << WAP TO PRINT A NUMBER INPUT FROM THE USER IS PRIME NUMBER OR NOTT [PRIME NO. = THIS IS ONLY DIVISIBLE BY OWN NUMBER And 1 ]


num = int(input("Enter a number ="))
is_prime = True

for i in range (2,int(num**0.5)+1):  # (2,int(num**0.5)+1): this means 2 se shuru hoga and num ka square root in integer form me ho jaayega and usme +1 add hoga 
       if num%i==0:      #  agar num 'i' se pura divide ho rha hai toh 
              is_prime = False # is_prime false ho jaayega
if is_prime and num >= 1:   # means is_prime is true and num is greater and equal to 1 then print num is a prime number otherwise execute else statement thaat is num is not a prime a number 
       print(num,"is a prime number!!")
else :
       print (num,"is NOT a prime number!!")
print ("_"*50)
       
       
       
       
# Q = 10 << WAP TO COUNT OCCURENCE OF EACH CHARACTER IN THE WORD 'PROGRAMMING'

word = 'programming'
char_count = {}
for char in word:  # loop for characters is present in word then
    if char in char_count:   # agar character char_count me hai toh
        char_count[char]+=1 # toh char_count of character ki value ko increament kardo
    else :
        char_count[char]=1 # agar nhi hai toh char_count of character ko 1 rahne do
for char , count in char_count.items():  #items used for printing values in column wise
    print(char + ':',count) #pehle character then colon and then count(1,2,3,4,5........)
print ("_"*50)