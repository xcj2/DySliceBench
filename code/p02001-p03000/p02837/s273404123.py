import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = []
    xy = [[] for _ in range(n)]
    for i in range(n):
        ai = (int(sys.stdin.readline().strip()))
        a.append(ai)
        for j in range(ai):
            xij, yij = [int(s) for s in sys.stdin.readline().strip().split()]
            xy[i].append((xij-1, yij))

    # n = 3
    # xy = [[(1, 1), (2, 0)], [(2, 1), (0, 0)], [(0, 1), (1, 0)]]
    # xy = [[(1, 1)], [(0, 1)], [(1, 0)]]

    # print(a)
    # for i in range(n):
    #     print(xy[i])

    def is_possible2(state):
        honests = set()
        unkinds = set()

        for i in range(n):
            if state[i]:
                honests.add(i)
            else:
                unkinds.add(i)

        for i in range(n):
            if state[i]:
                for j in range(len(xy[i])):
                    person, is_honest = xy[i][j]
                    if is_honest:
                        if person in unkinds:
                            return False
                        honests.add(person)
                    else:
                        if person in honests:
                            return False
                        unkinds.add(person)
        return True

    state = [0] * n

    def gen_and_calc(state, pos):
        if pos == n:
            if is_possible2(state):
                return sum(state)
            return 0
        cand = gen_and_calc(state, pos+1)
        state[pos] = 1
        cand2 = gen_and_calc(state, pos+1)
        state[pos] = 0
        return max(cand, cand2)

    print(gen_and_calc(state, 0))


main()
