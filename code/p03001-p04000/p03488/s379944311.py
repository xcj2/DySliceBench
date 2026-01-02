#!/usr/bin/env python3

import sys


def main():
    def input(): return sys.stdin.readline().rstrip()
    def mi():    return map(int, input().split())


    def preprocess(s):
        x_command, y_command = [], []
        L = s.split('T')
        n = len(L)
        for i in range(n):
            if i % 2 == 0 and L[i]:
                x_command.append(L[i].count("F"))
            elif i % 2 == 1 and L[i]:
                y_command.append(L[i].count("F"))
        return x_command, y_command
    

    def valid_command(command, delta):
        # print(f"{command} {delta}")
        if not command:
            return delta == 0
        possible_num_set = set()
        n = len(command)
        for i in range(n):
            if i == 0:
                possible_num_set.add(command[0])
                possible_num_set.add(-command[0])
            else:
                num = command[i]
                new_set = set()
                for candidate in possible_num_set:
                    new_set.add(candidate + num)
                    new_set.add(candidate - num)
                possible_num_set = new_set
        # print(f"{command} {possible_num_set}")
        return delta in possible_num_set

    s = input()
    s.rstrip('T')
    n = len(s)
    x, y = mi()
    dx, dy = x, y
    tail_of_front_F = -1
    for i in range(n):
        if s[i] == 'F':
            tail_of_front_F = i
        else:
            break
    s = s[tail_of_front_F+1:]
    if tail_of_front_F >= 0:
        dx -= (tail_of_front_F + 1)
    

    x_command, y_command = preprocess(s)
    # print(x_command)
    # print(y_command)
    if valid_command(x_command, dx) and valid_command(y_command, dy):
        print("Yes")
    else:
        print("No")

    


if __name__ == "__main__":
    main()
