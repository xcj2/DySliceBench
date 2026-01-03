import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
def divc(x,y) -> int: return -(-x//y)
def divf(x,y) -> int: return x//y
def gcd(x,y):
    while y: x,y = y,x%y
    return x
def lcm(x,y): return x*y//gcd(x,y)
import itertools as it
#======================================================#
def main():
    s = IS()
    n = len(s)

    def calc(bits):
        sumv = 0
        for i in range(len(bits)-1):
            sumv += int(s[bits[i]:bits[i+1]])
        return sumv

    ans = 0
    for bit in range(1<<(n-1)):
        bits = [0]
        for i in range(n-1):
            if bit&(1<<i):
                bits.append(i+1)
        bits += [n]
        ans += calc(bits)
    print(ans)

if __name__ == '__main__':
    main()