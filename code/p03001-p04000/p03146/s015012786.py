MAX_RANGE = 99999999999

def f(n:float):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

def main():
    s = float(input().strip())

    def a(i):
        if i < 1:
            raise ValueError
        elif i == 1:
            return s
        else:
            return f(a(i-1))

    a_s = [None, s]
    for i in range(2, MAX_RANGE):  # 1 .. MAX_RANGE-1
        value = a(i)
        for j in range(1, i):  # 1 .. i-1
            if a_s[j] == value:
                print(i)
                return
        a_s.append(value)

    # print(a_s)


if __name__ == "__main__":
    main()