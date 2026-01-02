def input_from_console():
    a, b, c, d = map(int, input().split())
    return a, b, c, d

def gcd(i,j):
    i, j = max(i,j), min(i,j)
    if i % j == 0:
        return j
    else:
        while i % j !=0:
            k = i % j
            i, j = j, k
        else:
            return k

def solve(a, b, c, d):
    def how_many(to, divide):
        if to >= divide:
            n = to // divide
        else:
            n = 0
        return n
    count_by_c = how_many(b, c) - how_many(a - 1, c)
    count_by_d = how_many(b, d) - how_many(a - 1, d)
    # print('gcd', int(c*d / math.gcd(c,d)))
    count_by_cd = how_many(b, int(c*d / gcd(c,d))) - how_many(a - 1, int(c*d / gcd(c,d)))
    result = b - a + 1 - (count_by_c + count_by_d - count_by_cd)
    # print(count_by_c,  count_by_d, count_by_cd)

    # print(result)
    return result

def main():
    a, b, c, d = input_from_console()
    print(solve(a, b, c, d))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
