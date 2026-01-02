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
 
def main():
    n = int(readline())
    if n == 1:
        print(0)
        return
    fact = factorize(n)
    num = [int(i) for i in range(50)]
    def f(x):
        i = 2
        j = 2
        cnt = 1
        while 1:
            if x<=i:
                break
            cnt += 1
            j += 1
            i += j
        return cnt 
    ans = 0
    for i, j in fact:
        ans += f(j)
    print(ans)
if __name__ == '__main__':
    main()
