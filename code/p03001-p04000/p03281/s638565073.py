#関数リスト
import sys
input = sys.stdin.readline


def RD(): return input().rstrip()
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    num = I()
    result = 0
    for i in range(1,num+1,2):
        temp = len(make_divisors(i))
        if temp == 8:
            result += 1
    print(result)
        
if __name__ == "__main__":
    main()