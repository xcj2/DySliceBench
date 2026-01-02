import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    n, k = mi()
    p = list(map(lambda x: int(x)-1, input().split()))
    c = li()
    ans = -10**18
    for i in range(n):
        v = i
        cycle_cnt = 0
        cycle_sum = 0
        while True:
            cycle_cnt += 1
            cycle_sum += c[v]
            v = p[v]
            if v == i:
                break
        
        cnt = 0
        tmp = 0
        while True:
            tmp += c[v]
            cnt += 1
            if cnt > k:
                break
            r = (k-cnt)//cycle_cnt
            score = tmp+r*max(0, cycle_sum)
            ans = max(ans, score)
            v = p[v]
            if v == i:
                break
    print(ans)



if __name__ == '__main__':
    main()