import sys
import copy

def solve(N: int, A: "List[List[int]]"):
    B = copy.deepcopy(A)
    for start_node in range(0,N):
        for end_node in range(start_node+1,N):
            min_dist = 10**12
            for transit in range(N):
                if transit == start_node or transit == end_node:
                    continue
                min_dist = min(min_dist,A[start_node][transit]+A[transit][end_node])

            ## impossible
            if A[start_node][end_node] > min_dist:
                print(-1)
                return 
            elif A[start_node][end_node] == min_dist:
                B[start_node][end_node] = 0
            else:
                continue
    answer =0
    for i in range(N):
        for j in range(i+1,N):
            answer+=B[i][j]
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)

if __name__ == '__main__':
    main()
