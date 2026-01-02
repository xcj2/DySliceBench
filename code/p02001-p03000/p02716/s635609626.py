from itertools import accumulate,chain
from itertools import combinations

from random import randrange


def solve(A):
    N = len(A)
    oddacc = tuple(chain((0,),accumulate(A[1::2])))
    evenacc = tuple(chain((0,),accumulate(A[::2])))
    if N%2==0:
        return max(evenacc[i]+oddacc[-1]-oddacc[i] for i in range(N//2+1))

    # one 3 space
    res = max(evenacc[-1]-A[i*2] for i in range(N//2+1))
    # two 2 space
    def it():
        m = 0

        for i in reversed(range(N//2)):
            m = max(m+A[i*2+1], A[i*2+1]+evenacc[-1]-evenacc[i+2])
            yield m+evenacc[i]
    res = max(max(it()), res)
    return res

def naive(A):
    def it():
        for indices in combinations(range(len(A)), r=len(A)//2):
            if all(i+1!=j for i,j in zip(indices,indices[1:])):
                yield (sum(A[i] for i in indices), indices)

    return max(it())

if __name__ == '__main__':
    N = map(int,input().split())
    A = tuple(map(int,input().split()))
    print(solve(A))


    # for _ in range(10000):
    #     A = [randrange(1000)-500 for _ in range(6)]

    #     a = solve(A)
    #     b,ind = naive(A)
    #     if a!=b:
    #         print(ind)
    #         print(A)
    #         print(a,b)
    #         break