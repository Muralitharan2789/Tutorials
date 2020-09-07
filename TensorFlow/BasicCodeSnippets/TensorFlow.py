# -*- coding: utf-8 -*-
'''
Running a TensorFlow session involves the following steps:

Importing the desired library
Initializing the variables and constants
Placeholders for performing the computation
Initializing a Session on CPU or GPU
Performing the computation
Display results
Close Session
'''

#Simple Program

import tensorflow as tf
import numpy as np

# Initialize two constants
a1 = tf.constant([4,3,2,1])
a2 = tf.constant([1,3,4,7])

# Perform Multiplication
res = tf.multiply(a1, a2)

# Intialize the Session
sess = tf.Session()

# Print the result
print(sess.run(res))

# Close the session
sess.close()

#Handling Session Efficiently
# Initialize Session and run `result`
with tf.Session() as sess:
  finalOutput = sess.run(res)
  print(finalOutput)
  
#Constants - constant(value, dtype=None, shape=None, name='Const', verify_shape=False)

x = tf.constant(42, name="a", dtype=tf.float32)

#Variables
'''
In TensorFlow all the variables are in-memory buffers that have tensors. These tensors require initialization to be consumed in the data flow graph
'''
a = tf.Variable(tf.zeros([5]), name="a")
z = tf.Variable(tf.add(x, y), trainable=False)

#Placeholders - Placeholders are values that are initially unassigned but get initialized when the session is invoked.

placeholder(dtype, shape=None, name=None)


#Mathematics with Tensor flow
tensor_1d = np.array([1,2,3,4,5])

tensor_1d = tf.convert_to_tensor(tensor_1d, dtype=tf.int64)

with tf.Session() as session:
    print(session.run(tensor_1d))
    print(session.run(tensor_1d[0]))
    print(session.run(tensor_1d[1]))

array_2d_1 = np.array(np.arange(16).reshape(4,4), dtype='int32')

print(array_2d_1)

tensor_2d_1 = tf.convert_to_tensor(array_2d_1)


with tf.Session() as session:
    print (session.run(tensor_2d_1))
    
array_2d_1 = np.array(np.arange(16).reshape(4,4), dtype='int32')
array_2d_2 = np.array(np.arange(16,32).reshape(4,4), dtype='int32')

tensor_2d_1 = tf.convert_to_tensor(array_2d_1)
tensor_2d_2 = tf.convert_to_tensor(array_2d_2)

mat_add = tf.add(tensor_2d_1, tensor_2d_2)
mat_mul = tf.matmul(tensor_2d_1, tensor_2d_2)
array_2d_1 = np.array(np.arange(16).reshape(4,4), dtype='float64')
tensor_2d_1 = tf.convert_to_tensor(array_2d_1)
mat_det = tf.matrix_determinant(tensor_2d_1)

with tf.Session() as sess:
    print(sess.run(mat_add))
    print(sess.run(mat_mul))
    print(sess.run(mat_det))
    
#Linear Regression
numPts = 100
x = []
y = []
a = 0.45
b = 0.60

for i in range(numPts):
    xtemp = np.random.normal(0.0,0.5)
    ytemp = a*xtemp + b +np.random.normal(0.0,0.1)
    x.append([xtemp])
    y.append([ytemp])


#Initialize the Variables
A = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

yPred = tf.add(tf.multiply(A, x), b)

learningRate = 0.25

cost_function = tf.reduce_mean(tf.square(yPred - y))
optimizer = tf.train.GradientDescentOptimizer(learningRate)
train = optimizer.minimize(cost_function)

NumIter = 50
model = tf.initialize_all_variables()

with tf.Session() as session:
        session.run(model)

        for step in range(0,NumIter):
            session.run(train)
        ModelA = session.run(A)
        ModelB = session.run(b)
