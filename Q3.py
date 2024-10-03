def sum_of_squares(num):
    if num>=1000 and num<=9999:
        # Extract first two digits and last two digits
        first_two_digits = num // 100    # Get first two digits
        last_two_digits = num % 100       # Get last two digits
        print("Firs Two digit",first_two_digits,"Square:",first_two_digits**2)
        print("Last Two digit",last_two_digits,"Square:",last_two_digits**2)
        result = (first_two_digits ** 2) + (last_two_digits ** 2)
        print("Result:",result)
    else:
        print("Please enter a 4-digit number.")

num = int(input("Enter a 4-digit number: "))
sum_of_squares(num)
