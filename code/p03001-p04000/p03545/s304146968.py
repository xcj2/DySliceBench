# dfs
def search7(i, ticket, equation):
    if i == len(ticket) - 1:
        if eval(equation) == 7:
            return True, equation
        else:
            return False, '_'
    else:
        check_param, new_equation = search7(i + 1, ticket, equation + '+' + ticket[i + 1])
        if check_param:
            return True, new_equation
        check_param, new_equation = search7(i + 1, ticket, equation + '-' + ticket[i + 1])
        if check_param:
            return True, new_equation
        
        return False, '_'


def input():
    import sys
    return sys.stdin.readline().rstrip()


def main():
    import math
    import collections
    import itertools

    ticket = list(input())

    _, equation = search7(0, ticket, ticket[0])
    print(equation+'=7')


if __name__ == '__main__':
    main()