# Neural network
# very simple toy game
# for machine learning with neural network
# iamtrask.github.io/2015/07/12/basic-python-network/

"""
# harsh version
import numpy as np
# input
x = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
# wanted output
y = np.array([[0, 1, 1, 0]]).T

syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for j in range(6000):
    l1 = 1 / (1 + np.exp( - (np.dot(X, syn0))))
    l2 = 1 / (1 + np.exp( - (np.dot(l1, syn1))))
    l2_delta = (y - l2) * (l2 * (1- l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
"""

import numpy as np
# from matplotlib import pyplot as plt


# sigmoid function
def nonlin(x, deriv=False):
    if(deriv is True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)  # locks seed

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1

print "Input"
print str(X[0]) + " " + str(X[1]) + " " + str(X[2]) + " " + str(X[3])
print ""
print "Wanted output"
print str(y[0]) + " " + str(y[1]) + " " + str(y[2]) + " " + str(y[3])
print ""
print "syn0:" + str(syn0[0]) + " " + str(syn0[1]) + " " + str(syn0[2])
print ""

for iter in xrange(10000):

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    if (iter % 1000) == 0:
        print str(l1[0]) + " " + str(l1[1]) + " " + str(l1[2]) + " " + str(l1[3])

    # how much did we miss?
    l1_error = y - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print ""
print "Output After Training:"
# print l1
print str(l1[0]) + " " + str(l1[1]) + " " + str(l1[2]) + " " + str(l1[3])
