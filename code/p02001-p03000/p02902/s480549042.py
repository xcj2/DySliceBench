from collections import deque
from copy import deepcopy


# detection of a cycle
def detect_cycle(N, repn):
    color = ['WHITE'] * (N + 1)
    unfinished_vertex = set([i for i in range(1, N + 1)])
    cycle = []
    Repn = deepcopy(repn)

    def dfs(u0):
        deq = deque([u0])
        color[u0] = 'GRAY'

        while deq != deque([]) and cycle == []:
            u = deq[-1]
            if len(Repn[u]) != 0:
                v = Repn[u].popleft()
                if color[v] == 'WHITE':
                    color[v] = 'GRAY'
                    deq.append(v)
                elif color[v] == 'GRAY':
                    cycle.append(v)
            else:
                deq.pop()
                color[u] = 'BLACK'
                unfinished_vertex.remove(u)

        return deq

    while cycle == [] and unfinished_vertex != set([]):
        u = unfinished_vertex.pop()
        unfinished_vertex.add(u)
        deq = dfs(u)
        #print('deq = {}, cycle = {}'.format(deq, cycle))
    #print('deq = {}'.format(deq))
    if cycle != []:
        v = cycle.pop()
        while True:
            u = deq.pop()
            cycle.append(u)
            if u == v:
                break
        cycle.reverse()
        return cycle # cycle = [v -> ... -> u (-> v)]
    else:
        return []

# one-step minimization of a cycle
def minimize_cycle(cycle, repn):
    length = len(cycle)
    cycle_idx = {u : i for i, u in enumerate(cycle)}
    minimized = False

    for i, u in enumerate(cycle):
        if minimized == True:
            break
        else:
            for v in repn[u]:
                if v in cycle_idx.keys():
                    j = cycle_idx[v]
                    if i + 1 == j:
                        continue
                    elif i == length - 1 and j == 0:
                        continue
                    elif i < j:
                        reduced_cycle = cycle[:(i + 1)] + cycle[j:]
                        minimized = True
                        break
                    else:
                        reduced_cycle = cycle[j:(i + 1)]
                        minimized = True
                        break

    if minimized == True:
        return reduced_cycle, minimized
    else:
        return cycle, minimized


def main():
    N, M = map(int, input().split())
    repn = [deque([]) for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        repn[a].append(b)

    cycle = detect_cycle(N, repn)
    #print('cycle detected: {}'.format(cycle))
    if cycle == []:
        print(-1)
        exit()

    minimized = True
    while minimized == True:
        cycle, minimized = minimize_cycle(cycle, repn)
        #print('cycle minimized: {}, {}'.format(minimized, cycle))

    print(len(cycle))
    for u in cycle:
        print(u)


if __name__ == '__main__':
    main()
