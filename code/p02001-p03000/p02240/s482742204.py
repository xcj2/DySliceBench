from collections import deque

def connected_components(U, C):
    no = 1

    for i in range(len(U)):
        if C[i] == None:
            depth_first_serch(U, C, i, no)
            no += 1

def depth_first_serch(U, C, r, no):
    S = list()
    S.append(r)

    while len(S) != 0:
        current = S[-1]
        
        if len(U[current]) != 0:
            v = U[current].popleft()
            if C[v] == None:
                C[v] = no
                S.append(v)
        else:
            C[current] = no
            S.pop()

def Main():
    N, M = map(int, input().split())
    Users = [deque() for n in range(N)]
    Color = [None for n in range(N)]

    for m in range(M):
        s, t = map(int, input().split())
        Users[s].append(t)
        Users[t].append(s)

    connected_components(Users, Color)

    Q = int(input())

    for q in range(Q):
        s, t = map(int, input().split())
        if Color[s] == Color[t]:
            print("yes")
        else:
            print("no")

Main()
