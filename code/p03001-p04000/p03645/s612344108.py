def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))


N,M = two_int()

from collections import defaultdict
start_dicts =defaultdict(list)
end_dicts = defaultdict(list)
for i in range(M):
    a,b = two_int()

    if a in start_dicts:
        start_dicts[a].append(b)
    else:
        start_dicts[a] =[b]

        
    if b in end_dicts:
        end_dicts[b].append(a)
    else:
        end_dicts[b] =[a]


if len(set(start_dicts[1]) & set(end_dicts[N]))>0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")