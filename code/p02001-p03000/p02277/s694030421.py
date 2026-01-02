#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_C&lang=jp

def partition(target_list, l, r):
    x = int(target_list[r][1:])
    i = l - 1

    for j in range(l, r):
        if int(target_list[j][1:]) <= x:
            i = i + 1
            tmp = target_list[i]
            target_list[i] = target_list[j]
            target_list[j] = tmp
    tmp = target_list[r]
    target_list[r] = target_list[i + 1]
    target_list[i + 1] = tmp
    
    return  i + 1

def merge(l,r):
    
    l_index = 0
    r_index = 0
    merge_list = []
    l.append("X " + str(pow(10,9) + 1))
    r.append("X " + str(pow(10,9) + 1))
   
    for k in range(len(l) + len(r) - 2):
        if int(l[l_index][1:]) <= int(r[r_index][1:]):
            merge_list.append(l[l_index])
            l_index += 1
        else:
            merge_list.append(r[r_index])
            r_index += 1
    
    return merge_list
    
def merge_sort(target_list):
    if len(target_list) == 1:
        return target_list
    
    mid = int(len(target_list) / 2)
    l = merge_sort(target_list[:mid])
    r = merge_sort(target_list[mid:])
    
    return merge(l, r)

def check_stable(origin_list, target_list):
    sorted_list = merge_sort(origin_list)
    if sorted_list == target_list:
        return "Stable"
    return "Not stable"

def quick_sort(target_list, l, r):
    if l < r:
        c = partition(target_list, l, r)
        quick_sort(target_list, l, c - 1)
        quick_sort(target_list, c + 1, r)
        
if __name__ == "__main__":
    n_list = int(input())

    target_list = []
    for i in range(n_list):
        target_list.append(input())
    origin_list = [a for a in target_list]
    quick_sort(target_list, 0, n_list - 1)
    print(check_stable(origin_list, target_list))
    print("\n".join(target_list))