# coding: UTF-8
#@document_it
from collections import deque
def document_it(func):
    def new_function(*args,**kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Kewword arguments:', kwargs)
        result = func(*args,**kwargs)
        print('Result:', result)
        return result
    return new_function


def exe():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    s = deque(A)
    alice =0
    bob = 0
    for i in range(N):
        if i % 2 == 0:
            alice += s.pop()
        else:
            bob += s.pop()
    print(alice-bob)

if __name__ == '__main__':
    exe()