def merge(num_list, p, q, r):
    #n_1 = q - p + 1
    #n_2 = r - q
    L_1 = num_list[p:q+1]
    L_1.append(float('inf'))
    L_2 = num_list[q+1:r+1]
    L_2.append(float('inf'))

    i = 0
    j = 0
    for k in range(p,r+1):
        if L_1[i] <= L_2[j]:
            num_list[k] = L_1[i]
            i += 1
        else:
            num_list[k] = L_2[j]
            j += 1

def merge_sort(num_list, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(num_list, p, q)
        merge_sort(num_list, q+1, r)
        merge(num_list, p, q, r)

num_list = [4,2,1,3,8,0,7,1.5,9,-2]
merge_sort(num_list,0,len(num_list)-1)
print(num_list)