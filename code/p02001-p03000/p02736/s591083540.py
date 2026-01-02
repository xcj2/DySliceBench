N = int(input())
a = input()

def is_combination_odd(n, r):
    _n = n
    _r = r
    is_odd = True
    while _n > 0 and _r > 0:
        if _n % 0b10 < _r % 0b10:
            is_odd = False
            break
        _n >>= 1
        _r >>= 1
    #print('n: %d, r: %d, is_odd: %d' % (n, r, is_odd))
    return is_odd
    
def is_ans_odd(num_str: str) -> bool:
    is_odd = False
    for i, c in enumerate(num_str):
        is_c_odd = int(c) % 2
        is_odd ^= is_combination_odd(len(num_str)-1, i) & is_c_odd
    return is_odd

def main():
    ans = -1
    table = str.maketrans({'1': '0', '2': '1', '3': '2'})
    a012 = a.translate(table)
    if is_ans_odd(a012):
        ans = 1
    else:
        if '1' in a012:
            ans = 0
        else:
            table = str.maketrans({'2': '1'})
            a01 = a012.translate(table)
            if is_ans_odd(a01):
                ans = 2
            else:
                ans = 0

    print(ans)

if __name__ == '__main__':
    main()
