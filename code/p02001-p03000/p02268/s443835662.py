class Binary_search():
    def __init__(self,S):
        self.num = 0
        self.S = S
    def binary_search(self,left,right,key):
        if left < right:
            mid =int((left + right) / 2)
            if self.S[mid] == key:
                self.num += 1
            elif self.S[mid] < key:
                self.binary_search(mid+1,right,key)
            else:
                self.binary_search(left,mid,key)

def main():
    N = int(input())
    S = [int(c) for c in input().split()]
    M = int(input())
    T = [int(c) for c in input().split()]
    binary_search = Binary_search(S)
    for i in range(M):
        binary_search.binary_search(0,N,T[i])
    print(binary_search.num)

if __name__ == '__main__':
    main()

