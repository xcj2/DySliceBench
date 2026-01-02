class Data:
    def __init__(self,n):
        self.n = n
        self.abc = []
        self.dp = [[0,0,0]]

    def input_abc(self):
        for i in range(self.n):
            self.abc.append(list(map(int,input().split())))
    
    def chmax(self,i,j,k):
        a = self.dp[i-1][j] + self.abc[i-1][k]
        b = self.dp[i][k]
        if (a>b):
            self.dp[i][k] = a
        #print("j",j,"k",k,a,b,"\n",self.dp)
def main():
    n = int(input())
    data = Data(n)
    data.input_abc()
    for i in range(1,n+1):
        data.dp.append([0,0,0])
        for j in range(3):
            for k in range(3):
                if j != k:
                    data.chmax(i,j,k)
    print(max(data.dp[i]))

if __name__ == "__main__":
    main()
