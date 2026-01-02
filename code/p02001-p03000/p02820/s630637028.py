# D - Prediction and Restriction
def fight(i, win_t):
	global rsp
	global ans
	global track
	
	if past_t(i) != win_t:
		ans += rsp[win_t]
		track += win_t
	else:
		future_t_ = future_t(i)
	
		for t in rsp:
			if t != win_t and t != future_t_:
				track += t
				break


def past_t(count):
	# K回前の自分の手が何だったか確認する
	global k
	global track
	
	if count >= k:
		return track[count-k]
	else:
		return ''
		

def future_t(count):
	global k
	global cpu_t

	try:
		cpu = cpu_t[count+k]
		
		if cpu == 'r':
			return 'p'
		elif cpu == 's':
			return 'r'
		else:
			return 's'
	except:
		return ''
			

n, k = map(int, input().split())
r, s, p = map(int, input().split())

rsp = dict()
rsp['r'] = r
rsp['s'] = s
rsp['p'] = p

cpu_t = input()
track = ''
i = 0
ans = 0

for cpu in cpu_t:
	if cpu == 's':
		fight(i, 'r')
	elif cpu == 'p':
		fight(i, 's')
	else:
		fight(i, 'p')
										
	i += 1

	if i == 3:
		pass

print(ans)
#print(track)