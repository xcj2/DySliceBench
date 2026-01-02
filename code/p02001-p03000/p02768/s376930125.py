import functools

def get_mul_inverse(x: int, p: int) -> int:
    return iterative_square(x, p - 2, p)

def _iterative_square(x: int, n: int, p: int) -> int:
    if n <= 1:
        return x
    div, mod = divmod(n, 2)
    return (((iterative_square(x, div, p) ** 2) % p) * x ** mod) % p

def iterative_square(x: int, n: int, p: int) -> int:
    if n <= 0:
        return None

    return _iterative_square(x, n, p)

def factorial(a, b, p):
  x = 1

  x = functools.reduce(lambda x, y: (x * y) % p, range(a, b + 1), 1)
  return x

def com(n, r, p):
  fact_div_r = get_mul_inverse(factorial(1, r, p), p)

  _result = factorial(n - r + 1, n, p)
  result = (_result * fact_div_r) % p
  
  return result


n, a, b = [int(i) for i in input().split()]
p = 10**9 + 7


pow_2_n_1 = iterative_square(2, n, p) - 1

_result = pow_2_n_1 - com(n, a, p)

_result = _result - com(n, b, p)

result = _result % p
print(result)