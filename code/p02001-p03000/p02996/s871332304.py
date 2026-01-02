import sys
from collections import deque
stdin = sys.stdin

def ii(): return int(stdin.readline())
def li(): return map(int, stdin.readline().split())
N = ii()
infos = [ tuple(li()) for i in range(N) ]
infos.sort(key=lambda x:x[1])
def do(infos):
    works = deque()
    time = 0
    used = 0
    for t, e in infos:
        time += t
        works.append( (t, e) )
        while works and time >= works[0][1]:
            deadline = works[-1][1]
            lt, le = works.popleft()
            if deadline < time:
                return "No"

    return "Yes"
print(do(infos))

