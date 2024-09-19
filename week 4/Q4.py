list1=[]
list2=[]
size=int(input("Enter size of list "))
print("List 1")
for i in range(size):
    print("Enter element")
    list1.append(int(input("->")))
print("------------")
print("List 2")
for i in range(size):
    print("Enter element")
    list2.append(int(input("->")))
print("Elements in List 1 in Original order and in List 2 in reverse order")
for i in range(size):
    print(list1[i],list2[-i])

