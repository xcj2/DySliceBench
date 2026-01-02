import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

#素因数分解を行う関数O(root(N))
#int -> list
def factorize(x):
      res = []
      for i in range(2, int(x**0.5)+1):
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
 
def f(x):
    l = 0     
    r = 1000
    while r-l>1:
        c = (r+l)//2
        if x >= c*(c+1)//2:
            l = c
        else:
            r = c
    return l 
def main():
    n = int(readline())    
    fact = factorize(n)     
    ans = 0
    for i, j in fact:
        ans += f(j)
    print(ans)
if __name__ == '__main__':
    main()
