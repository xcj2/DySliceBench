from math import floor
import unittest


class BiscuitGenerator:
    def __init__(self, product_count, interval_sec):
        self.product_count = product_count
        self.interval_sec = interval_sec

    def product(self, second):
        return self.product_count * floor(second / self.interval_sec)


def parse_argument(input):
    args = [int(arg) for arg in input.split(" ")]
    return args


def main(input):
    args = parse_argument(input)
    generator = BiscuitGenerator(interval_sec=args[0], product_count=args[1])
    print(generator.product(args[2]))


if __name__ == "__main__":
    main(input())