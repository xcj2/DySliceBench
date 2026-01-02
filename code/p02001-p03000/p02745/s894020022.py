#!/usr/bin/env python3

def compare(a, b):
    return a == '?' or b == '?' or a == b

def solve(A, B, C):
    n, m, l = len(A), len(B), len(C)
    AB, AC, BC = [True]*(n+1), [True]*(n+1), []
    for i in range(n):
        for j in range(m):
            if i + j >= n:
                continue
            if not compare(A[i + j], B[j]):
                AB[i] = False
                break
    
    for i in range(n):
        for j in range(l):
            if i + j >= n:
                continue
            if not compare(A[i + j], C[j]):
                AC[i] = False
                break

    for i in range(n):
        for j in range(l):
            if i + j >= m:
                continue
            if compare(B[i + j], C[j]):
                continue
            break
        else:
            BC.append(i)
    for i in range(max(0,n-m)):
        BC.append(m+i)

    res = n + m + l
    for i in range(n+1):
        if AB[i]:
            for j in BC:
                if i + j >= n:
                    res = min(res, max(i + m, i + j + l))
                elif AC[i + j]:
                    res = min(res, max(n, i + m, i + j + l))
    return res

def main():
    a = input()
    b = input()
    c = input()
    ans = min(solve(a,b,c),solve(a,c,b),solve(b,a,c),solve(b,c,a),solve(c,a,b),solve(c,b,a))
    print(ans)

if __name__ == '__main__':
    main()
