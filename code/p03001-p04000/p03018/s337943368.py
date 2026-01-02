import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')

def main():
    s = SI().strip()

    if len(s) <= 2:
        print(0)
        return
    
    prepre = s[0]
    previous = s[1]
    if previous == 'A' and prepre == 'A': A_counter = 2
    elif previous == 'A' or (prepre == 'A' and previous == 'B'): A_counter = 1
    else: A_counter = 0
    jumps = 0
    for char in s[2:]:
        if char == 'A':
            if previous == 'A':
                A_counter += 1
                prepre = previous
            elif previous == 'B':
                prepre = previous
                A_counter = 1
                previous = 'A'
            elif previous == 'C':
                prepre = previous
                A_counter += 1
                previous = 'A'
        elif char == 'B':
            if previous == 'A':
                prepre = previous
                previous = 'B'
            elif previous == 'B':
                prepre = previous
                A_counter = 0
            elif previous == 'C':
                # BCB のときはまだリセットしない。
                if prepre != 'B':
                    A_counter = 0
                prepre = previous
                previous = 'B'
        elif char == 'C':
            if previous == 'A':
                A_counter = 0
                prepre = previous
                previous = 'C'
            elif previous == 'B':
                jumps += A_counter
                prepre = previous
                previous = 'C'
            elif previous == 'C':
                A_counter = 0
                prepre = previous
    print(jumps)

main()