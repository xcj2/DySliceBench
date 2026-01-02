def bubble_sort(r, n):
    flag = True  # ??£??\????´?????????¨????????°
    while flag:
        flag = False
        for i in range(n - 1, 0, -1):
            if r[i - 1][1] > r[i][1]:
                r[i - 1], r[i] = r[i], r[i - 1]
                flag = True
    return r


def select_sort(r, n):
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if r[j][1] < r[minj][1]:
                minj = j
        if i != minj:
            r[i], r[minj] = r[minj], r[i]
    return r


def stable_sort(r, sort_r):
    for i in range(len(r)):
        for j in range(i + 1, len(r)):
            for a in range(len(sort_r)):
                for b in range(a + 1, len(sort_r)):
                    if r[i][1] == r[j][1] and r[i] == sort_r[b] and r[j] == sort_r[a]:
                         return "Not stable"

    return "Stable"


N = int(input())
R = list(input().split())
C = R[:]
BS_R = bubble_sort(R, N)
SS_R = select_sort(C, N)
print(*BS_R)
print(stable_sort(R, BS_R))
print(*SS_R)
print(stable_sort(R, SS_R))