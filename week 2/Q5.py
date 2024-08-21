number=int(input("Enter number "))
sum=0
while number > 0:
    sum=sum+(number%10)
    number=number//10
print("Sum : ",sum)
