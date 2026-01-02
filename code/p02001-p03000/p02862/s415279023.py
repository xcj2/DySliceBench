
def num_combinations_mod(n, r, mod, num_max=10**6):
    # if this functions is called twice or more, init process should be placed before calling this function to
    # save time.
    if r > n:
        return 0
    elif r == n:
        return 1
    elif r < 0 or n < 0:
        return 0
    f_mod, f_mod_inv = num_combinations_mod_init(num_max, mod)
    return f_mod[n] * (f_mod_inv[r] * f_mod_inv[n-r] % mod) % mod


def num_combinations_mod_init(num_max, mod):
    factorials_mod = dict()
    factorials_mod_inv = dict()
    factorials_mod[0] = 1
    factorials_mod[1] = 1
    factorials_mod_inv[0] = 1
    factorials_mod_inv[1] = 1
    mod_inv = dict()
    mod_inv[1] = 1
    for i in range(2, num_max):
        factorials_mod[i] = factorials_mod[i - 1] * i % mod
        mod_inv[i] = mod - mod_inv[mod % i] * (mod // i) % mod
        factorials_mod_inv[i] = factorials_mod_inv[i - 1] * mod_inv[i] % mod
    return factorials_mod, factorials_mod_inv


def get(num1, num2):
    if num1 > num2:
        num = num2
    else:
        num = num1
    return num_combinations_mod(num1+num2, num, 10**9+7)


def main(X, Y):
    if (X + Y) % 3 != 0:
        return 0

    total = (X + Y) // 3
    n_moveB = (2 * X - Y) // 3
    n_moveA = total - n_moveB
    answer = get(n_moveA, n_moveB)

    return answer


X, Y = map(int, input().split(" "))
print(main(X, Y))

