l = input().split()
n = int(l[0])

l = input().split()
A = [int(x) for x in l]

# print(N, A)

A.sort()
P = []
N = []
for a in A:
    if a >= 0:
        P.append(a)
    else:
        N.append(a)

def print_ans(ans, pairs):
    print(ans)
    for p in pairs:
        print(p[0], p[1])

def solve_p(A):
    ans = A[0]
    pairs = []
    for i in range(1, n - 1):
        pairs.append((ans, A[i]))
        ans -= A[i]

    pairs.append((A[n - 1], ans))
    ans = A[n - 1] - ans
    print_ans(ans, pairs)

def solve_n(A):
    A.sort(key=lambda x: -x)
    ans = A[0]
    pairs = []
    for i in range(1, n - 1):
        pairs.append((ans, A[i]))
        ans -= A[i]

    pairs.append((ans, A[n - 1]))
    ans -= A[-1]
    print_ans(ans, pairs)

# #P == 1
def solve1(P, N):
    ans = P[0]
    pairs = []
    for n in N:
        pairs.append((ans, n))
        ans -= n
    print_ans(ans, pairs)

# #N == 1 #P > 1
def solve2(P, N):
    ans = N[0]
    pairs = []
    for i in range(len(P) - 1):
        pairs.append((ans, P[i]))
        ans -= P[i]
    pairs.append((P[-1], ans))
    ans = P[-1] - ans
    print_ans(ans, pairs)

# #P > #N
def solve3(P, N):
    num_p = len(P)
    num_n = len(N)
    ans = P[0]
    pairs = []
    for i in range(num_n - 1):
        pairs.append((ans, N[i]))
        ans -= N[i]
    pairs.append((N[-1], ans))
    ans = N[-1] - ans
    for i in range(1, num_p - 1):
        pairs.append((ans, P[i]))
        ans -= P[i]
    pairs.append((P[-1], ans))
    ans = P[-1] - ans
    print_ans(ans, pairs)

num_p = len(P)
num_n = len(N)
if num_p == 0:
    solve_n(A)
elif num_n == 0:
    solve_p(A)
elif num_p == 1:
    solve1(P, N)
elif num_n == 1:
    solve2(P, N)
else:
    solve3(P, N)
