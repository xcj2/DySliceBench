import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7


def conv(n,a,b):
    return a*(2*n-a-1)//2+b-a-1

def main(): 
    N = II()
    # A = [[] for _ in range(N)]
    # for i in range(N):
    #     A[i] = LI()

    # print(A)
    # return

    from collections import defaultdict
    outs = defaultdict(list)
    ins = defaultdict(int)
    for i in range(N):
        # prev_v = (i+1, A[i][0]) if i+1 < A[i][0] else (A[i][0], i+1)
        a = LI()
        for j in range(1,N-1):
            # prev_v = (i+1, A[i][j-1]) if i+1 < A[i][j-1] else (A[i][j-1], i+1)
            # next_v = (i+1, A[i][j]) if (i+1 < A[i][j]) else (A[i][j] , i+1)
            # prev_v = conv(N, prev_v[0], prev_v[1])
            # next_v = conv(N, next_v[0], next_v[1])
            prev_v = (min(i+1, a[j-1]), max(i+1, a[j-1]))
            next_v = (min(i+1, a[j]), max(i+1, a[j]))
            prev_v = conv(N, prev_v[0]-1, prev_v[1]-1)
            next_v = conv(N, next_v[0]-1, next_v[1]-1)
            outs[prev_v].append(next_v)
            ins[next_v] += 1

    # print(outs, ins)
    # return

    from collections import deque
    q = deque()
    for i in range(1, N+1):
        for j in range(1, N+1):
        # j = A[i-1][0]
            if i < j and ins[conv(N, i-1, j-1)] == 0:
                q.append([conv(N, i-1, j-1), 0])

    if not q:
        print(-1)
        return

    # q = deque(v1 for v1 in range(1, N+1) if ins[v1] == 0)
    res = []
    depth_max = 0
    while q:
        v1, depth = q.popleft()
        res.append(v1)
        for v2 in outs[v1]:
            ins[v2] -= 1
            if ins[v2] == 0:
                q.append([v2, depth+1])
                depth_max = max(depth_max, depth+1)
    if len(res)!=N*(N-1)//2:
        print(-1)
        return
    else:
        print(depth_max+1)
        return


main()