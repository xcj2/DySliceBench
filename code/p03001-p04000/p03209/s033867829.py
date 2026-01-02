class christmas:
    def __init__(self,layers,levels):
        self.layers=layers
        self.levels=levels
        self.sum=[1]
        self.patty=[1]
    def num_patties(self):
        for i in range(self.levels):
            self.sum.append(2*self.sum[i]+3)
            self.patty.append(2*self.patty[i]+1)
        def f(layer,level):
            
            if layer==0:
                return 0
            temp=self.sum[level]
            if layer==temp:
                return self.patty[level]
            if layer>temp:
                if layer==temp+1:
                    return self.patty[level]+1
                return self.patty[level]+1+f(layer-temp-1,level)
            return f(layer-1,level-1)
        return f(self.layers,self.levels)
s=input().split()
level=int(s[0])
layer=int(s[1])
s=christmas(layer,level)
print(s.num_patties())