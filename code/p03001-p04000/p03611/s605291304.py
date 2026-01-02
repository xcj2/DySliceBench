def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

from collections import defaultdict
dicts = defaultdict(int)

N=one_int()
X=many_int()

sorted_X = sorted(X)

for i in sorted_X:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1

max_num = 1
for j in range(sorted_X[0]-1,sorted_X[-1]+1):
    temp_sum = dicts[j-1] + dicts[j] + dicts[j+1]
    
    if max_num < temp_sum:
        max_num = temp_sum

print(max_num)