class Solution(object):
    def __init__(self):
        pass
        
    def Sol(self, n, k, r):
        fq = dict([(i, 0) for i in range(0, n + 1)]) 
        t = 0
        for _r in r:
            fq[_r] += 1
            t += 1
        
        player = [k for i in range(0, n)]
        for i in range(0, n):
            player[i] = k - t + fq[i + 1]
        return player


def main():
    info = [int(e) for e in input().split()]
    r = []
    for _ in range(0, info[2]):
        r.append(int(input()))
    pl = Solution().Sol(info[0], info[1], r)
    for sc in pl:
        if sc <= 0:
            print('No')
        else:
            print('Yes')
    return 0

if __name__ == "__main__":
    main()