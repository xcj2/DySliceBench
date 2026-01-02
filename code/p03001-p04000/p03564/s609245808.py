from sys import stdin, stdout
from collections import defaultdict
def readLine_int_list():return list(map(int, stdin.readline().split()))
def readLine_int_list_reverse(): return list(map(int, stdin.readline().split())).reverse()
def readAll_int(): return list(map(int, stdin))
def readLine_str_list():return list(map(str, stdin.readline().split()))
def readAll_str(): return list(map(str, stdin))


def main():
	n,k = readAll_int()
	ans = 1
	for i in range(n):
	    _k = ans + k
	    _d = ans * 2 
	    ans = min(_k, _d)

	print(ans)

if __name__ == "__main__":
    main()
