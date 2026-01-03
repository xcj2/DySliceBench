from sys import stdin, stdout
def readLine_int_list():return list(map(int, stdin.readline().split()))
def readLine_int_list_reverse(): return list(map(int, stdin.readline().split())).reverse()
def readAll_int(): return list(map(int, stdin))
def readLine_str_list():return list(map(str, stdin.readline().split()))
def readAll_str(): return list(map(str, stdin))
def readLine_int_set(): return set(list(map(int, stdin.readline().split())))
def g_twoD_list(p,q): return [[0 for i in range(p)] for j in range(q)]


def main():
    n,k,x,y = readAll_int()
    print(k*x + (n-k)*y if n-k > 0 else n*x)
    
if __name__ == "__main__":
    main()
