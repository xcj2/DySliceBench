import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    dic = {}
    for char in string.ascii_lowercase:
        dic[char] = float("inf")
    n = I()
    for _ in range(n):
        s = S()
        sdic = collections.Counter(s)
        for char in string.ascii_lowercase:
            dic[char] = min(dic[char], sdic[char])
    
    ans = ""
    for char in string.ascii_lowercase:
        ans += char*dic[char]
    print(ans)
main()            
