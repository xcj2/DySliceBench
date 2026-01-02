from sys import stdin, stdout
from collections import defaultdict
def readLine_str_list():return list(map(str, stdin.readline().split()))
def readLine_int_list():return list(map(int, stdin.readline().split()))
def readAll_str(): return list(list(map(str,i.split())) for i in stdin.read().split("\n"))
def g_twoD_list(p,q): return [[0 for i in range(p)] for j in range(q)]


def main():
    h,w = readLine_int_list()
    a = g_twoD_list(w,h)
    b = defaultdict(lambda: 0)
    _h = 0
    _w = 0
    for l in readAll_str():
        for i in l:
            _w = 0
            for j in i:
                b[(_h,_w)] = j
                _w += 1
            _h += 1
            
    dir_b = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for d in dir_b:
                r = b[(i+d[0], j+d[1])]
                if r == '#':
                    cnt += 1
            if b[(i,j)] == '.':
                b[(i,j)] = str(cnt)
    # print(b)
    for i in b:
        if 0 <= i[0] < h and 0 <= i[1] < w:
            a[i[0]][i[1]] = b[i]
            
    for i in a:
        print(''.join(i))
if __name__ == "__main__":
    main()
