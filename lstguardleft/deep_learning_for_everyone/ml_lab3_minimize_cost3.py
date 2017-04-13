# How to minimizer

import tensorflow as tf

X = [1, 2, 3]
Y = [1, 2, 3]

#W = tf.Variable(tf.random_normal([1]), name='weight') 
W = tf.Variable(5.0)
#X = tf.placeholder(tf.float32)
#Y = tf.placeholder(tf.float32)

# Our hypotesis for linear model
hypothesis = X * W

# cost / loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#Minimize: Gradient Descent using derivative

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)

#gvs = optimizer.

train = optimizer.minimize(cost)
#Launch the grapsh in a session
sess = tf.Session()

# in#initialize global variables in the graph
sess.run(tf.global_variables_initializer())


for step in range(100):
	print(step, sess.run(W))
	sess.run(train)


