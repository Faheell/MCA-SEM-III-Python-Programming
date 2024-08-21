list_Of_Numbers=[]
print("Enter 10 numbers ")
for i in range(10):
    print("Number : ",i+1)
    list_Of_Numbers.append(int(input()))
temp=0
for i in range(10):
    temp = temp + list_Of_Numbers[i]
print("Sum of all 10 numbers ",temp)