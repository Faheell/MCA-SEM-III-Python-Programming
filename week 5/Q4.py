list1=[]
list2=[]
list3=[]
size=int(input("Enter size of list"))

print("Enter element in list 1")
for i in range(size):
    print("Element ",i+1)
    list1.append(int(input("->")))

print("Enter element in list 2")
for i in range(size):
    print("Element ",i+1)
    list2.append(int(input("->")))

for i in range(size):
    if list1[i]%2!=0:
        list3.append(list1[i])
    if list2[i]%2==0:
        list3.append(list2[i])

print("Final list")
for i in range(len(list3)):
    print("Element ",i+1,"->",list3[i])