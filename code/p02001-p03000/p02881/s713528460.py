import sys

def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()

def all_factors(n):
    """returns a sorted list of all distinct factors of n"""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small

def solve(a,b):
    return (a-1)+(b-1)


n = int(input())
facts = all_factors(n)
length = len(facts)
mini = 10**15 + 7
if length&1:
    for i in range(length//2+1):
        mini = min(mini, solve(facts[i], facts[~i]))
    print(mini)
else:
    for i in range(length//2):
        mini = min(mini, solve(facts[i], facts[~i]))
    print(mini)