#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    table = {}
    for i in range(len(T)):
        if table.get(S[i]) == None:
            table[S[i]] = T[i]
        else:
            if table[S[i]] == T[i]:
                continue
            else:
                # 同じ文字を違う文字に変換しようとしたらアウト
                print(NO)
                return

    value_list = []
    for value in table.values():
        value_list.append(value)
        
    # 違う文字を同じ文字に変換しようとしたらアウト
    if len(set(value_list)) == len(table):
        print(YES)
    else:
        print(NO)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)

if __name__ == '__main__':
    main()
