
def main():

    N, M = map(int, input().split())

    lights = []
    for _ in range(M):
        ary = [int(v) - 1 for v in input().split()]
        lights.append(ary[1:])

    P = [int(v) for v in input().split()]

    def is_on(state):
        for i, sw in enumerate(lights):
            on = 0
            for j in sw:
                if state & (1 << j) != 0:
                    on += 1
            if (on % 2) != P[i]:
                return False
        return True

    def search(i, state):
        if i == N:
            ok = 1 if is_on(state) else 0
            return ok

        c = 0
        c += search(i+1, state)
        c += search(i+1, state | (1 << i))
        return c

    print(search(0, 0))


main()
