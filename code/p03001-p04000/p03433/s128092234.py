# coding: UTF-8
# from collections import deque
#@document_it
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
    n = int(input())
    a = int(input())
    if n % 500 <= a:
        print('Yes')
    else:
        print('No')
    

if __name__ == '__main__':
    exe()