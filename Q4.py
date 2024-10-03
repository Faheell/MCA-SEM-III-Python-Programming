main_string = input("Enter the main string: ")

# Define the symbol-based string to be embedded
symbol = "@#"

# Create the encrypted string
encrypted_string = ""
for char in main_string:
    encrypted_string += char + symbol

# Display the encrypted string
print("Encrypted string:", encrypted_string)

# Decrypt the string by removing the symbol-based string
decrypted_string = ""
for i in range(0, len(encrypted_string), 3):  # Simplified iteration step
    decrypted_string += encrypted_string[i]  # Add the character before the symbol

# Display the decrypted string
print("Decrypted string:", decrypted_string)
