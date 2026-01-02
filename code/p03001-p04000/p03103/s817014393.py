# coding: utf-8
import os
from sys import stdin
from functools import total_ordering

# __dirname = os.path.dirname(__file__)
# __basename = os.path.splitext(os.path.basename(__file__))[0]
# __targetname = './input/' + __basename + '.txt'
# target_path = os.path.join(__dirname, __targetname)
# stdin = open(target_path)

@total_ordering
class struct(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __lt__	(self,other):
        return self.a < other.a
    def __eq__	(self,other):
        return self.a == other.a

def main():
    # st = struct(10,1)
    # print(st.a)
    input_line = stdin.readline().rstrip().split(' ')
    N, M = map(int, input_line)
    A = list()
    for _ in range(N):
        input_line = stdin.readline().rstrip().split(' ')
        a,b=map(int, input_line)
        st=struct(a,b)
        A.append(st)
    A.sort()
    ans=0
    time=0
    for x in A:
        # print(x.a,x.b)
        if(time>M):
            continue
        if((time+x.b)<=M):
            ans += x.a*x.b
            time += x.b
        else:
            ans += x.a*(M-time)
            time = M
    print(ans)



if __name__ == "__main__":
    main()
    