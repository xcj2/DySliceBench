# coding: utf-8
# Your code here!
n,x=[int(x) for x in input().split()]
burgurnum=["" for _ in [0]*51]
burgurnumP=["" for _ in [0]*51]
def burgurNumFunc(level):
    if burgurnum[level]=="":
        if level==0:
            burgurnum[level]=1
        else:
            burgurnum[level]=burgurNumFunc(level-1)*2+3
    return burgurnum[level]
def burgurnumPFunc(level):
    if burgurnumP[level]=="":
        if level==0:
            burgurnumP[level]=1
        else:
            burgurnumP[level]=burgurnumPFunc(level-1)*2+1
    return burgurnumP[level]
    
    
def burger(num,level):
    if level==0:
        return 1
    elif num==1:
        return 0
    elif 1<num<=1+burgurNumFunc(level-1):
        return burger(num-1,level-1)
    elif num==burgurNumFunc(level-1)+2:
        return burgurnumPFunc(level-1)+1
    elif burgurNumFunc(level-1)+2<num<=burgurNumFunc(level-1)*2+2-1:
        return burgurnumPFunc(level-1)+1+burger(num - burgurNumFunc(level-1)-2,level-1)
    else:
        return burgurnumPFunc(level-1)*2+1
    

print(burger(x,n))