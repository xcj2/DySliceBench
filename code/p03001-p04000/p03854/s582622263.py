S = str(input())
a= [0,1,2,3]

judge = False

class E():
	def ex(self,S):
		m = S.replace('eraser' , '2')
		return m
		
class e():
	def ex(self,S):
		m = S.replace('erase' , '2')
		return m
		
class D():
	def ex(self,S):
		m = S.replace('dreamer','3')
		return m
		
class d():
	def ex(self,S):
		m = S.replace('dream','3')
		return m
		
		

a[0] = E()
a[1] = e()
a[2] = D()
a[3] = d()

for i in range(4):
	for j in range(4):
		for k in range(4):
			for l in range(4):
				m = a[i].ex(S)
				m = a[j].ex(m)
				m = a[k].ex(m)
				m = a[l].ex(m)
				
				try:
					int(m)
					print('YES')
					judge = True
				except:
					pass
				if judge == True:break
			if judge==True:break
		if judge==True:break
	if judge==True:break
	
if judge == False:
	print('NO')