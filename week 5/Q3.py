import random as rd
import math
print("10 digit password")
UpperCase1=chr(rd.randint(65,90))
UpperCase2=chr(rd.randint(65,90))
SpecialSymbol=chr(rd.randint(33,47))
number=str(rd.randint(1000000,9999999))
print("Password ",UpperCase1+SpecialSymbol+number+UpperCase2)