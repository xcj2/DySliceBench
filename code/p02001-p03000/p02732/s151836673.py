N = int(input())
A = list(map(int,input().split()))

def group_by_val(list_):
    res = dict()
    for v in list_:
        if v not in res:
            res[v] = [v]
            continue
        res[v].append(v)
    return res

def count_leng(dict_):
    res = dict()
    for k in dict_:
        res[k] = len(dict_[k])
    return res

def comb2(list_):
    leng = len(list_)
    if leng == 1:
        return 0
    return (leng*(leng-1)) // 2

grouped_dict = group_by_val(A)
group_leng = count_leng(grouped_dict)

sum_val = 0
for k in grouped_dict:
    sum_val += comb2(grouped_dict[k])

for a in A:
    print(sum_val-(group_leng[a]-1))