
class Num:
    def __init__(self, h, t, d):
        self.head = h
        self.tail = t
        self.digit = d
        self.min = self.get_min()
        self.max = self.get_max()

    def get_min(self):
        if self.digit == 1:
            if self.head == self.tail:
                return self.head
            else:
                return 0
        else:
            return self.head * (10 ** (self.digit-1)) + self.tail

    def get_max(self):
        if self.digit == 1:
            if self.head == self.tail:
                return self.head
            else:
                return 0
        if self.digit == 2:
            return self.get_min()
        else:
            return self.get_min() + (10 ** (self.digit-1) - 10)


def solve(a, b, n):
    if a.min * a.max * b.min * b.max == 0:
        return 0

    if a.min > n:
        return 0

    if b.min > n:
        return 0

    if a.max > n:
        if a.digit >= 3:
            if str(a.max)[-1] > str(n)[-1]:
                a.max = int(str(a.max)[0] + str(n-10)[1:-1] + str(a.max)[-1])
            else:
                a.max = int(str(a.max)[0] + str(n)[1:-1] + str(a.max)[-1])

    if b.max > n:
        if b.digit >= 3:
            if str(b.max)[-1] > str(n)[-1]:
                b.max = int(str(b.max)[0] + str(n-10)[1:-1] + str(b.max)[-1])
            else:
                b.max = int(str(b.max)[0] + str(n)[1:-1] + str(b.max)[-1])

    total_a = (a.max - a.min) // 10 + 1
    total_b = (b.max - b.min) // 10 + 1
    count = total_a * total_b

    # print('------')
    # print(a.min, a.max)
    # print(b.min, b.max)
    # print(count)

    return count


def main():
    n = int(input())
    digit_n = len(str(n))

    total = 0
    for a_head in range(1, 10):
        for a_tail in range(1, 10):

            b_head = a_tail
            b_tail = a_head

            for digit_a in range(1, digit_n+1):
                for digit_b in range(1, digit_n+1):
                    a = Num(a_head, a_tail, digit_a)
                    b = Num(b_head, b_tail, digit_b)
                    count = solve(a, b, n)
                    total += count

    print(total)


if __name__ == '__main__':
    main()
