# coding: utf-8
def getLnInputs():
    return input().split()


def getLnIntInputs():
    return list(map(int, getLnInputs()))


def main():
    N, C, K = getLnIntInputs()

    a_queue = []
    bus_count = 0
    for _ in range(N):
        a_queue.append(int(input()))

    a_queue = sorted(a_queue)
    p_queue = []

    for i in range(N):
        t = a_queue[i]
        if len(p_queue) != 0 and t - p_queue[0] > K:
            p_queue = [t]
            bus_count += 1
            continue

        p_queue.append(t)

        if len(p_queue) == C:
            p_queue = []
            bus_count += 1

    if len(p_queue):
        bus_count += 1

    print(bus_count)
    return


main()
