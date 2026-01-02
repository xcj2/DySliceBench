import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def like_agc3(www):
	lkagc=['AGC','ACG','GAC']
	return  not (www in lkagc)

def like_agc(www,w):
	if www[0]+www[2]+w =='AGC':
		return False
	if www[0]+www[1]+w == 'AGC':
		return False
	return like_agc3(www[1]+www[2]+w)
	

def main():
	ll=['AAA','AAC','AAG','AAT','ACA',       'ACC', 'ACG', 'ACT',"AGA", "AGC",     "AGG", "AGT", "ATA", "ATC" ,"ATG",     "ATT", "CAA", "CAC", "CAG", "CAT",     "CCA", "CCC", "CCG", "CCT", "CGA" , "CGC" ,"CGG" ,"CGT" ,"CTA" ,"CTC" , "CTG" ,"CTT" ,"GAA" ,"GAC" ,"GAG" , "GAT" ,"GCA" ,"GCC" ,"GCG" ,"GCT" , "GGA" ,"GGC" ,"GGG" ,"GGT" ,"GTA" , "GTC" ,"GTG" ,"GTT" ,"TAA" ,"TAC" , "TAG" ,"TAT" ,"TCA" ,"TCC" ,"TCG" , "TCT" ,"TGA" ,"TGC" ,"TGG" ,"TGT" , "TTA" ,"TTC" ,"TTG" ,"TTT"]
	dll={}
	for i,w in enumerate(ll):
		dll[w]=i
	
	n = int(input())
	#b , c = IN()
	#s = input()
	#cc=[1]*64
	#cc[6]=0#ACG
	#cc[9]=0#AGC
	#cc[18]=0#CAG
	cll='AGCT'
	cc = [1 if like_agc3(w) else 0 for w in ll]
	for i in range(4,n+1):
		#print(i)
		ncc=[0]*64
		for word in ll:
			for c in cll:
				if like_agc(word, c):
					next_word=word[1:]+c
					ncc[dll[next_word]]+=cc[dll[word]]
					ncc[dll[next_word]] %= mod
		cc=ncc
	ret = sum(cc) % mod
	print(ret)
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)