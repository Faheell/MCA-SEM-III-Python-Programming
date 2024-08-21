num = int(input("Enter number to find factorial : "))
fact=1
if num<=0:
    print("Number must be greater than 0")
else:
    for i in range(num,0,-1):
        fact=fact*i
    print("Factorial of ",num,"is: ",fact)
