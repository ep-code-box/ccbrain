import tensorflow as tf

# 그래프의 구현 시작

x_train = [1, 2, 3]
y_train = [1, 2, 3] 

# Now we can use X and Y in place of x_data and y_data
# placeholder for a tensor that will be always fed using feed_dict

X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

# Variable : Tensorflow가 사용하는 변수
# trainable : Tensorflow가 학습하는 과정에서 스스로 변경시킴
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#hypothesis = x_train * W + b
hypothesis = X * W + b

# Cose / loss function : reduce_mean
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#Gradient Descent, Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# 그래프의 구현 종료

#Launch the grapsh in a session
sess = tf.Session()

#initialize global variables in the graph
sess.run(tf.global_variables_initializer())

# fit the line
for step in range(3001):
	cost_val, W_val, b_val, train_val = sess.run([cost, W, b, train],
		feed_dict = {X: [1, 2, 3, 4, 5],
					Y: [1.1, 2.1, 3.1, 4.1, 5.1]})
	if step % 20 == 0:
		print(step, cost_val, W_val, b_val)