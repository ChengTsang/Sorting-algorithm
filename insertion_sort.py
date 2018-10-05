def insertion_sort(num_list):
    #insertion sort is O(n^2)
    for i in range(1,len(num_list)):
        key = num_list[i]
        del num_list[i]
        for j in range(0,i):
            #print(j)
            if key <= num_list[j]:
                num_list.insert(j, key)
                break
            if j == i-1:
                num_list.insert(i, key)
    return num_list

num_list = [4,2,1,3,8,0,7,1.5,9,-2]
num_list_sort = insertion_sort(num_list)
print(num_list_sort)