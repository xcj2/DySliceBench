from collections import deque
readline = open(0).readline
writelines = open(1, 'w').writelines
N, Q = map(int, readline().split())
ans = []
A = [deque() for i in range(N)]
def push(t, x):
    A[t].append(str(x))
def dump(t):
    ans.append(" ".join(A[t]))
    ans.append("\n")
def splice(s, t):
    if A[s]:
        if A[t]:
            if len(A[s]) == 1:
                A[t].append(A[s][0])
            elif len(A[t]) == 1:
                A[s].appendleft(A[t][0])
                A[t] = A[s]
            else:
                A[t].extend(A[s])
        else:
            A[t] = A[s]
        A[s] = deque()

C = [push, dump, splice].__getitem__
for i in range(Q):
    t, *a=map(int, readline().split())
    C(t)(*a)
writelines(ans)
