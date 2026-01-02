import sys
import socket
 
if socket.gethostname() in ['N551J', 'F551C']:
    sys.stdin = open('c1.in')
 
 
def read_int_list():
    return list(map(int, input().split()))
 
 
def read_int():
    return int(input())
 
 
def read_str_list():
    return input().split()
 
 
def read_str():
    return input()
 
 
def solve():
    n = read_int()
    s = read_str()

    #同じ文字が連続する場合、redとblueに振り分ける順番が変わってもそのあとの判定に影響を与えないので、計算結果をcasheに格納して同一計算を省略する
    cache = {}

    #1文字ずつredとblueに振り分けながら再帰的に関数読み出しを繰り返し、条件を満たしながらredとblue双方の長さが2nになったものの数を数える
    #探索数は基本的に2のn乗でスケールするが、条件に当てはまらないような塗分けは排除しながら進んでいく（再帰読み出しを行わず戻り値0を返す）
    def rec(red, blue):
        #一度探索したことのある文字列は即答する
        if (red, blue) in cache:
            return cache[(red, blue)]

        nr = len(red)
        nb = len(blue)

        #redとblueのどちらかが長さnを超えていたら関数は0を返す
        if nr > n or nb > n:
            res = 0
            cache[(red, blue)] = res
            return res
        #長さの合計がちょうど2nなら（上記と合わせると、両方の長さがnずつならば関数は1を返す）
        if nr + nb == 2 * n:
            res = 1
            cache[(red, blue)] = res
            return res
        c = s[nr + nb]
        res = 0

        #文字列sの一番左の文字から始め、1文字ずつredの左側もしくはblueの右側に格納していく
        #nr+nbがn未満の場合無条件で再帰的関数読み出しを行う
        #nr+nbがnを超えた場合、新しく追加する文字cがこれまでのred, blueと整合性が取れている場合のみに再帰的関数読み出しを行う
        if nr + nb < n or (nr < n and c == blue[nr - n]):
            res += rec(red + c, blue)
        if nr + nb < n or (nb < n and c == red[n - 1 - nb]):
            res += rec(red, c + blue)

        
        cache[(red, blue)] = res
        return res

    res2 = rec('', '')
    return res2
 
 
def main():
    res = solve()
    print(res)
 
 
if __name__ == '__main__':
    main()
