def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

N, M = MAP()
H = LIST()
lights = [0] * N
for _ in range(M):
    a, b = MAP()
    a -= 1; b -= 1
    if lights[a] == 0:
        if H[a] <= H[b]:
            lights[a] += 1
    if lights[b] == 0:
        if H[b] <= H[a]:
            lights[b] += 1

print(lights.count(0))

# ans = 0
# for i in range(N):
#     flag = True
#     j = 0
#     while flag or j < len(AB):
#         a, b = AB[j][0], AB[j][1]
#         if a == i and H[a] <= H[b]:
#             flag = False
#             break

#         j += 1
#         if j == len(AB):
#             break

#     if flag:
#         ans += 1
# import deque





# print(ans)

 