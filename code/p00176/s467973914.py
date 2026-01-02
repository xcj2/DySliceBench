color = {
	'black' 	: '#000000',
	'blue' 		: '#0000ff',
	'lime' 		: '#00ff00',
	'aqua' 		: '#00ffff',
	'red' 		: '#ff0000',
	'fuchsia' 	: '#ff00ff',
	'yellow' 	: '#ffff00',
	'white' 	: '#ffffff',
}

def list_chunk(arr, n):
	return [arr[i:i+3] for i in range(0,15,n)]

def code2rgb(code):
	code = code.lstrip('#')
	r, g, b = [code[i:i+2] for i in range(0,len(code),2)]
	return [int(v, 16) for v in [r, g, b]]
def dk2(a, b):
	return sum([(a[i]-b[i])**2 for i in range(0,3)])


while True:
	v = input()
	if(v is '0'): break
	rgb = code2rgb(v)
	dks = [dk2(code2rgb(c), rgb) for c in color.values()]
	k = list(color.keys())
	print(k[dks.index(min(dks))])