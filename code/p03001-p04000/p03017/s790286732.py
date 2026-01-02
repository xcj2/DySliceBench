l = input().split()
N = int(l[0])
A = int(l[1])
B = int(l[2])
C = int(l[3])
D = int(l[4])
l = input().split()
S = l[0]

# print(N, A, B, C, D, S)

def blocked(path):
    return '##' in path

def find_path(A, B, C, D, S):
    s_path = S[A:C]
    f_path = S[B:D]
    if blocked(s_path) or blocked(f_path):
        return False
    return True

def solve(A, B, C, D, S):
    if not find_path(A, B, C, D, S):
        return False
    begin = B - 2
    if S[D - 2] == '#':
        if '...' in S[begin:D - 2]:
            return True
        else:
            return False
    else:
        path = S[begin:C]
        if '...' in path:
            return True
    return False

ret = True
if C < D:
    ret = find_path(A, B, C, D, S)
else:
    ret = solve(A, B, C, D, S)

if ret:
    print('Yes')
else:
    print('No')
