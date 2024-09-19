tp1 = (50, 10, 60, 70, 50)
size = len(tp1)-1
occurrence = 0
i=0
while i<=size:
    if tp1[i] == 50:
        occurrence = occurrence+1
    i=i+1

print("Total 50 in tp1:",occurrence)
