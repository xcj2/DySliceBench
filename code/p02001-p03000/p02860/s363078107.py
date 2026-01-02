import sys

def propare():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    
    tokens = iterate_tokens()
    N = int(next(tokens))
    S = next(tokens)

    solve(N, S)

def solve(N: int, S: str):
    if N%2 == 0:
        half = int(N/2)
        s_first = S[:half]
        s_last = S[half:]
        if s_first == s_last:
            print('Yes')
        else:
            print('No')
    else: 
        print('No')

    return


 
if __name__ == "__main__":
    propare()