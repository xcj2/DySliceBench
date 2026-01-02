#  --*-coding:utf-8-*--


def f(ABCD):
    vals = list(map(int, ABCD))

    a = vals.pop(0)
    exps = {a:str(a)}

    for val in vals:
        nextExps = {}
        for x, exp in exps.items():
            nextExps[x + val] = exp + '+' + str(val)
            nextExps[x - val] = exp + '-' + str(val)

        exps = nextExps

    return exps[7] + '=7'
            
            
def test():
    print("test mode")
    print(f('1222'))
    print(f('0290'))
    print(f('3242'))


def main():
    ABCD = input()
    print(f(ABCD))
    
if __name__ == '__main__':
    main()
