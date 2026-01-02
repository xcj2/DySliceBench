import sys, heapq
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
  
def solve():
    Q = int(single_input())
    n, a, b = map(int, line_input())
    left, right = [-a], [a]
    heapq.heapify(left)
    heapq.heapify(right)
    minans =  b
    ans = ""
    for i in range(1, Q):
        queri = [int(i) for i in line_input()]
        if queri[0] == 1:
            a, b = queri[1:]
            minans += b
            if -1 * left[0] <= a <= right[0]:
                heapq.heappush(left, -a)
                heapq.heappush(right, a)
            elif a < -1 * left[0]:
                minans += (-1 * left[0]) - a
                heapq.heappush(left, -a)
                heapq.heappush(left, -a)
                heapq.heappush(right, -1 * heapq.heappop(left))
            else:
                minans += a - right[0]
                heapq.heappush(left, -1 * heapq.heappop(right))
                heapq.heappush(right, a)
                heapq.heappush(right, a)
        else: ans += str(-1 * left[0]) + " " + str(minans) + "\n"
    print(ans)

    return 0
  
if __name__ == "__main__":
    solve()