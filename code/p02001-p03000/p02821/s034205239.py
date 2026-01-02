import sys
import bisect

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, M = na()
A_array = na()
A_array.sort()

hap_min = 0
hap_max = 3 * (10 ** 5)

while(hap_max - hap_min > 1):
    hap = (hap_min + hap_max) // 2
    cnt = 0
    for a in A_array:
        idx = bisect.bisect_left(A_array, hap - a)
        cnt += N - idx
    # print(hap, hap_max, hap_min, cnt)
    if cnt >= M:
        hap_min = hap
    else:
        hap_max = hap

hap = hap_min
# print(hap)
cnt_array = [0] * N
sum_array = [0] * N

for i, a in enumerate(A_array):
    idx = bisect.bisect_left(A_array, hap - a)
    cnt_array[i] = N - idx
    if idx != N:
        sum_array[idx] += 1

# print(cnt_array, sum_array)

ans = 0
cusum = 0
cntsum = 0
for a, c, s in zip(A_array, cnt_array, sum_array):
    cusum += s
    cntsum += c
    ans += a * (cusum + c)

print(ans - (cntsum - M) * hap)
