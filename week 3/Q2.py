# Upper right triangle
for i in range(1,6):
    for x in range(i):
        print("*",end=' ')
    print()
# Lower triangle
for i in range(4,0,-1):
    for x in range(i):
        print("*",end=' ')
    print()