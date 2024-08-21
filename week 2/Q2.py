number=int(input("Enter number to count digit : "))
digit=0
if number==0:
    print("Number should be greater than 0")
else:
    while number > 0:
        number = number // 10
        digit+=1
    print("Total digit : ",digit)
