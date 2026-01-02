import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def is_kaibun(_S):
    if len(_S)==1 or _S[:int((len(_S))/2)]==_S[int((len(_S)+1)/2):][::-1]:
        return True
    else:
        return False

def main():
    _S = S()
    is_tsuyoi1 = is_kaibun(_S)
    is_tsuyoi2 = is_kaibun(_S[:int((len(_S)-1)/2)])
    is_tsuyoi3 = is_kaibun(_S[int((len(_S)+1)/2):])
    print("Yes" if is_tsuyoi1 and is_tsuyoi2 and is_tsuyoi3 else "No")


main()
