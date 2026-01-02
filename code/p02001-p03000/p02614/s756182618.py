def main():
    height, width, leave_black = [int(x) for x in input().split()]
    table = [input() for _ in range(height)]

    def bit_patterns(height, width):
        for num_h in range(2 ** height):
            for num_w in range(2 ** width):
                yield num_h, num_w

    def count_black(height, width, num_h, num_w):
        for bit_h in range(height):
            for bit_w in range(width):
                if num_h >> bit_h & 1 or num_w >> bit_w & 1:
                    continue
                yield table[bit_h][bit_w] == '#'

    def black_matched(height, width):
        for ii, jj in bit_patterns(height, width):
            yield sum(count_black(height, width, ii, jj)) == leave_black

    print(sum(black_matched(height, width)))


if __name__ == '__main__':
    main()
