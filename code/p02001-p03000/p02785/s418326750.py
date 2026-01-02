import sys

def propare():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    K = int(next(tokens))
    H_list = []
    for i in range(N):
        H_list.append(int(next(tokens)))

    solve(N, K, H_list)

def solve(H: int, N: int, H_list: list):
    H_ranking_list = sorted(H_list, reverse=True)
    H_ranking_list = H_ranking_list[N:]

    count = sum(H_ranking_list)

    print(count)

    return
 
if __name__ == "__main__":
    propare()