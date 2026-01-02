N = int(input())
Cs = list(map(int, input().split()))
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

under_col = [0] * N
ans = [0] * N


def tri(n):
    return n * (n + 1) // 2


def go(curr, fro):
    col = Cs[curr] - 1
    prev_under = under_col[col]
    deg = 1
    for n in adj[curr]:
        if n == fro:
            continue
        curr_under = under_col[col]
        ch_deg = yield go(n, curr)
        diff_under = under_col[col] - curr_under
        ans[col] += tri(ch_deg - diff_under)
        deg += ch_deg
    under_col[col] = prev_under + deg
    return deg


def tramp(gen):
    stack = [gen]
    val = None
    while stack:
        try:
            stack.append(stack[-1].send(val))
            val = None
        except StopIteration as e:
            stack.pop()
            val = e.value
    return val


tramp(go(0, -1))
for i in range(N):
    ans[i] += tri(N - under_col[i])
    print(tri(N) - ans[i])
