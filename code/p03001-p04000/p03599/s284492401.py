import sys

# utils
def read_numbers():
    return [int(num) for num in sys.stdin.readline().split()]
def read_string():
    return sys.stdin.readline().rstrip('\r\n')
def list2str(*array):
    return ' '.join([str(i) for i in array])

def main(nums):
    A, B, C, D, E, F = nums
    def density(sugar, water):
        if sugar + water == 0:
            return 0.0
        return sugar / (sugar + water)
    cache = {}
    def recurse(sugar, water):
        if (sugar, water) in cache:
            return cache[(sugar, water)]
        if sugar + water > F:
            return (0.0, 0, 0)
        if density(sugar, water) > density(E, 100):
            return (0.0, 0, 0)
        result = max(
            (density(sugar, water), sugar, water),
            recurse(sugar, water+100*A),
            recurse(sugar, water+100*B),
            recurse(sugar+C, water),
            recurse(sugar+D, water),
        )
        cache[(sugar, water)] = result
        return result
    dens, sugar, water = recurse(0,0)
    return "%d %d" % (sugar+water, sugar)




def parse_stdin():
    # N = read_numbers()
    # data = []
    # for i in range(N):
    #    data.append(read_numbers())
    nums = read_numbers()
    return nums

def test_main():
    """run pytest stdin.py to test"""
    assert main([17, 19, 22, 26, 55, 2802]) == "2634 934"

if __name__ == '__main__':
    nums = parse_stdin()
    result = main(nums)
    print(result)