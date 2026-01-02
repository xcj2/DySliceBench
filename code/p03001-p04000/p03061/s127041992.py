"""
問題文

N個の整数 A1,A2,...,ANが黒板に書かれています。
あなたはこの中から整数を 1つ選んで、1 以上 109以下の好きな整数に書き換えます。
元の整数と同じ整数に書き換えても構いません。書き換えた後のN個の整数の最大公約数の最大値を求めてください。

制約
入力は全て整数である。
2≤N≤105
1≤Ai≤109
"""

"""
3 5 7
最大公約数: 1
最大の最大公約数: 1

8 4 6
最大公約数: 2
最大の最大公約数: 4
『aとbとcの最大公約数』　＝　『aとbの最大公約数』と『c』　の最大公約数

A1 , A2 , A3 ... An

gcd(A1 , A2 , A3 ... An-1) * N
= gcd * N * N
= gcd * N^2

gcd(A1 , A2 , A3 ... An-1)
gcd(A1 , A2 , A3 ... An-2 , An) = gcd(A1 , A2 , A3 ... An-2) , An
"""
def gcd(a, b):  # a>b
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

from functools import reduce
def GCD(numbers):
    if len(numbers) == 0 : return 0
    if len(numbers) == 1 : return numbers[0]
    if len(numbers) == 2 : 
        return gcd(numbers[0] , numbers[1])
    else : 
        value = GCD(numbers[:len(numbers)-1])
        result = gcd(value , numbers[len(numbers) - 1])
        return result

def main() : 
    N = int(input())
    a_list = input().split(" ")
    a_list = [int(i) for i in a_list]
    R = [0 for i in range(N - 1)]
    L = [0 for i in range(N - 1)]
    R[0] = a_list[0]
    L[0] = a_list[-1]

    for i in range(1 , N-1) : 
        R[i] = gcd(R[i - 1] , a_list[i])
    
    for j in range(1 , N-1) : 
        L[j] = gcd(L[j - 1] , a_list[- j - 1])
    
    maxValue = 0
    for i in range(N - 2) : 
        value = gcd(R[i] , L[N - i - 3])
        if value > maxValue : maxValue = value
    print(max(maxValue , R[-1] , L[-1]))
main()
