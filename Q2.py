User_Dictionary={}
str="yes"
print("Enter data in dictionary")
while(str=="yes"):
    Name=input("Enter Name:").upper()
    Number=int(input("Enter Name:"))
    User_Dictionary[Name]=Number
    str=input("Enter more yes/no").lower()
    if(str=="no"):
        break
print(User_Dictionary)
name=input("Enter Name to fetch mobile number:").upper()
if name not in User_Dictionary:
    print("Invalid Entry")
else:
    print("Mobile Number:",User_Dictionary[name])