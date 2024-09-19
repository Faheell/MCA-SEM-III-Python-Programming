num = []


def check_number_in_list():
    #last_element_of_list=num[size]
    for i in range(len(num)):
        if num[0] == num[-1]:
            return True
        else:
            return False


size = int(input("Enter total number of element in list "))
for i in range(size):
    print("Element ",i+1)
    num.append(int(input("-> ")))

result=check_number_in_list()
print(result)