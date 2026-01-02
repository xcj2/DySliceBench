import collections,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
n = I()
A = LI()
q = I()
m = LI()
partial_sum = set()
stack = [] #indexとsumを入れておく
def dfs():
    stack.append([0,0])
    stack.append([0,A[0]])
    partial_sum.add(A[0])
    while stack:
        i,s = stack.pop()
        i += 1
        if i==n:
            partial_sum.add(s)
            continue
        stack.append([i,s])
        stack.append([i,s+A[i]])
dfs()
for x in m:
    print('yes' if x in partial_sum else 'no')

