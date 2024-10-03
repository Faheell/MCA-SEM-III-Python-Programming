file1=open("Marks.txt","w+")
str="yes"
print("Enter Details Of Students")
while str == "yes":
    Name=input("Enter Name:")
    Roll=int(input("Enter Roll Number:"))
    Marks=int(input("Enter marks:"))
    file1.write("Name: " + Name + ", Roll: " + Roll.__str__() + ", Marks: " + Marks.__str__() + "\n")
    str=input("Want to enter more details yes/no").lower()
    if str == "no":
        break
print("File Successfully created")
file1.close()