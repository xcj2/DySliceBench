#这个也是在模拟，不过是吧骰子反转到正面和侧面一样 (⊙o⊙)？，不知道有没有简单的方法
start = [0,1,2,4,3,5]#上 正 右 后 左 下
s = []
#下面的是几个反转方式
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


#这是特殊的旋转方法
def roll():
    start[1],start[2],start[3],start[4] = \
    start[4],start[1],start[2],start[3]          

def get_top():
    return s[start[0]]

def get_zhengMian():
    return s[start[1]]

def get_right():
    return s[start[2]]

def get_left():
    return s[start[4]]

if __name__=='__main__':
    s = list(map(int,input().split()))
    num = int(input())
    for i in range(num):
        a,b = map(int,input().split())
        if a!=get_top():
            right =get_right()
            left = get_left()
            top = get_top()
            if(a==right):
                W()
            elif a==left:
                E()
            while a!=top:
                S()
                top = get_top()
        zhengmian = get_zhengMian()
        right = get_right()
        if b!=zhengmian:
            while b!=zhengmian:
                roll()
                zhengmian = get_zhengMian()
        print(get_right())
