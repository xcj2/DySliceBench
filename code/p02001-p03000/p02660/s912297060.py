def main():
    def factorization(num):
        result = []
        count = 0
        temp = num
        for i in range(2, int(num ** 0.5) + 1):
            if temp % i == 0:
                count = 0
                while temp % i == 0:
                    count += 1
                    temp /= i
                result.append(count)
        if temp != 1:
            result.append(1)
        return result
    C = []
    c = 0
    for i in range(1, 40):
        c += i
        C.append(c)
    def combi(num, C):
        for i, c in enumerate(C):
            if num < c:
                return i
        return -1
    n = int(input())
    exps = factorization(n)
    count = 0
    for e in exps:
        count += combi(e, C)
    print(count)


if __name__ == '__main__':
    main()
