#我不知道怎么定义结构体，我是直接模拟的    QAQ
start = [1,2,3,5,4,6]

def N():
    start[0],start[1],start[3],start[5] = \
    start[1],start[5],start[0],start[3]
    
def S():
    start[0],start[1],start[3],start[5] = \
    start[3],start[0],start[5],start[1]
    
def W():
    start[0],start[2],start[4],start[5] = \
    start[2],start[5],start[0],start[4]

def E():
    start[0],start[2],start[4],start[5] = \
    start[4],start[0],start[5],start[2]

if __name__ == "__main__":
    lst = list(map(int,input().split()))
    s = input()
    for i in range(len(s)):
        if s[i]=='S':
            S()
        if s[i]=='E':
            E()
        if s[i]=='W':
            W()
        if s[i]=='N':
            N()
    print(lst[start[0]-1])
