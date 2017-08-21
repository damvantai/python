import tensorflow as tf 

a = tf.constant(2)

b = tf.constant(3)

x = tf.add(a, b)
init = tf.global_variables_initializer()
with tf.Session() as sess:
	# add this line to use Tensorboard
	sess.run(init)
	writer = tf.summary.FileWriter('./graphs', sess.graph)
	print (sess.run(x))

writer.close()

