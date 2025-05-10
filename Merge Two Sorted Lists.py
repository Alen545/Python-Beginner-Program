# Merge Two Sorted Lists 
list1 = [10,30,5,45,0]
list2 = [20,40,15,9,100]

my_list = list1 + list2

for i in range(len(my_list)):
    for j in range(len(my_list)-1-i):
        temp = []
        if my_list[j] > my_list[j+1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp

print(my_list)

