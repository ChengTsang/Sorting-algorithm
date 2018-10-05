def partition(num_list, p, r):
    x = num_list[r]
    i = p-1
    for j in range(p,r):
        if num_list[j] <= x:
            i = i+1
            num_list[i],num_list[j] = num_list[j], num_list[i]
    num_list[i+1], num_list[r] = num_list[r], num_list[i+1]
    return i+1

def quick_sort(num_list, p, r):
    if p < r:
        q = partition(num_list, p, r)
        quick_sort(num_list, p, q-1)
        quick_sort(num_list, q+1, r)

num_list = [4,2,1,3,8,0,7,1.5,9,-2]
quick_sort(num_list,0,len(num_list)-1)
print(num_list)