def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list



list = [5,1,4,6,7,2,8,3]

bubble_sort(list)

print(list)
