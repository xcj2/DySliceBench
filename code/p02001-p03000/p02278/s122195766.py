
def resolve():
    def solve(n, arr):

        def cycles():
            V = [False]*N
            B = sorted(A)
            T = {B[i]:i for i in range(N)}
            C = []
            for i in range(N):
                if V[i]:
                    continue
                cur = i
                cycle = []
                while not V[cur]:
                    V[cur] = True
                    cycle.append(cur)
                    cur = T[A[cur]]
                C.append(cycle)
            return C

        ans = 0
        minV = min(A)
        for cycle in cycles():
            S = sum([A[i] for i in cycle])
            m = min([A[i] for i in cycle])
            an = len(cycle)
            ans += min(S+(an-2)*m, S+(an+1)*minV+m)
        return ans

    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)

if __name__ == '__main__':
    resolve()
