#-*- coding:utf-8 -*-
"""
2020年, AtCoder社は年商10億円を超え, プログラミング教育にも手を出すようになった.
ある日行われたテストでは, 1才児は Hello world を出力するプログラムを, 2才児は整数A,Bを入力してA+Bを出力するプログラムを書かなければならない.
高橋君はこのテストを受けているが, 突然自分が何才なのかが分からなくなってしまった.
そこで, 最初に自分の年齢N(Nは1または2)を入力し, N=1ならば Hello World と出力し, N=2ならばA,Bを入力してA+Bを出力するプログラムを作ることにした.
高橋君に代わって, このようなプログラムを作りなさい.
"""
def kadai1():
    print("Hello World")


def kadai2():
    A = int(input())
    B = int(input())
    print(A + B)


def main():
    N = int(input())
    if N == 1:
        kadai1()
    else:
        kadai2()


if __name__ == "__main__":
    main()