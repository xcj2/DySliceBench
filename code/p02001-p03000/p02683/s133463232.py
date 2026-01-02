# import sys
# input = sys.stdin.readline
import itertools

# 持っているビスケットを叩き、1枚増やす
# ビスケット A枚を 1円に交換する
# 1円をビスケット B枚に交換する
def main():
    n, m, x = input_list()
    books = {}
    contents = {}
    for i in range(n):
        c = input_list()
        books[i] = c[0]
        contents[i] = c[1:m+1]

    if n == 1:
        if sum(contents[0]) >= x:
            print(books[0])
        else:
            print(-1)
        exit()

    ans = []
    for v in itertools.product([0, 1], repeat=n):
        understands = [0] * m
        ok = [False] * m
        a = 0
        for i, vi in enumerate(v):
            if vi == 0:
                continue
            for index, val in enumerate(contents[i]):
                understands[index] += val
                if understands[index] >= x:
                    ok[index] = True
            a += books[i]
        if all(ok):
            ans.append(a)

    if len(ans) > 0:
        print(min(ans))
    else:
        print(-1)
        # a = 0
        # for vi in v:
        #     for index, val in enumerate(contents[vi]):
        #         understands[index] += val
        #         if understands[index] >= x:
        #             ok[index] = True
        #     a += books[vi]
        # if all(ok):
        #     ans.append(a)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
