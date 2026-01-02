import sys
import collections

def solve(N: int, A: "List[int]"):
    counter = collections.Counter(A)
    counter = sorted(counter.items(), key=lambda x:x[0], reverse=True)

    w =0
    h =0
    for i,item in enumerate(counter):
        if item[1] >=2:
            w = item[0]
            counter[i] = (item[0],item[1]-2)
            break
    
    for i,item in enumerate(counter):
        if item[1] >=2:
            h = item[0]
            break
    
    print(w*h)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
