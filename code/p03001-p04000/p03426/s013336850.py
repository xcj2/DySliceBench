import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    H, W, D = LI()
    mod_array = [[(0,0) for _ in range(H*W//D+1)] for _ in range(D)]
    for row_number in range(H):
        row = LI()
        for column_number, item in enumerate(row):
            mod_array[item%D][item//D] = (row_number, column_number)

    # print(mod_array)

    mod_array_cumsum = [[0 for _ in range(H*W//D+1)] for _ in range(D)]
    for row_number in range(D):
        cumsum = 0
        prev_position = mod_array[row_number][0]
        for column_number in range(1, H*W//D+1):
            position = mod_array[row_number][column_number]
            cumsum += abs(prev_position[0] - position[0]) + abs(prev_position[1] - position[1])
            mod_array_cumsum[row_number][column_number] = cumsum
            prev_position = position

    # print(mod_array_cumsum)

    Q = II()
    for _ in range(Q):
        L, R = LI()
        ans = mod_array_cumsum[L%D][R//D] - mod_array_cumsum[L%D][L//D]
        print(ans)
        

main()