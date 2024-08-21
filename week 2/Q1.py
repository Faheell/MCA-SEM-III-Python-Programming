number = int(input("Enter number to Reverse : "))
if number ==0:
    print("Number should be greater than 0")
else:
    Original_number = number
    temp=0
    # reverse the digit
    while number>0:
        last_digit = number % 10
        temp = temp * 10 + last_digit
        number = number // 10
    print("Reversed Number ",temp)

