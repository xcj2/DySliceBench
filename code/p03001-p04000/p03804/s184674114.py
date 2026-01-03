def read():
    return int(input())

def reads(sep=None):
    return list(map(int, input().split(sep)))

def check(i, j, a, b):
    for x in range(len(b)):
        for y in range(len(b)):
            if a[i+x][j+y] != b[x][y]:
                return False
    return True

def main():
    n, m = reads();
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if check(i, j, a, b):
                print('Yes')
                return
    print('No')
 
main()
