#coding: utf-8

def getInput():
    in_row = [ int(x) for x in input().split(" ") ]
    return in_row

def gcd(n1, n2):
    while n1 % n2 != 0:
        if n1 < n2:
            n1, n2 = n2, n1
        n1 %= n2
    return n2
            
def judgeTakahashi(in_row):
    A = in_row[0]
    B = in_row[1]
    C = in_row[2]
    D = in_row[3]
    g = gcd(B, D)

    if B > A:
        return False
    if B > D:
        return False
    if C >= B:
        return True
    
    if B-g+(A%g) > C:
        return False
    else:
        return True

if __name__ == "__main__":
    N = int(input())
    assert gcd(1071, 1029) == 21, "error"
    assert not(judgeTakahashi([1, 10, 1, 1])), "error"
    for i in range(N):
        in_row = getInput()
        result = "Yes" if judgeTakahashi(in_row) else "No"
        print(result)
