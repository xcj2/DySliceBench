#!/usr/bin/env python3
import sys

def solve(a: str, b: str, c: str):
    permutation = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,1,0),(2,0,1)]
    abc = (a,b,c)
    ans = 10**4

    for i_1,j_1,k_1 in permutation:
        A = abc[i_1]
        B = abc[j_1]
        C = abc[k_1]
        LENA = len(A)
        LENB = len(B)
        LENC = len(C)

        AB = [False]*(LENA+1)
        BC = [False]*LENB+[True]*2010
        AC = [False]*(LENA)+[True]*(2010)
        AB[LENA] = True

        # 前計算
        for i in range(LENA): # Aのindex
            for j in range(i,min(LENA,LENB+i)):
                if A[j] != B[j-i] and A[j] != "?" and B[j-i] != "?":
                    break
            else:
                AB[i] = True

        for i in range(LENB): # Bのindex
            for j in range(i,min(LENB,LENC+i)):
                if B[j] != C[j-i] and B[j] != "?" and C[j-i] != "?":
                    break
            else:
                BC[i] = True

        for i in range(LENA): # Aのindex
            for j in range(i,min(LENA,LENC+i)):
                if A[j] != C[j-i] and A[j] != "?" and C[j-i] != "?":
                    break
            else:
                AC[i] = True        

        # x: AとBがどれだけずれてるか
        # y: BとCがどれだけずれてるか
        length = 10**4
        for x in range(LENA+1):
            for y in range(2001+1):
                if AB[x] and BC[y] and AC[x+y]:
                    length = min(length,max(LENA,x+LENB,x+y+LENC))
        ans = min(ans,length)
 
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = next(tokens)  # type: str
    b = next(tokens)  # type: str
    c = next(tokens)  # type: str
    solve(a, b, c)

if __name__ == '__main__':
    main()
