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
D=many_int()

num=998244353


dicts={i:0 for i in range(N)}
for d in D:
    if d in dicts:
        dicts[d] += 1
    else:
        dicts[d] = 1

sums = 1
keys = sorted(list(dicts.keys()))

test = [i for i in range(len(keys))]
flg=False
for t,k in zip(test,keys):
    if t!=k:
        flg=True

if keys[0]!=0 or D[0]!=0:
    flg=True
else:
    if dicts[0]!=1:
        flg=True
        
if flg:
    sums=0

for i in range(len(keys)-1):
    if i >= 1:
        for j in range(dicts[keys[i+1]]):
            sums *= (dicts[keys[i]])
            sums = sums%num
print(sums)