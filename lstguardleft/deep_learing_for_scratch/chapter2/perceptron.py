# chapter 2. Perceptron
#
# runnable 
# %run 

class perceptron(object):

	def __init__(self):
		print('perceptron is created')

	def AND(self, x1, x2):
		w1, w2, theta = 0.5, 0.5, 0.7
		tmp = x1*w1 + x2*w2 
		if tmp <= theta:
			return 0
		elif tmp > theta:
			return 1

if __name__ == "__main__":

	a = perceptron()
	print(a.AND(0, 0))
	print(a.AND(1, 0))
	print(a.AND(0, 1))
	print(a.AND(1, 1))

