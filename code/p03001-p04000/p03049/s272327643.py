from sys import stdin
import math
import itertools


def makeIntMatrix(lines):
    intMatrix = []
    for a in makeStringMatrix(lines):
        intMatrix.append([int(b) for b in a])
    return intMatrix
 
 
def makeStringMatrix(lines):
    stringMatrix = [line.rstrip() for line in lines]
    return stringMatrix
 
 
def makeInt(line):
    return int(line.rstrip())
 
 
def makeMultiInteger(line):
    return [int(x) for x in line.rstrip().split()]


def solve(input_string):
    N = makeInt(input_string[0])
    S = makeStringMatrix(input_string[1:])
    #print(S)
    C_S_has_ab = []
    for s_index, s in enumerate(S):
        C_S_has_ab.append(0)
        for i in range(len(s)-1):
            if s[i] + s[i+1] == 'AB':
                C_S_has_ab[s_index] += 1
    #print(C_S_has_ab)
    _sum = 0
    _sum += sum(C_S_has_ab) 
    c_head_has_b = 0
    c_tail_has_a = 0
    c_head_tail_has_a_and_b = 0
    for s in S:
        """
        if s[0] == 'B':
            c_head_has_b += 1
        if s[-1] == 'A':
            c_tail_has_a += 1
        if s[0] == 'B' and s[-1] == 'A':
            c_head_tail_has_a_and_b += 1
        """
        if(s[0] == 'B' and s[-1] == 'A'):
            c_head_tail_has_a_and_b += 1
        elif(s[-1] == 'A'):
            c_tail_has_a += 1
        elif(s[0] == 'B'):
            c_head_has_b += 1
    #print(c_head_has_b, c_tail_has_a, c_head_tail_has_a_and_b)
    if c_head_tail_has_a_and_b > 0:
        count_combi_a_b = max(0, c_head_tail_has_a_and_b-1) + min(c_head_has_b, c_tail_has_a)
        if c_head_has_b > 0 or c_tail_has_a > 0:
            count_combi_a_b += 1
    else:
        count_combi_a_b = min(c_head_has_b, c_tail_has_a)
    _sum += count_combi_a_b
    #print(_sum)
    return _sum


def main():
    input_lines = stdin.readlines()
    answer = solve(input_lines)
    print(answer)


if __name__ == '__main__':
    main()
