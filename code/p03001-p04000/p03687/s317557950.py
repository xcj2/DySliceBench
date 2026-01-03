import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    s = list(s)
    blen = len(s)
    same = len(s) == s.count(s[0])
    ans = float("inf")
    dic = collections.Counter(s)
    chars = dic.keys()

    if same:
        ans = 0
    elif not same:
        for char in chars:
            same = False
            bs = copy.copy(s)
            while not same:
                same = True
                for i in range(1,len(bs)):
                    if bs[i-1] == char and bs[i] == char:
                        pass
                    elif bs[i-1] == char or bs[i] == char:
                        bs[i-1] = char
                    else:
                        same = False
                bs.pop()
            cnt = blen - len(bs)
            ans = min(ans,cnt)
    print(ans)
main()            
