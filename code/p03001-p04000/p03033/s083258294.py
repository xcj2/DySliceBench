import sys, collections, heapq
def single_input(F): return F.readline().strip("\n")
def line_input(F): return F.readline().strip("\n").split()

def solve():
    F = sys.stdin
    N, Q = map(int, line_input(F))
    event = []
    for i in range(N):
        s, t, x = map(int, line_input(F))
        event.append((s-x, 1, x))
        event.append((t-x,-1, x))
    for i in range(Q):
        d = int(single_input(F))
        event.append((d, 2, d))
    event.sort()
    candidate = []
    heapq.heapify(candidate)
    stop = collections.defaultdict(int)
    ans = ""
    for time, parameter, co in event:
        if parameter == 1:
            heapq.heappush(candidate, co)
            stop[co] += 1
        elif parameter == -1:
            stop[co] -= 1
        else:
            while candidate:
                x = heapq.heappop(candidate)
                if stop[x] > 0:
                    heapq.heappush(candidate, x)
                    ans += str(x) + "\n"
                    break
            else: ans += "-1\n"
    print(ans)

    return 0

if __name__ == "__main__":
    solve()