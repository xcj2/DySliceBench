#!/usr/bin/env python3
import sys, itertools

def solve(S: str):
    ans = 0
    for i in range(1<<(len(S)-1)):
        # i の bit が記号の挿入位置に当たる
        # print(i, format(i, 'b'), len(format(i,'b'))-1)
        tmp =int(S[0])
        for j in range(len(S)-1):
            # print(format(i, 'b'), j, bool(i & (1<<j))) # 挿入位置の判定
            if i & (1<<j): ans+=tmp;tmp=0;
            tmp*=10
            tmp+=int(S[j+1])
        ans+=tmp
    print(ans)
def main():
    def read(): return sys.stdin.readline().rstrip()
    solve(read())

if __name__ == '__main__':
    main()
# s = list(sys.stdin.rea