#!/usr/bin/env python3
import sys

def encode(s):
    code = [0] * 26
    for i in range(10):
        code[ord(s[i]) - ord('a')] += 1
    return code

def codeEqual(code1, code2):
    for i in range(26):
        if code1[i] != code2[i]:
            return False
    return True

def solve(N: int, s: "List[str]"):
    list_code = []
    for i in range(N):
        code = encode(s[i])
        list_code += [code]
    list_code = sorted(list_code)
    # count same string
    list_same = []
    count = 1
    for i in range(N-1):
        if codeEqual(list_code[i], list_code[i+1]):
            count += 1
        else:
            list_same += [count]
            count = 1
    if count > 1:
        list_same += [count]
    # count pairs
    final_count = 0
    for same in list_same:
        if same > 1:
            final_count += same * (same - 1) // 2
    print(final_count)
            
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
