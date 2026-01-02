from heapq import heappush, heappop, merge
from collections import defaultdict
import sys
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()

def solve():
    N, Q = map(int, line_input())
    events = []
    for _ in range(N):
        s, t, x = map(int, line_input())
        events.append((s-x, 1, x))
        events.append((t-x, -1, x))
    for _ in range(Q):
        d = int(single_input())
        events.append((d, 2, d))
    events = sorted(events)

    constructions = []
    under_construction = defaultdict(bool)
    ans = ''
    for _, flag, coord in events:
        if flag == 1:
            heappush(constructions, coord)
            under_construction[coord] = True
        elif flag == -1:
            under_construction[coord] = False
        else:
            while constructions:
                x = heappop(constructions)
                if under_construction[x]: # x is the minimum coordinate under construction
                    heappush(constructions, x)
                    ans += str(x) + '\n'
                    break
            else: # no constructions
                ans += '-1\n'
    print(ans)
    
if __name__ == "__main__":
    solve()