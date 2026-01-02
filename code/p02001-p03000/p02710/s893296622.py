import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def solve(N, C, AB):
    def edges_to_array(A, B, N, M):
        head = [-1] * (N + 1)
        nxt = [0] * (M + M)
        to = [0] * (M + M)
        for i in range(M):
            a = A[i]
            b = B[i]
            nxt[i << 1] = head[a]
            to[i << 1] = b
            head[a] = i << 1
            nxt[i << 1 | 1] = head[b]
            to[i << 1 | 1] = a
            head[b] = i << 1 | 1
        return head, nxt, to

    def EulerTour(head, nxt, to, root=1):
        N = len(head) - 1
        parent = [0] * (N + 1)
        ind_L = [0] * (N + 1)
        ind_R = [0] * (N + 1)
        i = -1
        tour = []
        stack = [-root, root]
        stack[0] = -root
        stack[1] = root
        while stack:
            v = stack.pop()
            tour.append(v)
            i += 1
            if v > 0:
                ind_L[v] = i
                p = parent[v]
                k = head[v]
                while k != -1:
                    w = to[k]
                    if w == p:
                        k = nxt[k]
                        continue
                    parent[w] = v
                    stack.append(-w)
                    stack.append(w)
                    k = nxt[k]
            else:
                ind_R[-v] = i
        return tour, ind_L, ind_R, parent
    head, nxt, to = edges_to_array(AB[::2], AB[1::2], N, N - 1)
    tour, ind_L, ind_R, parent = EulerTour(head, nxt, to)
    removed = [0] * (N + 1)
    answer = [N * (N + 1) // 2] * (N + 1)
    memo = [0] * (N + 1)
    for v in tour:
        if v > 0:
            memo[v] = removed[C[parent[v]]]
        else:
            v = -v
            removed[C[v]] += 1
            p = parent[v]
            x = (ind_R[v] - ind_L[v]) // 2 + 1  # subtree size
            x -= removed[C[p]] - memo[v]
            answer[C[p]] -= x * (x + 1) // 2
            removed[C[p]] += x
    for i, x in enumerate(removed):
        x = N - x
        answer[i] -= x * (x + 1) // 2
    return answer


N = int(readline())
C = (0,) + tuple(map(int, readline().split()))
AB = tuple(map(int, read().split()))
answer = solve(N, C, AB)
print('\n'.join(map(str, answer[1:])))
