def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def S(n):
    return sum(map(int, str(n)))


def snuke(n):
    return n / S(n)


def main():
    K = ii()
    snuke_list = list(range(1, 10))

    for n in range(1, 17):
        c = 1
        while True:
            if snuke(10 ** n * c - 1) < snuke(10 ** n * (c+1) - 1):
                if not 10 ** n * c - 1 in snuke_list:
                    snuke_list.append(10 ** n * c - 1)
                c += 1
            else:
                break

    snuke_list = sorted(snuke_list)
    for i in range(K):
        print(snuke_list[i])

if __name__ == '__main__':
    main()