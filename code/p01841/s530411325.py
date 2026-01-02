def sToTree(S):
#    print(S)
    if len(S)==0:
        return 'N'
    c = 0
    left=0
    right=0
    #print(S)
    for i in range(len(S)):
        if S[i] =='(':
            c+=1
        elif S[i] ==')':
            c-=1
        elif c==0 and S[i]=='[':
            left=i
        elif c==0 and S[i] ==']':
            right=i
            break
#    print(S[right+1:len(S)-1],right,left)   
    return[sToTree(S[1:left-1]),int(S[left+1:right]),sToTree(S[right+2:len(S)-1])]
    
def dfs(S1,S2):
    if S1=='N' or S2=='N':
        return 'N'

    ret = [dfs(S1[0],S2[0]),S1[1]+S2[1],dfs(S1[2],S2[2])]
    return ret

def my_print(ans):
    if ans == 'N':
        return
    print('(',end='')
    my_print(ans[0])
    print(")[{0}](".format(ans[1]),end = '')
    my_print(ans[2])
    print(')',end='')

S1 = input()
S2 = input()


S1 = sToTree(S1)
S2 = sToTree(S2)

ans = dfs(S1,S2)
my_print(ans)
print()

