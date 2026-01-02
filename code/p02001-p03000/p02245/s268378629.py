import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    S = []
    SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    for _ in range(3):
        S += LI()

    neighbor = (
        (1, 3),      
        (0, 2, 4),   
        (1, 5),      
        (0, 4, 6),   
        (1, 3, 5, 7),
        (2, 4, 8),   
        (3, 7),      
        (4, 6, 8),   
        (5, 7)       
    )

    dist = dict()
    que = collections.deque()
    S = tuple(S)
    que.append((S, S.index(0)))
    dist[S] = 0
    while que:
        c, idx_0 = que.popleft()
        if c == SOLVED:
            break
        for i in neighbor[idx_0]:
            c_l = list(c)
            c_l[idx_0], c_l[i] = c_l[i], c_l[idx_0]
            n = tuple(c_l)
            if not n in dist:
                que.append((n, i))
                dist[n] = dist[c] + 1

    print(dist[SOLVED])

if __name__ == '__main__':
    resolve()

