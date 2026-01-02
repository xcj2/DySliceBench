
def mCk(m, k):
  if k == 3:
    return m * (m - 1) * (m - 2) // 6
  elif k == 2:
    return m * (m - 1) // 2
  elif k == 1:
    return m
  return None

def count_up(n, k):
  digit_n = len(n)
  if digit_n < k: #桁不足
    return 0
  top_n = int(n[0])
  if k == 1:
    return (top_n + 9 * (digit_n - 1))
  return (
    count_up(str(int(n[1:])), k - 1) 
    + (top_n - 1) * mCk(digit_n - 1, k - 1) * (9 ** (k - 1))
    + mCk(digit_n - 1, k) * (9 ** k)
  )


def main():
  n = input() 
  k = int(input())
  print(count_up(n, k))

if __name__ == "__main__":
  main()