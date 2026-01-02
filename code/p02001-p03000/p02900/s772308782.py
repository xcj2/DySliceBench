# coding: utf-8
# Your code here!
def main():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def divisor(n):
        ass = []
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                ass.append(i)
                if i**2 == n:
                    continue
                ass.append(n//i)
        return ass
    
    def is_prime(n):
        if n == 1:
            return True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    a,b=map(int,input().split())
    c=gcd(a,b)
    cnt=0
    d=divisor(c)
    for i in d:
        if is_prime(i):
            cnt+=1
    print(cnt)
    
if __name__ == "__main__":
    main()
