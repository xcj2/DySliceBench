import bisect
import copy
def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))


N=one_int()
L=many_int()

L=sorted(L)

sankaku_dict={}
count=0
for i in range(len(L)-1):
    low=L[i]
    for j in range(i+1, len(L)):
        #すでに探索済みか判定
        high = L[j]
        
        #上限を取得
        high_index = bisect.bisect_left(L[j+1:], high+low)
        count+=high_index#len(L[j+1:high_index])

# len(sankaku_dict)
print(count)
# print(len(sankaku_dict.keys()))