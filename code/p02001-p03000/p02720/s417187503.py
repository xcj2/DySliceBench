

def min_lunlun(lmd, dnum):
    # lmdが先頭にあり、最も小さいdnum桁のlunlun数をつくる
    lst = [lmd]
    for i in range(1, dnum):
        lst.append(max(0, lst[i - 1] - 1))
    return lst


def next_lunlun(lst):
    # lstから次のlunlun数を作る
    # 数を増やせる桁を確認する
    add_d = -1
    for i in reversed(range(1, len(lst))):
        if lst[i] < 9 and lst[i - 1] >= lst[i]:
            add_d = i
            break
    lst[add_d] = lst[add_d] + 1
    for i in range(add_d + 1, len(lst)):
        lst[i] = max(lst[i - 1] - 1, 0)

    return lst



def submit():
    k = int(input())

    if k < 10:
        print(k)
        return

    # d[i][j] : i始まりのj桁のルンルン数の数
    d = [[0 for _ in range(11)] for _ in range(10)]
    for x in range(10):
        d[x][1] = 1

    for j in range(1, 10):
        for i in range(10):
            if 0 <= i - 1:
                d[i][j + 1] += d[i - 1][j]
            if i + 1 < 10:
                d[i][j + 1] += d[i + 1][j]
            d[i][j + 1] += d[i][j]

    total = 0
    lmd = dnum = -1
    for j in range(1, 11):
        for i in range(1, 10):
            if total + d[i][j] >= k:
                prev_total = total
                lmd = i
                dnum = j
                break
            total += d[i][j]
        if lmd > 0:
            break

    lst = min_lunlun(lmd, dnum)
    for i in range(k - prev_total - 1):
        next_lunlun(lst)
    print("".join(map(str, lst)))
    

submit()