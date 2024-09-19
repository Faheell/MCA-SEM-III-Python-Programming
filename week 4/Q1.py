def cal_sum_sub():
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    sum = num1 + num2
    sub = num1 - num2
    return sum,sub

sum,sub=cal_sum_sub()
print("Sum : ",sum )
print("Subtraction : ",sub)