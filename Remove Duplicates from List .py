# Remove Duplicates from List 
# my_list = list([10,20,10,30,50])

# unique_list = set(my_list)
# print(unique_list)

my_list = [10,20,10,30,50]

unique_list = []
 
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)