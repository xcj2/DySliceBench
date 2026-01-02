import sys,time
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def solve():
    start = time.time()

    N = inp()
    AA = [inpl() for _ in range(N)]
    itrs = [0]*N
    ans = cnt = 0

    while True:
        next = set()
        for x,itr in enumerate(itrs):
            if itr < N-1:
                t = AA[x][itr] - 1
                if AA[t][itrs[t]]-1 == x:
                    next.add(x)

        for n in next:
            itrs[n] += 1
            if itrs[n] == N-1:
                cnt += 1

        if len(next) == 0:
            for x in itrs:
                if x != N-1:
                    return -1
            return ans

        now = time.time() - start
        if now > 1.6:
            return N*(N-1)//2

        ans += 1

if __name__ == '__main__':
    print(solve())
