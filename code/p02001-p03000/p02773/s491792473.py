# Useful data structures
from collections import Counter

# For sys.std*, sys.argv etc...
import sys

# For cases when input tokens are spread unevenly over many lines.
# This provides methods for reading tokens of various types.
class BufferedTokenizer:
    pass

def read_ints():
    return [int(token) for token in input().split()]

def read_tokens():
    return input().split()

def main():
    N = read_ints()[0]
    votes = Counter(input() for _ in range(N))
    best = votes.most_common(1)[0][1]
    for vote in sorted(v[0] for v in votes.most_common() if v[1] == best):
        print(vote)

if __name__ == '__main__':
    main()
