import sys
def input(): return sys.stdin.readline().strip()

def first_bit_of(n):
    """
    nの先頭ビットが下から何桁目かを出力する。（最下位を0桁目として）
    """
    if n == 0: return 0
    if n > 0:
        idx = 0
        while n > 0:
            n -= pow(4, idx)
            idx += 1
        return 2 * (idx - 1)
    if n < 0:
        idx = 0
        while n < 0:
            n += pow(2, 2 * idx + 1)
            idx += 1
        return 2 * idx - 1
        

def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    first_place = first_bit_of(N)
    #print("first_bit={}".format(first_place))
    ans = [0] * (first_place + 1)
    ans[0] = 1
    N -= pow(-2, first_place)

    while N != 0:
        place = first_bit_of(N)
        #print("first_bit_of({})={}".format(N, place))
        ans[first_place - place] = 1
        N -= pow(-2, place)
    print("".join(map(str, ans)))
    

if __name__ == "__main__":
    main()
