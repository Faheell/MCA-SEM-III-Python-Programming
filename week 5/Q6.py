import numpy as np

array1 = np.array([[34, 23, 12],
                  [45, 65, 78],
                  [56, 33, 25]])

#printing array orginially
for e in array1:
    print(e)
print(" ")

# Case 1: Sort array by the second row
print("Row 2")
print(array1[2:3,:])
print("Sorted Row 2")
print(np.sort(array1[2:3,:]))
print("--------------")
# Case 2: Sort array by the second column
print("Column 2")
print(array1[:,2:3])
print("Sorted Column 2")
# set axis=0 for column
print(np.sort(array1[:,2:3],axis=0))
