import sys
from collections import deque
input = sys.stdin.readline


def gen_hash(panel):
    _hash = ""
    for i in range(3):
        for j in range(3):
            _hash += str(panel[i][j])
    return _hash


def get_matchings(_hash):
    ans = "123456780"
    cnt = 0
    for i in range(9):
        if _hash[i] == str(ans[i]):
            cnt += 1
    return cnt


def bfs(panel):
    swap_candidates = {
        0: (1, 3),
        1: (0, 2, 4),
        2: (1, 5),
        3: (0, 4, 6),
        4: (1, 3, 5, 7),
        5: (2, 4, 8),
        6: (3, 7),
        7: (4, 6, 8),
        8: (5, 7)
    }
    dq = deque()
    dq.append((gen_hash(panel), 0))
    seen = set()
    seen.add(gen_hash(panel))
    while dq:
        _hash, cnt = dq.popleft()
        if get_matchings(_hash) == 9:
            return cnt
        z_ptr = _hash.index("0")
        for n_ptr in swap_candidates[z_ptr]:
            next_hash = list(_hash)
            next_hash[z_ptr], next_hash[n_ptr] = next_hash[n_ptr], next_hash[z_ptr]
            next_hash = "".join(next_hash)
            if next_hash not in seen:
                seen.add(next_hash)
                dq.append((next_hash, cnt + 1))


panel = []
for _ in range(3):
    panel.append([int(i) for i in input().split()])

ans = bfs(panel)
print(ans)

