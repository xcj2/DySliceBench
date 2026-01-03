import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        a,b=map(int,input().split())
        if a==0 or b==0:
            return 'Zero'
        if a<0 and b>0:
            return 'Zero'
        else:
            if a<0 and b<0:
                if (b-a)%2==0:
                    return 'Negative'
                else:
                    return 'Positive'
            else:
                if a%2==0:
                    return 'Negative'
                else:
                    return 'Positive'
    print(main())
resolve()
