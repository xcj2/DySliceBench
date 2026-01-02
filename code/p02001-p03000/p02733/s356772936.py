"""
NTC here
"""
import sys
inp = sys.stdin.readline


def input(): return inp().strip()


flush = sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**25)


def iin(): return int(input())


def lin(): return list(map(int, input().split()))

# range = xrange
# input = raw_input


def main():
    def cnt_ones(n):
        ch = 0
        x = n
        ans = []
        while x:
            if x&1:
                ans.append(ch)
            x>>=1
            ch+=1
        return ans
    ans = []
    h, w, K = lin()
    a = [list(map(int, list(input()))) for _ in range(h)]
    h1 = 2**(h-1)
    for i in range(h1):
        ch = cnt_ones(i)+[h-1]
        l1 = len(ch)
        a1 = [0]*(l1)
        ch2 = 0
        for j in range(w):
            ch1 = 0
            a2 = [0]*(l1)
            for k in range(h):
                a2[ch1]+=a[k][j]
                if ch[ch1]==k:
                    ch1+=1
            for k in range(l1):
                if a1[k]+a2[k]>K:
                    ch2 += 1
                    a1 = a2[:]
                    break
            else:
                for k in range(l1):
                    a1[k]+=a2[k]
            #check
            for i in a1:
                if i>K:
                    ch2 = w*10
                    break
            else:
                continue
            break
        ans.append(l1-1+ch2)
    # print(ans)
    print(min(ans))

"""
TEST-
4 4 1
1111
1111
1111
1111
"""


main()
# threading.Thread(target=main).start()
