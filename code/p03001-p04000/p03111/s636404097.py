

from collections import deque


def submit():
    n, a, b, c = map(int, input().split())
    llist = [int(input()) for _ in range(n)]

    def update(st, h):
        return st[0] + h, st[1] + 1

    def cost(st, goal):
        return (st[1] - 1) * 10 + abs(goal - st[0])

    def rec_search(ast, bst, cst, rest):
        # 処理し終わった
        if not rest:
            if ast[1] == 0 or bst[1] == 0 or cst[0] == 0:
                return float('inf')
            else:
                return cost(ast, a) + cost(bst, b) + cost(cst, c)
        else:
            head = rest[0]
            rest = rest[1:]

            # headをAに使う
            acost = rec_search(update(ast, head), bst, cst, rest)
            # headをBに使う
            bcost = rec_search(ast, update(bst, head), cst, rest)
            # headをCに使う
            ccost = rec_search(ast, bst, update(cst, head), rest)
            # headを使わない
            ncost = rec_search(ast, bst, cst, rest)

            return min(acost, bcost, ccost, ncost)


    # それぞれl合計、個数を保存
    ast = (0, 0)
    bst = (0, 0)
    cst = (0, 0)
    
    cost = rec_search(ast, bst, cst, llist)
    print(cost)


if __name__ == "__main__":
    submit()