def digits_to_number(digits):
    res = 0
    for d in reversed(digits):
        res *= 10
        res += d
    return res


def next_lunlun(n):
    digits = []
    x = n
    while x > 0:
        digits.append(x % 10)
        x //= 10
    for i in range(0, len(digits)-1):
        if digits[i] <= digits[i+1] and digits[i] != 9:
            digits[i] += 1
            for j in range(i-1, -1, -1):
                digits[j] = max(digits[j+1] - 1, 0)
            return digits_to_number(digits)
    if digits[-1] == 9:
        digits = [0] * len(digits)
        digits.append(1)
        return digits_to_number(digits)
    digits[-1] += 1
    for j in range(len(digits)-2, -1, -1):
        digits[j] = max(digits[j+1] - 1, 0)
    return digits_to_number(digits)


def kth_lunlun(k):
    lunlun = 1
    for i in range(0, k-1):
        lunlun = next_lunlun(lunlun)
    return lunlun

if __name__ == '__main__':
    k = int(input())
    print(kth_lunlun(k))
