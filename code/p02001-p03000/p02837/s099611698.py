n = int(input())


def make_remark_list(i, r):
    # -1: 不明, 0: 嘘つき, 1: 真実
    people = [-1] * n
    people[i] = 1
    for x, y in r:
        people[x - 1] = y
    return people


def check(x, y):
    new_list = []
    for a, b in zip(x, y):
        a, b = min(a, b), max(a, b)
        if (a, b) == (0, 1):
            return False
        elif (a, b) == (-1, 0):
            new_list.append(0)
        else:
            new_list.append(max(a, b))
    return new_list


remarks = []
for i in range(n):
    a = int(input())
    r = [tuple(map(int, input().split())) for _ in range(a)]
    remarks.append(make_remark_list(i, r))

def max_count(r, cnt, i = 0):
    tmp = r
    for j, r_j in enumerate(remarks):
        if j < i: continue
        if tmp[j] == 0:
            continue
        elif tmp[j] == 1:
            if check(tmp, r_j):
                tmp = check(tmp, r_j)
                cnt += 1
            else:
                cnt = 0
                break
        else:
            tmp[j] = 1
            if check(tmp, r_j):
                cnt_1, tmp_1 = max_count(tmp, cnt, j)
                tmp[j] = 0
                cnt_0, tmp_0 = max_count(tmp, cnt, j)
                if cnt_0 > cnt_1:
                    return cnt_0, tmp_0
                else:
                    return cnt_1, tmp_1
            else:
                tmp[j] = 0
    return cnt, tmp

r = [-1] * n
cnt, r = max_count(r, 0)
print(cnt)