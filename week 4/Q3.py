num=[]
size=int(input("enter size of list "))
for i in range(size):
    print("Enter elements")
    num.append(int(input("->")))
print("Cube of Elements in list ")
for i in range(size):
    print("Element ",num[i],"Cube :",num[i]**3)

