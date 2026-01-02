import sys
input = sys.stdin.readline

 
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    n, y = MI()
    result = "-1 -1 -1"
    for i in range(n, -1, -1):
        a = i * 10000
        if a <= y:
            for j in range(n-i, -1, -1):
                b = a + j * 5000
                if b <= y:
                    if b + 1000 * (n-i-j) == y:
                        result = str(i)+" "+str(j)+" "+str(n-i-j)
                        print(result)
                        sys.exit()
    print(result)

main()