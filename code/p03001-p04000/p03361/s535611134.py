#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(H: int, W: int, s: "List[str]"):
    s = ["."*(W+2)]+["."+ss+"." for ss in s]+["."*(W+2)]
    
    direction = ((0,1),(1,0),(0,-1),(-1,0))

    # 全ての黒マスの上下左右に一つでも黒マスがあればおk
    for i in range(H+2):
        for j in range(W+2):
            if s[i][j] == ".":
                continue
            
            for x,y in direction:
                if s[i+x][j+y] == "#":
                    break
            else:
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
    s = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, s)

if __name__ == '__main__':
    main()
