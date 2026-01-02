def f(s):
    if s == "A":
        return A
    elif s == "B":
        return B
    elif s == "C":
        return C


def inc(s):
    global A, B, C

    if s == "A":
        A += 1
    elif s == "B":
        B += 1
    elif s == "C":
        C += 1


def dec(s):
    global A, B, C

    if s == "A":
        A -= 1
    elif s == "B":
        B -= 1
    elif s == "C":
        C -= 1


N, A, B, C = map(int, input().split())

if A + B + C == 0:
    print("No")

elif A + B + C == 1:
    ans = []
    for _ in range(N):
        s = input()
        if f(s[0]) == f(s[1]) == 0:
            print("No")
            exit()
        else:
            if f(s[0]) == 1:
                ans.append(s[1])
                dec(s[0])
                inc(s[1])
            elif f(s[1]) == 1:
                ans.append(s[0])
                inc(s[0])
                dec(s[1])
    print("Yes")
    for i in range(N):
        print(ans[i])

elif A + B + C >= 2:
    s = []
    for i in range(N):
        s.append(input())

    # 共に0を選ぶことは初手でしか起こり得ない
    # 2回目以降は、0は1個以下
    if f(s[0][0]) == f(s[0][1]) == 0:
        print("No")
        exit()

    ans = []
    for i in range(len(s)):
        if f(s[i][0]) >= 1 and f(s[i][1]) == 0:
            ans.append(s[i][1])
            dec(s[i][0])
            inc(s[i][1])
        elif f(s[i][0]) == 0 and f(s[i][1]) >= 1:
            ans.append(s[i][0])
            inc(s[i][0])
            dec(s[i][1])
        # (1,1,0)の状態で(1,1)を選んだ時 and 最後の手ではない and 次に違う手が予定されている
        elif (A + B + C == 2) and (f(s[i][0]) == f(s[i][1]) == 1) and (i < N - 1):
            # s[i][0]を次に操作する場合
            if s[i][0] == s[i + 1][0] or s[i][0] == s[i + 1][1]:
                ans.append(s[i][0])
                inc(s[i][0])
                dec(s[i][1])
            # s[i][1]を次に操作する場合
            elif s[i][1] == s[i + 1][0] or s[i][1] == s[i + 1][1]:
                ans.append(s[i][1])
                dec(s[i][0])
                inc(s[i][1])
        else:
            if f(s[i][0]) <= f(s[i][1]):
                ans.append(s[i][0])
                inc(s[i][0])
                dec(s[i][1])
            else:
                ans.append(s[i][1])
                inc(s[i][1])
                dec(s[i][0])

    print("Yes")
    # print(ans)
    for i in range(N):
        print(ans[i])
