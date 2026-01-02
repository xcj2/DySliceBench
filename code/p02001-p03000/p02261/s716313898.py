def chk_stable(re):
    for i in range(N-1):
        re_chk = list()
        re_chk.append(re[i])
        for j in range(i+1, N):
            if int(re[i][1]) == int(re[j][1]):
                re_chk.append(re[j])
        if len(re_chk) >= 2:
            for j in range(1, len(re_chk)):
                if A.index(re_chk[j]) < A.index(re_chk[j-1]):
                    return 'Not stable'
    return 'Stable'


def bubble():
    b_list = [i for i in A]
    flag = True
    while flag:
        flag = False
        for i in reversed(range(1, N)):
            if int(b_list[i][1]) < int(b_list[i-1][1]):
                tmp = b_list[i]
                b_list[i] = b_list[i-1]
                b_list[i-1] = tmp
                flag = True
    print(' '.join(b_list))
    return chk_stable(b_list)


def selection():
    s_list = [i for i in A]
    for i in range(N):
        min_i = i
        for j in range(i, N):
            if int(s_list[min_i][1]) > int(s_list[j][1]):
                min_i = j
        tmp = s_list[i]
        s_list[i] = s_list[min_i]
        s_list[min_i] = tmp
    print(' '.join(s_list))
    return chk_stable(s_list)


N = int(input())
A = list(input().split())

print(bubble())
print(selection())

