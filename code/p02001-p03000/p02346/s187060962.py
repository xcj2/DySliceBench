class SegTree:
    '''Segment Tree:
    Data structure to answer queries on segments of a sequence.
    '''
    def __init__(self,n,init_num,func):
        '''Create a segment tree.
        :param n: Size
        :type n: int or float (number)
        :param init_num: Initialization number
        :type init_num: int or float (number)
        :param func: Function to use
        :type func: function
        '''
        self.func=func
        self.init_num=init_num
        self.size = 2**(len(bin(n-1))-2)*2-1
        self.tree = [init_num for i in range(self.size)]
     
    def data(self):
        '''Return data.
        '''
        return self.tree[self.size//2:]
 
    def update(self,i,x,update_func):
        '''Update the i-th data by update_func.
            example:
            a[i]<-update_func(a[i],x)
        '''
        i=self.size//2+i
        self.tree[i]=update_func(self.tree[i],x)
        while 1:
            i=(i-1)//2
            self.tree[i]=self.func(self.tree[i*2+1],self.tree[i*2+2])
            if i<=0:
                break
 
    def _check(self,s,t,l,r,_p=0):
        if s<=l and r<=t:
            return self.tree[_p]
        elif r<s or t<l:
            return self.init_num
        else:
            return self.func(self._check(s,t,l,l+(r-l)//2,_p*2+1),self._check(s,t,l+(r-l)//2+1,r,_p*2+2))
 
    def find(self,s,t):
        '''Answer queries on [s,t]segment
        '''
        return self._check(s,t,0,self.size//2)

n,q=map(int,input().split())
st=SegTree(n,0,lambda x,y:x+y)
for i in range(q):
    c,x,y=map(int,input().split())
    if c:
        print(st.find(x-1,y-1))
    else:
        st.update(x-1,y,lambda x,y:x+y)

