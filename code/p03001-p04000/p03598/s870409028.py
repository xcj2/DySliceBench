import sys

# utils
def read_numbers():
    return [int(num) for num in sys.stdin.readline().split()]
def read_string():
    return sys.stdin.readline().rstrip('\r\n')
def list2str(*array):
    return ' '.join([str(i) for i in array])

def main(N, K, xs):
    result = 0
    for x in xs:
        result += 2*min(K-x, x)
    return result

def parse_stdin():
    # N = read_numbers()
    # data = []
    # for i in range(N):
    #    data.append(read_numbers())
    N = read_numbers()[0]
    K = read_numbers()[0]
    xs = read_numbers()
    return N, K, xs

def test_main():
    """run pytest stdin.py to test"""
    assert main(2, 9, [3, 6]) == 12

if __name__ == '__main__':
    N, K, xs = parse_stdin()
    result = main(N, K, xs)
    print(result)