n,x=map(int,input().split())

bagaAtsusas=[]
bagaAtsusasP=[]
def bagaAtsusa(number):
  if number==0:
    bagaAtsusas.append(1)
    return 1
  else:
    tmp=3+ bagaAtsusa(number-1)*2
    bagaAtsusas.append(tmp)
    return tmp

def bagaAtsusaP(number):
  if number==0:
    bagaAtsusasP.append(1)
    return 1
  else:
    tmp=1 + bagaAtsusaP(number-1)*2
    bagaAtsusasP.append(tmp)
    return tmp

#どのバーガーまであるのかを知りたい
def donoBaga(bagaLevel,fukasa,numList,ans):
  if(fukasa==1):
    numList[bagaLevel-1]=0
    #今までのを足せばわかる
    for i in range(bagaLevel-1,len(numList)):
      ans+=bagaAtsusasP[i]*numList[i]
    print(ans)
  elif(fukasa<bagaAtsusas[bagaLevel-1]+1):
    #つぎへ
    numList[bagaLevel-1]=0
    fukasa=fukasa-1
    donoBaga(bagaLevel-1,fukasa,numList,ans)
  elif (fukasa==bagaAtsusas[bagaLevel-1]+1):
    numList[bagaLevel-1]=1
    #今までのを足せばわかる
    for i in range(bagaLevel-1,len(numList)):
      ans+=bagaAtsusasP[i]*numList[i]
    print(ans)
  elif (fukasa==bagaAtsusas[bagaLevel-1]+2):
    numList[bagaLevel-1]=1
    #今までのを足せばわかる
    for i in range(bagaLevel-1,len(numList)):
      ans+=bagaAtsusasP[i]*numList[i]
    ans=ans+1
    print(ans)
  elif(fukasa<bagaAtsusas[bagaLevel-1]*2+2):
    #つぎへ
    numList[bagaLevel-1]=1
    fukasa=fukasa-(bagaAtsusas[bagaLevel-1]+2)
    ans=ans+1
    donoBaga(bagaLevel-1,fukasa,numList,ans)
  elif (fukasa==bagaAtsusas[bagaLevel-1]*2+2):
    numList[bagaLevel-1]=2
    #今までのを足せばわかる
    for i in range(bagaLevel-1,len(numList)):
      ans+=bagaAtsusasP[i]*numList[i]
    ans=ans+1
    print(ans)
  elif (fukasa==bagaAtsusas[bagaLevel-1]*2+3):
    numList[bagaLevel-1]=2
    #今までのを足せばわかる
    for i in range(bagaLevel-1,len(numList)):
      ans+=bagaAtsusasP[i]*numList[i]
    ans=ans+1
    print(ans)
    
bagaAtsusa(n)
bagaAtsusaP(n)
numList=[0]*n
ans=0
donoBaga(n,x,numList,ans)
#print(numList)
#print(bagaAtsusas)
#print(bagaAtsusasP)