import sys
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()

def solve():
    N, M = map(int, input().split())
    A = [None] * N
    for i in range(N):
        A[i] = list(map(int, line_input()))
    pointer = [0] * N
    used = set()
    minmax = 500
    for m in range(M):
        num_people = [0] * M
        maxgather = (0, 0)
        for n in range(N):
            num_people[A[n][pointer[n]] - 1] += 1
            if num_people[A[n][pointer[n]] - 1] > maxgather[0]:
                maxgather = (num_people[A[n][pointer[n]] - 1], A[n][pointer[n]])
        used |= {maxgather[1]}
        minmax = min(minmax, maxgather[0])
        for n in range(N):
            while pointer[n] < M:
                if A[n][pointer[n]] in used:
                    pointer[n] += 1
                else: break
    print(minmax)
    return 0
  
if __name__ == "__main__":
    solve()