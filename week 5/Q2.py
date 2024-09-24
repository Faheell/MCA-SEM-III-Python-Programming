import random as rd
str=input("Enter String:")
random_char=str[rd.randint(0,len(str)-1)]
print("Random char from ",str,":",random_char)