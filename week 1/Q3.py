listNum =[]
print("Enter 20 numbers ")
for i in range(20):
    print("Enter number ",i+1)
    listNum.append(int(input()))
print("Numbers which are divisible by zero ")
for i in range(20):
    if listNum[i]%5==0:
        print("Number Index in list ", i+1 ," Number :",listNum[i])
print("---ENDED---")

