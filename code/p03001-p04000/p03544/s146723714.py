import sys

def solve(n):
    print(luca(n))
    # print(luca_other(n))

def luca(n):
    result = [0 for i in range(n+1)]
    result[0] = 2
    result[1] = 1
    for i in range(2,n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

def luca_other(n):
    if n == 0:
        return 2
    (x, y) = (2, 1)
    for i in range(n-1):
        (x, y) = (y, x + y)
    return y

def readQuestion():
    ws = sys.stdin.readline().strip().split()
    n = int(ws[0])
    return (n,)

def main():
    solve(*readQuestion())

# Uncomment before submission
main()
