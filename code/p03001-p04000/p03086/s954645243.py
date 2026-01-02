class Test:
    def __init__(self):
        pass

class CustomUtils:
    def __init__(self):
        pass
    def to_int(self, inputs, sp=' '):
        if sp == '':
            return [int(d) for d in list(inputs)]
        else:
            return [int(d) for d in inputs.split(sp)]
    def debug_print(self, inputs, debug=False):
        if debug:
            print(inputs)

# 引用　python する man,「Pythonでの再帰関数とメモ化」, PSM, ２０１７、７/４
# http://muromura.hatenablog.com/entry/2017/07/04/204908#%E3%83%A1%E3%83%A2%E5%8C%96
def memorize(f):
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func
debug = False


u = CustomUtils()
iarray = list(input())

@memorize
def acgt(i):
    if i < 0:
        return 0
    elif iarray[i] in ['A', 'C', 'G', 'T']:
        return acgt(i -1) + 1
    else:
        return 0
result = max(acgt(i) for i in range(len(iarray)))
print("{}".format(result))