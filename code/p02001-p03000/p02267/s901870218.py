class Search():
    def __init__(self,N,input_S):
        self.sum = 0
        self.N = N
        self.input_S = input_S
        input_S.append(0)
    def search(self,key):
        self.input_S[self.N] = key
        i = 0
        while(self.input_S[i]!=key):
            i += 1
        if i != self.N:
            self.sum += 1
def main():
    N = int(input())
    input_S = [int(i) for i in input().split()]
    M = int(input())
    input_T = [int(i) for i in input().split()]
    linear_search = Search(N,input_S)
    for i in range(len(input_T)):
        linear_search.search(input_T[i])
    print(linear_search.sum)

if __name__ == "__main__":
    main()

