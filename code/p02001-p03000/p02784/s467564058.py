import sys

def propare():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))
    N = int(next(tokens))
    A_list = []
    for i in range(N):
        A_list.append(int(next(tokens)))

    solve(H, N, A_list)

def solve(H: int, N: int, A_list: list):
    sum_a = 0
    for a in A_list:
        sum_a = sum_a + a

    if H <= sum_a:
        print('Yes')
    else:
        print('No')

    return


 
if __name__ == "__main__":
    propare()