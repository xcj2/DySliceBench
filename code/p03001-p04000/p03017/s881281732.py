#  --*-coding:utf-8-*--


def f(S, N, A, B, C, D):
    if B > C:
        if g(S, A, C) or g(S, C, D):
            return 'No'
        else:
            return 'Yes'
            
    elif C < D:
        if g(S, A, D):
            return 'No'
        else:
            return 'Yes'
        
    else:
        if g(S, A, B):
            return 'No'

        if g2(S, B-1, D):
            return 'Yes'
        
        return 'No'


def g(S, X, Y):
    for i in range(X-1, Y-1):
        if S[i] == '#' and S[i+1] == '#':
            return True

    return False



def g2(S, X, Y):
    for i in range(X-1, Y-1):
        if S[i] == '.' and S[i+1] == '.' and S[i+2] == '.':
            return True

    return False



def main():
    N, A, B, C, D = map(int, input().split())
    S = input()

    print(f(S, N, A, B, C, D))
 


if __name__ == '__main__':
    main()
