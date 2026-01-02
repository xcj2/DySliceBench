#!/usr/bin/env python3
import sys
INF = float("inf")
# import matplotlib.pyplot as plt


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    red = [[a[i], b[i], False] for i in range(N)]
    blue = [[c[i], d[i], False] for i in range(N)]

    red.sort(key=lambda x: x[0], reverse=True)
    blue.sort(key=lambda x: x[0])

    # print(red)
    # print(blue)
    ans = 0

    for b in blue:
        cand = [i for i, r in enumerate(red) if r[0] < b[0] and r[1] < b[1]]
        # fix
        if len(cand) > 0:
            ans += 1
            i = max(cand, key=lambda i: red[i][1])
            red.pop(i)
    print(ans)

    # flag = True
    # while flag:
    #     flag = False
    #     for i in range(N):
    #         if red[i][2] == True:
    #             continue
    #         cand = []
    #         counter = 0
    #         for j in range(N):
    #             if blue[j][2] == True:
    #                 continue
    #             if red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
    #                 counter += 1
    #                 cand.append(j)
    #         if counter == 1:
    #             red[i][2] = True
    #             blue[cand[0]][2] = True
    #             flag = True
    #             ans += 1
    #             print("pair ", red[cand[0]], blue[cand[0]])
    # print(ans)
    # for i in range(N):
    #     if red[i][2]:
    #         plt.scatter(red[i][0], red[i][1], color="red", marker="o")
    #     else:
    #         plt.scatter(red[i][0], red[i][1], color="orange", marker="o")
    # for i in range(N):
    #     if blue[i][2]:
    #         plt.scatter(blue[i][0], blue[i][1], color="blue", marker="o")
    #     else:
    #         plt.scatter(blue[i][0], blue[i][1], color="navy", marker="o")
    # plt.show()
    # return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, a, b, c, d)


if __name__ == '__main__':
    main()
