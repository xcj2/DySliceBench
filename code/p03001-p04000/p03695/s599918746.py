#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    color = set()
    rainbow_count = 0
    for i in range(N):
        if a[i]<=399:
            color.add("gray")
        elif a[i]<=799:
            color.add("brown")
        elif a[i]<=1199:
            color.add("green")        
        elif a[i]<=1599:
            color.add("lightblue")        
        elif a[i]<=1999:
            color.add("blue")        
        elif a[i]<=2399:
            color.add("yellow")
        elif a[i]<=2799:
            color.add("orange")        
        elif a[i]<=3199:
            color.add("red")
        else:
            rainbow_count+=1
    
    min_answer = len(color)
    max_answer = len(color) + rainbow_count
    
    if not color and rainbow_count >0:
      min_answer=1
      max_answer=rainbow_count
    print(min_answer,max_answer)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
