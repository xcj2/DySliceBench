import sys

def _calc(Ai, j):
    if j != 0:
        return j * Ai + 1
    if j == 0:
        return 1

def main(inp_list):
    # return inp_list
     N = inp_list[0]
     D = inp_list[1][0]
     X = inp_list[1][1]
     A = inp_list[2:]
     #return type(A[0][0])
     results =[ _calc(per[0], i) for per in A  for i in range(0,100) if _calc(per[0], i) < D + 1]
     return len(list(results)) + X

def init(MODE):
    if MODE == 0:
        while True:
            try:
                result = int(input())
                yield result
            except:
                break

    if MODE == 1:
        while True:
            try:
                li=list(map(int,input().split()))
                yield li
            except:
                break
if __name__ == '__main__':
    """ MODE: 0 縦, 1 縦横, 2 横 """
    MODE = 1
    inp_list = init(MODE)
    print(main(list(inp_list)))