def read_values():
    return map(int, input().split())
 
 
def read_list():
    return list(read_values())

def main():
    mod = 10 ** 9 + 7
    N = int(input())
    A = read_list()
  
    u = {}
    for a in A:
      m = 2
      while m * m <= a:
        c = 0
        while a % m == 0:
          c += 1
          a //= m
        if c > 0:
          u[m] = max(u.get(m, 0), c)
        m += 1
      if a > 1:
        u[a] = max(u.get(a, 0), 1)

    lcm = 1
    for k, v in u.items():
      lcm *= pow(k, v, mod)
      lcm %= mod

    ans = 0
    for a in A:
      ans += lcm * pow(a, mod-2, mod)
      ans %= mod

    print(ans)

if __name__ == "__main__":
  main()