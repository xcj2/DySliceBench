import sys

ERROR_INPUT = 'input is invalid'


def main():
    num = int(input())
    if num < 2 or 200000 < num:
        print(ERROR_INPUT)
        sys.exit(1)

    prices = [check_price(price=int(input())) for _ in range(num)]

    print(calc_max_diff(prices=prices))
    return 0


def check_price(price):
    if price < 1 or price > 10 ** 9:
        print(ERROR_INPUT)
        sys.exit(1)
    else:
        return price


def calc_max_diff(prices):
    min_price = prices[0]
    max_diff = prices[1] - prices[0]

    for p in prices[1:]:
        if max_diff < p - min_price:
            max_diff = p - min_price
        if p < min_price:
            min_price = p

    return max_diff


if __name__ == '__main__':
    main()