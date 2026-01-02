import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import math 
def main():
    A, B = map(int, readline().split())
    def gcd(x, y):
        if not x%y:
            return y
        return gcd(y, x%y)
    
    def factorize(x):
        res = []
        for i in range(2, int(math.sqrt(x))+1):
            if x%i != 0:
                continue
            cnt = 0
            while x%i == 0:
                x //= i
                cnt += 1 
            res.append((i, cnt))
        if x != 1:
            res.append((x, 1))
        return res

    print(len(factorize(gcd(A, B)))+1) 
if __name__ == '__main__':
    main()
