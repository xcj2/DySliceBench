class Price:
    ALL_DIGITS = set(list(map(str, range(10))))

    def __init__(self, required_price, disabled_digits):
        self.required_price = '0' + str(required_price)
        self.disabled_digits = set(disabled_digits)
        self.available_digits = sorted(
            list(self.ALL_DIGITS - self.disabled_digits))
        self.payed_price = required_price

    def get_greater_digit(self, digit):
        candidates = [d for d in self.available_digits if d >= digit]
        if len(candidates) == 0:
            raise ValueError
        return min(candidates)

    def get_lower_digit(self, digit):
        candidates = [d for d in self.available_digits if d <= digit]
        if len(candidates) == 0:
            raise ValueError
        return max(candidates)

    def _from_right(self):
        reversed_price = list(reversed(self.required_price))
        length = len(reversed_price)
        for i in range(length - 1):
            r = reversed_price[i]
            if r not in self.available_digits:
                try:
                    reversed_price[i] = self.get_greater_digit(r)
                except ValueError:
                    reversed_price[i] = min(self.available_digits)
                    r_next = reversed_price[i + 1]
                    reversed_price[i + 1] = chr(ord(r_next) + 1)

        r = reversed_price[-1]
        if r not in self.available_digits and r != '0':
            reversed_price[-1] = self.get_greater_digit(r)

        self.payed_price = ''.join(reversed(reversed_price))

    def _from_left(self):
        carry = False
        i = 0
        pay = list(self.payed_price)
        while i < len(pay):
            if carry:
                pay[i] = min(self.available_digits)
            else:
                carry = pay[i] > self.required_price[i]
            i += 1
        self.payed_price = ''.join(pay)

    def calculate(self):
        self._from_right()
        self._from_left()

    def get_payed_price(self):
        return int(self.payed_price)


def check(price, disabled_digits):
    p = Price(required_price=price, disabled_digits=disabled_digits)
    p.calculate()
    return p.get_payed_price()


def main():
    price, k = input().split()
    disabled_digits = input().split()
    print(check(price, disabled_digits))


if __name__ == '__main__':
    main()
