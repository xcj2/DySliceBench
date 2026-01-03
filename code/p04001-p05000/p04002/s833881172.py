def main():

    S = list(input())
    checklist = [0 for i in range(26)]
    for i in S:
        checklist[ord(i) - ord("a")] += 1
    ans = True

    for i in checklist:
        if i > 1:
            ans = False

    if not ans:
        print(-1)
        return 0
    else:
        ans = False
        for i in range(len(checklist)):
            if checklist[i] == 0:
                for i in S:
                    print(i, end="")
                print(chr(i + ord("a")), end = "")
                print()
                ans = True
                break

        if not ans:
            new_S = []
            for i in S:
                new_S.append(ord(i))

            for i in range(len(new_S) - 1):
                if new_S[i] > new_S[i + 1]:
                    for j in range(i - 1):
                        print(S[j], end = "")
                    print(chr(new_S[i - 1] + 1), end = "")
                    print()
                    ans = True
                    break

            if not ans:
                print(-1)
#main()

def ABC069D():

    H, W = map(int, input().split())
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        for j in range(a[i]):
            ans.append(i + 1)
    printlist = [[0 for i in range(W)] for j in range(H)]
    k = 0
    for i in range(H):
        for j in range(W):
            printlist[i][j] = ans[k]
            k += 1
        if i % 2 != 0:
            printlist[i] = printlist[i][::-1]

    for i in range(H):
        for j in range(W):
            print(printlist[i][j], end = "")
            if j != W:
                print(" ", end = "")
        print()
    print()
#ABC069D()

import math
def cc(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def ABC057D():

    N, A, B = map(int, input().split())
    v = list(map(int, input().split()))
    v = sorted(v)[::-1]

    anslist = []
    for i in range(A, B + 1):

        anslist.append([sum(v[0:i]) / i, i, v[i - 1]])
    anslist.sort()
    anslist = anslist[::-1]
    ans = anslist[0][0]
    key = anslist[0][2]
    long = anslist[0][1]
    print(ans)
    for i in range(1, len(anslist)):
        if anslist[i][0] == anslist[i - 1][0]:
            ans = anslist[i][0]
            key = anslist[i][2]
            long = anslist[i][1]
        else:
            break
    #print(anslist)
    #print(ans, key, long)
    cnt = 0
    for i in v:
        if i == key:
            cnt += 1

    c = 0
    for i in v[:long]:
        #print(i)
        if i == key:
            c += 1
    #print(c, long)
    ans = 0
    if c == long:
        for i in range(A,  min(B + 1, cnt + 1)):
            ans += cc(cnt, i)
    else:
        ans = cc(cnt, c)
    #print(anslist)
    #print(cnt, c, long)
    print(ans)
#ABC057D()

def ABC104D():
    S = list(input())
    A_cnt = 0
    B_cnt = 0
    C_cnt = 0
    Q_cnt = 0
    ans = 0
    for i in S:
        if i == "A":
            A_cnt += 1
        elif i == "B":
            B_cnt += 1
        elif i == "C":
            C_cnt += 1
        else:
            Q_cnt += 1
    for i in range(Q_cnt + 1):
        for j in range(Q_cnt - i + 1):
            k = Q_cnt - i - j
            if A_cnt + i > 0 and B_cnt + j > 0 and C_cnt + k > 0:
                f_i = math.factorial(i)
                f_j = math.factorial(j)
                f_k = math.factorial(k)
                if f_i == 0:
                    f_i = 1
                if f_j == 0:
                    f_j = 1
                if f_k == 0:
                    f_k = 1
                ans += (A_cnt + i) * (B_cnt + j) * (C_cnt + k) * math.factorial(Q_cnt) // f_i // f_j // f_k
                print(ans, i, j, k, A_cnt + i, B_cnt + j, C_cnt + k)
                print(math.factorial(Q_cnt), f_i, f_j, f_k)
    print(ans)
#ABC104D()

def ARC082D():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    if p[N - 1] == N:
        #print(p[N - 1], N)
        p[-2], p[-1] = p[-1], p[-2]
        cnt += 1

    for i in range(N - 1):
        if p[i] == i + 1:
            p[i], p[i + 1] = p[i + 1], p[i]
            cnt += 1
    print(cnt)
#ARC082D()

from queue import Queue
def ABC070D():
    N = int(input())
    a, b, c =map(int, input().split())
    Q, K = map(int, input().split())
    xy = [list(map(int, input().split())) for i in range(Q)]
    x = [[] for i in range(N)]
    for i, j in xy:
        x[i - 1].append(j - 1)
        x[j - 1].append(i - 1)

    q = Queue()
    visited = [0 for i in range(N)]

def ABC076D():
    N = int(input())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    speed_lim = [0]
    speed_list = [0 for i in range(sum(t) + 1)]
    for i in range(N):
        for j in range(t[i]):
            speed_lim.append(v[i])
    print(speed_lim)
    for i in range(1, sum(t) + 1):
        speed_list[i] = speed_list[i - 1] + 1
        if speed_list[i] > speed_lim[i]:
            speed_list[i] = speed_lim[i]
    print(speed_list)
    speed_list[-1] = 0
    for i in range(sum(t) - 1, -1, -1):
        speed_list[i] = min(speed_list[i + 1] + 1, speed_list[i])
        if speed_list[i] > speed_lim[i + 1]:
            speed_list[i] = speed_lim[i + 1]
    print(speed_list)
    ans = 0
    for i in speed_list:
        ans += i

    print(ans)
#ABC076D()

def ABC085D():
    N, H = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(N)]
    a = []
    b = []
    for i, j in ab:
        a.append(i)
        b.append(j)
    a.sort()
    b.sort()
    a = a[::-1]
    b = b[::-1]
    damage = 0
    cnt = 0
    for i in b:
        if i < a[0]:
            break
        damage += i
        cnt += 1
        if damage >= H:
            break
    key = 0
    if damage < H:
        key = (H - damage) / a[0]
        if int(key) != key:
            key += 1
        key = int(key)

    cnt += key

    print(cnt)
#ABC085D()

def ARC068D():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count_list = []
    cnt = 1
    #print(A)
    for i in range(1, N):
        if A[i] == A[i - 1]:
            cnt += 1
        else:
            count_list.append(cnt)
            cnt = 1
    count_list.append(cnt)
    ans_cnt = 0
    #print(count_list)
    for i in range(len(count_list)):
        if count_list[i] > 2:
            ans_cnt += (count_list[i] % 2) - 1
            count_list[i] %= 2
            if count_list[i] == 0:
                count_list[i] = 2
    #print(ans_cnt)
    count_list = sorted(count_list)[::-1]
    for i in range(len(count_list) - 1):
        if count_list[i] == 2 and count_list[i + 1] == 2:
            ans_cnt += 1
            count_list[i] = 1
            count_list[i + 1] = 1
    count_list = sorted(count_list)[::-1]
    if count_list[0] == 2:
        count_list[0] = 0
    #print(ans_cnt)
    #print(count_list)
    print(sum(count_list))
#ARC068D()

def ARC073D():
    N, W = map(int, input().split())
    wv = [list(map(int, input().split())) for i in range(N)]
    wv.sort()
    count_list = []
    cnt = 1
    weight_list = []
    s = 0
    g = 0
    for i in range(N - 1):
        if wv[i][0] != wv[i + 1][0]:
            g = i
            count_list.append(cnt)
            weight_list.append([wv[i][0], s, g, cnt])
            s = i + 1
            g = i + 1
            cnt = 1
        else:
            g = i
            cnt += 1

    count_list.append(cnt)
    weight_list.append([wv[-1][0], s, g, cnt])
    print(weight_list)
    wl = []
    for i in weight_list:
        this_weight = i[0]
        this_list = []
        for j in wv[i[1]:i[2] + 1]:
            this_list.append(j[1])
        this_list = sorted(this_list)[::-1]
        print(this_list)
        wl.append([this_weight, this_list])

def ARC081D():
    pattern = []
    N = int(input())
    S1 = list(input())
    S2 = list(input())
    i = 0
    while i < N:
        if S1[i] == S2[i]:
            pattern.append("X")
        else:
            pattern.append("Y")
            i += 1
        i += 1
    ans_list = []
    for i in range(len(pattern)):
        if i == 0:
            if pattern[i] == "X":
                ans_list.append(3)
            else:
                ans_list.append(6)
        else:
            if pattern[i] == "X":
                if pattern[i - 1] == "X":
                    ans_list.append(2)
                else:
                    ans_list.append(1)
            elif pattern[i] == "Y":
                if pattern[i - 1] == "X":
                    ans_list.append(2)
                elif pattern[i - 1] == "Y":
                    ans_list.append(3)
    #print(pattern)
    #print(ans_list)
    ans = 1
    for i in ans_list:
        ans *= i
    print(ans % (1000000007))
#ARC081D()

def ARC090D():
    N, M = map(int, input().split())
    LRD = [list(map(int, input().split())) for i in range(M)]
    L = []
    R = []
    D = []
    LRD.sort()
    root = [[] for i in range(N)]
    for i, j, k in LRD:
        L.append(i)
        R.append(j)
        D.append(k)
        root[i - 1].append(j - 1)
    print(root)
#ARC090D()

def ABC073D():
    N, M, R = map(int, input().split())
    r = list(map(int, input().split()))
    ABC = [list(map(int, input().split())) for i in range(M)]
    root = [[1000000000 for i in range(N)] for j in range(N)]
    for i, j, k in ABC:
        root[i - 1][j - 1] = k
        root[j - 1][i - 1] = k

    import itertools
    def kumiawase(list_name):  # list_name(リスト)のすべての並び替え
        return itertools.permutations(list_name)

    #for i in range(N):
     #   for j in range(N):
      #      for k in range(N):
       #         if root[i][j] > root[i][k] + root[k][j]:
        #            root[i][j] = root[i][k] + root[k][j]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if root[N - i - 1][N - j - 1] > root[N - i - 1][N - k - 1] + root[N - k - 1][N - j - 1]:
                    root[N - i - 1][N - j - 1] = root[N - i - 1][N - k - 1] + root[N - k- 1][N - j - 1]

    a = kumiawase(r)
    ans = float("inf")
    for i in a:
        key = 0
        for j in range(len(i) - 1):
            key += root[i[j] - 1][i[j + 1] - 1]
        if ans > key:
            ans = int(key)
    #print(root)
    print(ans)
#ABC073D()

def ARC061D():
    H, W, N = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(N)]
    ab.sort()
    tmp_list = []
    ans_list = [0 for i in range(10)]
    for x, y, in ab:
        for i in range(x - 3, x):
            for j in range(y - 3, y):
                if 0 <= i < H - 2 and 0 <= j < W - 2:
                    #print(x, y, i, j)
                    tmp_list.append([i, j])
    #print(tmp_list)
    tmp_list.sort()
    temp = 1
    #print(tmp_list)
    cnt = 0
    for i in range(1, len(tmp_list) + 1):
        if i != len(tmp_list):
            if tmp_list[i] == tmp_list[i - 1]:
                temp += 1
            else:
                ans_list[temp] += 1
                temp = 1
                cnt += 1
        else:
            ans_list[temp] += 1
            cnt += 1
    #print(ans_list)

    key = 0
    for i in range(len(ans_list)):
        key += i * ans_list[i]
    ans_list[0] = (H - 2) * (W - 2) - cnt
    #print(key)
    #print((H - 2) * (W - 2) - key)

    for i in range(10):
        print(ans_list[i])

ARC061D()
