#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(H: int, W: int, s: "List[str]"):
    def is_valid(i, j):
        if (i > 0 and s[i - 1][j] == '#' or 
            i < H - 1 and s[i + 1][j] == '#' or 
            j > 0 and s[i][j - 1] == '#' or 
            j < W - 1 and s[i][j + 1] == '#'):
            return True
        return False

    for i, R in enumerate(s):
        for j, c in enumerate(R):
            if c == '#' and not is_valid(i, j):
                print(NO)
                return
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    s = [ next(tokens) for _ in range(H) ]  # type: "List[str]"
    solve(H, W, s)

if __name__ == '__main__':
    main()
