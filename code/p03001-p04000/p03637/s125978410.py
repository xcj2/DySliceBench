def f(li):
    ret = [0] * 3
    for e in li:
        if e % 4 == 0:
            ret[2] += 1
        elif e % 2 == 0:
            ret[1] += 1
        else:
            ret[0] += 1

    return ret


def solve(li):
    cnt = f(li)
    q = [1] * cnt[0] + [2] * cnt[1] + [4] * cnt[2]

    fin = []
    for i in range(len(li)):
        if i % 2:
            fin.append(q.pop())
        else:
            fin.append(q.pop(0))

    bl = True
    for i in range(len(li) - 1):
        if fin[i] * fin[i+1] % 4 != 0:
            bl = False

    print("Yes" if bl else "No")


def main():
    n = int(input())
    a = list(map(int, input().split()))

    solve(a)


if __name__ == "__main__":
    main()
