#!/usr/bin/env python3
import sys
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

from collections import deque
def main():
    S = input()
    queue = deque(list(S))
    Q = INT()
    reverse_flag = False

    for _ in range(Q):
        query = list(input().split())
        if len(query) == 3:
            F = int(query[1])
            C = query[2]
            if F == 1:
                if reverse_flag:
                    queue.append(C)
                else:
                    queue.appendleft(C)
            elif F == 2:
                if reverse_flag:
                    queue .appendleft(C)
                else:
                    queue.append(C)
        else:
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
    answer = ''.join(queue)
    if reverse_flag:
        answer = answer[::-1]
    print(answer)
    return
        
if __name__ == '__main__':
    main()
