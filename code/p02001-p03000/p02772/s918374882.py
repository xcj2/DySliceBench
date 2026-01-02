# Useful data structures

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
    read_ints()
    approved = all(any(n % d == r for (d, r) in [(2, 1), (3, 0), (5, 0)])
                    for n in read_ints())
    print("APPROVED" if approved else "DENIED")

if __name__ == '__main__':
    main()
