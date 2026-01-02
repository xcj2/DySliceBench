def bubble_sort_revision(target_list):#?????????????????????

    list_length = len(target_list)
    
    flag = True
    change_count = 0
    
    for top_index in range(1,list_length):
        for i in range(top_index, list_length)[::-1]:
            if target_list[i] < target_list[i - 1] and target_list[top_index] >= target_list[i]:
                tmp = target_list[i]
                target_list[i] = target_list[i - 1]
                target_list[i - 1] = tmp
                change_count += 1
                
    return change_count

def my_add(bit, i, x):
    while i <= len(bit) - 1:
        bit[i] += x
        i += int(bin(i & -i), 2)
        
def my_sum(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= int(bin(i & -i), 2)
    return s

def merge(l,r):
    global count
    l_index = 0
    r_index = 0
    merge_list = []
    l.append(pow(10,9) + 1)
    r.append(pow(10,9) + 1)

    len_l = len(l) - 1
    for k in range(len(l) + len(r) - 2):
        if l[l_index] < r[r_index]:
            merge_list.append(l[l_index])
            l_index += 1
            len_l -= 1
        else:
            count += len_l
            merge_list.append(r[r_index])
            r_index += 1

    return merge_list
    
def merge_sort(target_list):
    if len(target_list) == 1:
        return target_list
    
    mid = int(len(target_list) / 2)
    
    r = merge_sort(target_list[mid:])
    l = merge_sort(target_list[:mid])
    
    return merge(l, r)

def bit_solve(n, target_list):#???????????§????????????bit?????§?????????????????????
    bit = [0 for i in range(max(target_list) + 2)]
    ans = 0
    for i in range(n):
        ans += i - my_sum(bit, target_list[i] + 1)
        my_add(bit, target_list[i] + 1, 1)
        print(ans, target_list[i], bit)
    return ans

if __name__ == "__main__":
    global count
    count = 0
    l = int(input())
    target_list = [int(i) for i in input().split()]
    merge_sort(target_list)
    print(count)
    