import heapq

def main2(l, n):
    ans = 0
    lis = []
    heapq.heapify(lis)
    for i in range(1, n):
        for j in l[i]:
            heapq.heappush(lis, j)
        while len(lis) > i:
            ans += heapq.heappop(lis)
    return ans

def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    t = int(input())

    answer = []
    for _ in range(t):

        n = int(input())
        ans = 0
        l = [[] for _ in range(n+1)]
        r = [[] for _ in range(n+1)]
        for _ in range(n):
            i, j, k = map(int, input().split())
            if j > k:
                ans += j
                l[i].append(j-k)
            elif j < k:
                if i == n:
                    ans += j
                else:
                    ans += k
                    r[n-i].append(k-j)
            else:
                ans += j

        ans -= main2(l, n) + main2(r, n)
        answer.append(ans)

    for i in answer:
        print(i)

main()