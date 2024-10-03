
input_string = input("Enter a string: ")


uppercase_count = 0
lowercase_count = 0
total_alphabets = 0
digit_count = 0


for char in input_string:
    if char.isupper():
        uppercase_count += 1
        total_alphabets += 1
    elif char.islower():
        lowercase_count += 1
        total_alphabets += 1
    elif char.isdigit():
        digit_count += 1


print("Number of uppercase characters:", uppercase_count)
print("Number of lowercase characters:", lowercase_count)
print("Total number of alphabets:", total_alphabets)
print("Number of digits:", digit_count)
