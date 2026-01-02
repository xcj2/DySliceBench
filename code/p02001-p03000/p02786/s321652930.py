from itertools import count


def main():
    H = int(input())
    for i in count():
        if 2 ** i > H:
            print(2**i-1)
            exit()


def test():
    for H in range(1, 101):
        monster = [H]
        ans = 0
        while len(monster) > 0:
            tmp = list()
            for m in monster:
                if m != 1:
                    tmp.extend([m//2]*2)
                ans += 1
            monster = tmp
        print(ans)


def test2():
    H = 10 ** 12
    ans = 0
    while H > 1:
        H //= 2
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
