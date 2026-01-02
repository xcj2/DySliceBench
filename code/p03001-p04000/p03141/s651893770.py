def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


N = read()
A = []
B = []
C = []
D = []
for _ in range(N):
    a, b = readmap()
    A.append(a)
    B.append(b)
    C.append(a+b)
    D.append((a, b))

# A.sort(key=dict(zip(A, C)).get)
# B.sort(key=dict(zip(B, C)).get)
#
# A.reverse()
# B.reverse()

D.sort(key=dict(zip(D, C)).get)
D.reverse()

# ans = 0
# for i in range(N):
#     if i % 2 == 0:
#         ans += A[i]
#     else:
#         ans -= B[i]

ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += D[i][0]
    else:
        ans -= D[i][1]

print(ans)