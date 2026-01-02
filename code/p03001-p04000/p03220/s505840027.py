import io
import sys

import sys
def solve(T,A,listH):
    sa = 1000
    for x in range(len(listH)):
        if sa >= abs(A - (T - (int(listH[x]) * 0.006))):
            sa = abs(A - (T - (int(listH[x]) * 0.006)))
            a = x+1
    return a

def readQuestion():

    line1 = sys.stdin.readline().rstrip()
    line2 = sys.stdin.readline().rstrip()
    list1 = line2.split(" ")
    line3 = sys.stdin.readline().rstrip()
    list2 = line3.split(" ")
    return int(list1[0]),int(list1[1]),list2

def main():
    t,a,h = readQuestion()
    answer = solve(t,a,h)
    print(answer)
    
if __name__ == '__main__':
    main()