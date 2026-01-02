from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, a, b, c = rl()
    moves = []
    ans = []
    abc = [a,b,c]
    for i in range(n):
        moves.append(input())
    moves.append(moves[-1])

    for i in range(len(moves) - 1):
        curr = moves[i]
        nxt = moves[i + 1]
        x = {"A":0, "B":1, "C":2}[curr[0]]
        y = {"A":0, "B":1, "C":2}[curr[1]]
        nx = {"A":0, "B":1, "C":2}[nxt[0]]
        ny = {"A":0, "B":1, "C":2}[nxt[1]]

        if abc[x] == 0 and abc[y] == 0:
            print ("No")
            return
        elif abc[x] == 0:
            abc[x] += 1
            abc[y] -= 1
            ans.append(curr[0])
        elif abc[y] == 0:
            abc[x] -= 1
            abc[y] += 1
            ans.append(curr[1])
        elif x == y and nx == ny:
            abc[x] += 1
            abc[y] -= 1
            ans.append(curr[0])
        else:
            common = list(set([x,y]).intersection(set([nx,ny])))[0]
            if x == common:
                other = y
                ans.append(curr[0])
            else:
                other = x
                ans.append(curr[1])
            abc[common] += 1
            abc[other] -= 1

    print ("Yes")
    for l in ans:
        print (l)


mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
