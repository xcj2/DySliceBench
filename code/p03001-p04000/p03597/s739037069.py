import sys

# utils
def read_numbers():
    return [int(num) for num in sys.stdin.readline().split()]
def read_string():
    return sys.stdin.readline().rstrip('\r\n')
def list2str(*array):
    return ' '.join([str(i) for i in array])

def main(N, A):
    return N*N - A

def parse_stdin():
    # N = read_numbers()
    # data = []
    # for i in range(N):
    #    data.append(read_numbers())
    N = read_numbers()[0]
    A = read_numbers()[0]
    return N, A

def test_main():
    """run pytest stdin.py to test"""
    #assert main([1,2], 'hi') == '3 hi'
    pass

if __name__ == '__main__':
    N, A = parse_stdin()
    result = main(N, A)
    print(result)