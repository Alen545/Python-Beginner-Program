# Second Largest Number in a List
# Selecting Sorting
num_list = [10,5,20,35,7]

for i in range(0,len(num_list)):
    for j in range(i+1,len(num_list)):
        if num_list[i] >= num_list[j]:
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp

print(num_list[-2])

# Easy method
# num_list.sort()
# print(num_list[-2])