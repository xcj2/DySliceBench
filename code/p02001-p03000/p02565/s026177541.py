class Two_SAT:
    """2-SATを定義する.

    """

    #入力定義
    def __init__(self,variable=[]):
        self.variable=set(variable)

        self.clause_number=0
        self.variable_number=len(variable)

        self.adjacent_out={(v,b):set() for v in variable for b in [True,False]} #出近傍(vが始点)
        self.adjacent_in={(v,b):set() for v in variable for b in [True,False]} #入近傍(vが終点)
        #※ (X,False)が not Xに対応

    #変数の追加
    def add_variable(self,*adder):
        """変数を加える.

        adder(可変長):加える変数の名前
        """
        for v in adder:
            if v not in self.variable:
                self.adjacent_in[(v,True)]=set()
                self.adjacent_in[(v,False)]=set()
                self.adjacent_out[(v,True)]=set()
                self.adjacent_out[(v,False)]=set()

                self.variable_number+=1
                self.variable.add(v)

    #節の追加
    def add_clause(self,X,F,Y,G):
        """(X=F) or (Y=G) という節を加える.

        X,Y:変数の名前
        F,G:真偽値(True or False)
        """

        assert isinstance(F,bool),"Fが真偽値ではない"
        assert isinstance(G,bool),"Gが真偽値ではない"

        for v in [X,Y]:
            if v not in self.variable:
                self.add_variable(v)

        if (Y,G) not in self.adjacent_out[(X,not F)]:
            self.clause_number+=1

            #(X,not F)→(Y,G)を追加
            self.adjacent_out[(X,not F)].add((Y,G))
            self.adjacent_in[(Y,G)].add((X,not F))

            #(Y,not G) → (X,F)を追加
            self.adjacent_out[(Y,not G)].add((X,F))
            self.adjacent_in[(X,F)].add((Y,not G))

    #節を除く
    def remove_edge(self,X,F,Y,G):
        pass

    #変数を除く
    def remove_vertex(self,*vertexes):
        pass

    #変数が存在するか否か
    def variable_exist(self,v):
        """変数 X が存在するか?

        X,Y:変数の名前
        """
        return v in self.variable

    #グラフに節が存在するか否か
    def clause_exist(self,X,F,Y,G):
        """(X=F) or (Y=G) という節が存在するか?

        X,Y:変数の名前
        F,G:真偽値(True or False)
        """
        if not(self.variable_exist(X) and self.variable_exist(Y)):
            return False
        return (Y,G) in self.adjacent_out[(X,not F)]

    #近傍
    def neighbohood(self,v):
        pass

    #出次数
    def out_degree(self,v):
        pass

    #入次数
    def in_degree(self,v):
        pass

    #次数
    def degree(self,v):
        pass

    #変数の数
    def variable_count(self):
        return len(self.vertex)

    #節の数
    def clause_count(self):
        return self.edge_number

    #充足可能?
    def Is_Satisfy(self,Mode):
        """有向グラフDを強連結成分に分解

        Mode:
        0(Defalt)---充足可能?
        1        ---充足可能ならば,その変数の割当を変える.(不可能なときはNone)
        """
        import sys
        from collections import deque

        T={(x,b):-1  for b in [True,False] for x in self.variable}
        Q=deque([])

        def f(v):
            T[v]=0
            for w in self.adjacent_out[v]:
                if T[w]==-1:
                    f(w)

            Q.appendleft(v)
            T[v]=len(Q)

        x=self.variable.pop()
        self.variable.add(x)

        RT=sys.getrecursionlimit()
        sys.setrecursionlimit(3*10**5)

        for b in [True,False]:
            for v in self.variable:
                w=(v,b)
                if T[w]==-1:
                    f(w)

        sys.setrecursionlimit(RT)

        T={(x,b):-1 for b in [True,False] for x in self.variable }
        C=[]
        p=0

        for v in Q:
            if T[v]==-1:
                T[v]=p
                P=[v]
                R=deque([v])

                while R:
                    u=R.popleft()
                    for w in self.adjacent_in[u]:
                        if T[w]==-1:
                            T[w]=p
                            R.append(w)
                            P.append(w)
                C.append(P)
                p+=1


        if Mode==0:
            for x in self.variable:
                if T[(x,True)]==T[(x,False)]:
                    return False

            return True
        else:
            X={x:None for x in self.variable}
            for x in self.variable:
                if T[(x,True)]==T[(x,False)]:
                    return None
                else:
                    X[x]=(T[(x,False)]<T[(x,True)])
            return X
#================================================
N,D=map(int,input().split())
X=[0]*N
Y=[0]*N

for i in range(N):
    x,y=map(int,input().split())
    X[i]=x
    Y[i]=y

T=Two_SAT(list(range(N))) # True→Xiに建てる,False→Yiに建てる
for i in range(N):
    for j in range(i+1,N):
        #XX
        if abs(X[i]-X[j])<D:
            T.add_clause(i,False,j,False)
        #XY
        if abs(X[i]-Y[j])<D:
            T.add_clause(i,False,j,True)

        #YX
        if abs(Y[i]-X[j])<D:
            T.add_clause(i,True,j,False)

        #YY
        if abs(Y[i]-Y[j])<D:
            T.add_clause(i,True,j,True)

H=T.Is_Satisfy(Mode=1)
if H==None:
    print("No")
else:
    Z=[0]*N
    for i in range(N):
        if H[i]:
            Z[i]=X[i]
        else:
            Z[i]=Y[i]

    print("Yes")
    print("\n".join(map(str,Z)))