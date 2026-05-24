# #WAP TO COUNT OCCURENCE OF EACH CHARACTER IN THE WORD 'PROGRAMMING'
# word = 'programming'
# char_count = {}
# for char in word :
#     if char in char_count:
#         char_count[char]+=1
#     else :
#         char_count[char]=1
        
# for char ,count in char_count.items():
#     print(char +':',count)













while True:
 word = str(input("Enter any word or sentences = "))
 char_count = {}
 for char in word:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char]=1
 
# items used for printing values
 for char ,count in char_count.items():
    print(char + ':',count)