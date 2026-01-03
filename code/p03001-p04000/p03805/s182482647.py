import sys
import itertools
import copy

input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N, M = MI()
    numlist = [i for i in range(1, N)]
    mylist2 = [[0 for i in range(N)] for j in range(M)]
    result = 0
    for i in range(M):
        a, b = MI()
        mylist2[min(a, b) - 1][max(a, b) - 1] = 1
    for j in itertools.permutations(numlist, len(numlist)):
        mylist = copy.deepcopy(mylist2)
        index = 0
        past = 0
        for k in j:
            try:
                
                if mylist[min(past, k)][max(past, k)] == 1:
                    mylist[min(past, k)][max(past, k)] = 0
                    past =  k
                    index += 1
                else:
                    break
            except:
                if mylist[0][k] == 1:
                    mylist[0][k] = 0
                    past = k
                    index += 1
                else:
                    break
        if index == len(numlist):
            result += 1
    print(result)
    
main()
                        
                    
        
    