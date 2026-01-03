#H×Wのマス目入力の周りに"."を付け加える関数
def pixel_input(H,W,border="."):
    pixel = [[border]*(W+2)] + \
    [[border] + list(input()) + [border] for _ in range(H)] + \
    [[border]*(W+2)]
    return pixel

#マス目型2次元配列を出力する関数
def pixel_print(pixel):
    for i in range(len(pixel)):
        print("".join(pixel[i]))

#数値の標準入力関数（1次元配列の場合は引数なし、2次元配列の場合は引数に行の数）
#switchを1にすると2次元配列のときに各行を配列として読み込まない
def ipt(N=0,switch=0):
    if N == 0:
        return list(map(int,input().split()))
    else:
        if switch==0:
            return [list(map(int,input().split())) for _ in range(N)]
        else:
            return [int(input()) for _ in range(N)]
          
#問題を解く
H,W=ipt()
pixel_print(pixel_input(H,W,"#"))