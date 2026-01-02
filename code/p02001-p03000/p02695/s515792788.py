def read_int():
    return int(input())

def read_int_map():
    return map(int,input().split(' '))

def read_int_list():
    return list(map(int,input().split(' ')))

def read_s_list_loop(n):
    return [input() for _ in range(n)]

N,M,Q = read_int_map()
ans_map = {}

abcd_list = []
for i in range(Q):
    abcd_list.append(read_int_list())

abcd_list.sort(key=lambda x:(x[0],x[1]))

for abcd in abcd_list:
    a,b,c,d = map(int,abcd)

import copy
import sys
sys.setrecursionlimit(36288000)
all_list = []
def make_list(current=1,n=10,m=10,current_list=[],cnt=0):
    cnt += 1
    for i in range(current,m):
        tmp = copy.deepcopy(current_list)
        tmp.append(i)
        if cnt == n:
            global all_list
            all_list.append(tmp)
        else:
            make_list(i,n,m,tmp,cnt)
make_list(current=1,n=N,m=M+1,current_list=[],cnt=0)
ans = 0
for An in all_list:
    tmp = 0
    for abcd in abcd_list:
        a,b,c,d = map(int,abcd)
        if An[b-1] - An[a-1] == c:
            tmp += d
    ans = max(tmp,ans)
print(ans)