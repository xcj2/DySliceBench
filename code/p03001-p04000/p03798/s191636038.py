def args():
    N = int(input())
    S = input()

    # print(N, S)

    return N, S


def solve(N, S):
    def inv_animal(animal):
        return "S" if animal == "W" else "W"

    def is_correct(st):
        for i in range(0, N):
            pre, nxt = i - 1, i + 1
            if i == 0:
                pre = -1
            elif i == N - 1:
                nxt = 0

            say = S[i]
            animal = st[i]

            if animal == "S":
                if say == "o":
                    if not st[pre] == st[nxt]:
                        return False
                else:
                    if st[pre] == st[nxt]:
                        return False
            else:
                if say == "o":
                    if st[pre] == st[nxt]:
                        return False
                else:
                    if not st[pre] == st[nxt]:
                        return False
        return True

    # print(S)

    lis = []
    def recur(i, st):
            if not i < 2:
                lis.append(st)
                return

            recur(i + 1, st + "S")
            recur(i + 1, st + "W")
    recur(0, "")

    # print(lis)

    if len(lis) == 0:
        return -1

    def fill(p, n):
        for i in range(1, n):
            pre = i - 1
            say = S[i]
            animal = p[i]

            if animal == "S":
                if say == "o":
                    p += p[pre]
                else:
                    p += inv_animal(p[pre])
            else:
                if say == "o":
                    p += inv_animal(p[pre])
                else:
                    p += p[pre]
        return p

    for p in lis:
        filled = fill(p, N - 1)
        if is_correct(filled):
            return filled
    return -1


if __name__ == '__main__':
    res = solve(*args())
    print(res)
