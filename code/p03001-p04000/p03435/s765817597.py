# coding: UTF-8
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
    C11,C12,C13 = map(int,input().split())
    C21,C22,C23 = map(int,input().split())
    C31,C32,C33 = map(int,input().split())
    
    C = C11
    A2 = C21 - C
    A3 = C31 - C
    B2 = C12 - C
    B3 = C13 - C
    C22 -= C
    C23 -= C
    C32 -= C
    C33 -= C
    
    if C22 == A2+B2 and C23 == A2+B3 and C32 == A3+B2 and C33 == A3+B3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    exe()