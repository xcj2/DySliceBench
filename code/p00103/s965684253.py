class Baseball:

	def __init__(self, score = 0):
		self.inning = Inning()
		self.game_score = score

	# def get_game_score(self):
	# 	return self.game_score

	def change(self):
		del self.inning
		self.inning = Inning()

	def batting(self, event):
		if event == 'HIT':
			self.inning.hit()
		elif event == 'HOMERUN':
			self.inning.homerun()
		elif event == 'OUT':
			self.inning.out()
		else:
			print('Error')

	def check_outcnt(self):
		return bool(self.inning.get_outcnt() != 3)

	# def update_score(self):
	# 	self.game_score += self.inning.get_score()

	def run(self):
		while self.check_outcnt():
			self.batting(input())
		# self.update_score()
		print(self.inning.get_score())
		self.change()


class Inning:

	def __init__(self, score = 0, outcnt = 0):
		self.base = Base()
		self.score = score
		self.outcnt = outcnt

	def hit(self):
		self.score += self.base.update(1)

	def homerun(self):
		self.score += self.base.update(4)
		self.base.clear()

	def out(self):
		self.outcnt += 1

	def get_outcnt(self):
		return self.outcnt

	def get_score(self):
		return self.score


class Base:
	def __init__(self):
		self.runner = [0, 0, 0]
	
	def update(self, num):
		score = 0
		for _ in range(num):
			score += self.runner.pop(0)
			self.runner.append(1)
		return score

	def clear(self):
		self.runner = [0, 0, 0]

def main():
	game = Baseball()
	for _ in range(int(input())):
		game.run()

if __name__ == '__main__':
	main()
