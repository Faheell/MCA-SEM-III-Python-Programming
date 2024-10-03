l1=[]
l2=[]
size=int(input("Enter size of tuple:"))
print("Enter elements in tuple 1")
for i in range(size):
    element=int(input("-> "))
    l1.append(element)
print("Enter elements in tuple 2")
for i in range(size):
    element=int(input("-> "))
    l2.append(element)
tuple1=tuple(l1)
tuple2=tuple(l2)
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
Final_tuple=tuple(l1+l2)
print("Final Tuple ",Final_tuple)