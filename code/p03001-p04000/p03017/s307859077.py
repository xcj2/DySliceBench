from copy import deepcopy
def solve():
    N,A,B,C,D = map(lambda x:int(x)-1, input().split())
    field_orig = list(input())
    field = deepcopy(field_orig)

    if C < D:
        if existsContinuousRocks(field,A,B,C,D):
            print('No')
        else:
            print('Yes')
    else:
        if not existsContinuousRocks(field,A,B,C,D) \
            and existsContinuousDots(field,A,B,C,D):
            print('Yes')
        else:
            print('No')

def existsContinuousRocks(field, A, B, C, D):
    for i in range(A, min(max(C,D), len(field)-1)):
        if field[i] == '#' and field[i+1] == '#':
            return True
    return False

def existsContinuousDots(field,A,B,C,D):
    for i in range(B-1,min(D, len(field)-2)):
        if field[i] == '.' and field[i+1] == '.' and field[i+2] == '.':
            return True
    return False


if __name__ == '__main__':
    solve()