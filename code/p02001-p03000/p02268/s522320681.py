class BinarySearch:

    def __init__(self, S, n):
        self.target = S
        self.length = n
    
    def search(self, key):
        left = 0
        right = self.length
        while left<right:
            mid = int((left+right)/2)
            if self.target[mid]==key:
                return True
            elif self.target[mid]<key:
                left = mid + 1
            elif self.target[mid]>key:
                right = mid
        return False


def main():
    n = int(input())
    S = [int(i) for i in input().split()]
    q = int(input())
    T = (int(i) for i in input().split())
    bs = BinarySearch(S, n)
    count = 0
    for t in T:
        if bs.search(t):
            count += 1
    print(count)

if __name__=='__main__':
    main()
