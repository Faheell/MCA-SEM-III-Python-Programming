numbers_list=[]
size = int(input("Total number to cube "))

# taking inputs from users
for i in range(size):
    print("Enter number ",i+1)
    numbers_list.append(int(input()))

# Cubing all the numbers
for i in range(size):
    print("Number @ index ",i+1,"->",numbers_list[i]," cube is :",numbers_list[i]**3)

