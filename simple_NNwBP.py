# Previous simple Neural nets

# softmax, hot coding, cross entropy

import numpy as np
import pandas as pd

# Using a dataset with THREE label categories, 1, 2, and 3---------------
filename = "./data/clean.csv"
DF = pd.read_csv(str(filename))
print(DF.head())
from sklearn.model_selection import train_test_split
train, test = train_test_split(DF, test_size=0.33)
# n = len(DF)  # number of rows of entire X
n = len(train)
# Take the label off of X and make it a numpy array
TrainLabel = train["target"]
X = np.array(train.drop('target', axis=1))
# Set y to the label. Check the shape!
y = np.array(TrainLabel).T
y = np.array([y]).T
print("y is\n", y)
LR = .01
LRB = .01
# ................................................
# -*- coding: utf-8 -*-
"""
author: Xingyu Chen
"""

import numpy as np
import matplotlib.pyplot as plt


class neural_nets(object):

    @staticmethod
    def Sigmoid(value, deriva=False):
        if deriva:
            return value * (1 - value)
        return 1 / (1 + np.exp(-value))

    def __init__(self, X, y, bs, c, W1_x, W2_h):
        self.LR = 0.01
        self.X = X
        self.y = y

        self.bs = bs
        self.c = c
        self.W1_x = W1_x
        self.W2_h = W2_h

        self.z = None
        self.h = None
        self.z2 = None

        self.GA = False

    def train(self, X, y):
        output = self.FeedForward(X)
        self.BackProp(X, y, output)
        return output

    def FeedForward(self, X):
        # print("FeedForward:\n")
        self.z = (np.dot(X, self.W1_x)) + self.bs # X is n by c   W1  is c by h -->  n by h
        # print("Z1 is:\n", self.z)
        self.h = self.Sigmoid(self.z)  # activation function    shape: n by h
        # print("H is:\n", self.h)
        self.z2 = (np.dot(self.h, self.W2_h)) + self.c  # n by h  @  h by o  -->  n by o
        # print("Z2 is:\n", self.z2)
        output = self.Sigmoid(self.z2)
        # print("y^ is:\n", output)
        return output

    def BackProp(self, X, y, output):
        # print("\nBackProp:\n")
        # Y^ - Y
        self.output_error = output - y
        # print("Y^ - Y\n", self.output_error)
        # print("SIG Y^\n", self.Sigmoid(output, deriva=True))

        # (Y^ - Y)(Y^)(1-Y^)
        self.output_delta = self.output_error * self.Sigmoid(output, deriva=True)
        # print("D_Error (Y^)(1-Y^)(Y^-Y) is:\n", self.output_delta)

        # (Y^ - Y)(Y^)(1-Y^)(W2)
        self.D_Error_W2 = self.output_delta.dot(self.W2_h.T)  # D_Error times W2
        # print("W2 is\n", self.W2)
        # print(" D_Error times W2\n", self.D_Error_W2)

        # (H)(1 - H) (Y^ - Y)(Y^)(1-Y^)(W2)
        self.H_D_Error_W2 = self.D_Error_W2 * self.Sigmoid(self.h, deriva=True)
        # Note that * will multiply respective values together in each matrix

        # print("Derivative sig H is:\n", self.Sigmoid(self.h, deriva=True))
        # print("self.H_D_Error_W2 is\n", self.H_D_Error_W2)

        # ------UPDATE weights and biases ------------------

        #  XT  (H)(1 - H) (Y^ - Y)(Y^)(1-Y^)(W2)
        self.X_H_D_Error_W2 = X.T.dot(self.H_D_Error_W2)  # this is dW1

        # (H)T (Y^ - Y)(Y^)(1-Y^)
        self.h_output_delta = self.h.T.dot(self.output_delta)  # this is dW2

        # print("the gradient :\n", self.X_H_D_Error_W2)
        # print("the gradient average:\n", self.X_H_D_Error_W2/self.n)

        if self.GA == "True":
            print("Using average gradient........\n")
            # self.W1_x = self.W1_x - self.LR * (self.X_H_D_Error_W2 / 3)
            # self.W2_h = self.W2_h - self.LR * (self.h_output_delta / 3)  ## average the gradients
        # #print("New W1: \n", self.W1)
        else:
            # print("Using sum gradient........\n")
            self.W1_x = self.W1_x - self.LR * self.X_H_D_Error_W2  # c by h first set (input -> hidden) weights
            self.W2_h = self.W2_h - self.LR * self.h_output_delta  # adjusting second set (hidden -> output) weights
        # print("New W1: \n", self.W1_x)
        # print("New W2: \n", self.W2_h)
        # print("The b biases before the update are:\n", self.bs)
        self.bs = self.bs - self.LR * self.H_D_Error_W2
        # print("The H_D_Error_W2 is...\n", self.H_D_Error_W2)
        # print("Updated bs are:\n", self.bs)

        self.c = self.c - self.LR * self.output_delta
        # print("Updated c's are:\n", self.c)

        # # print("The W1 is: \n", self.W1_x)
        # print("The W1 gradient is: \n", self.X_H_D_Error_W2)
        # # print("The W1 gradient average is: \n", self.X_H_D_Error_W2/self.n)
        # print("The W2 gradient  is: \n", self.h_output_delta)
        # # print("The W2 gradient average is: \n", self.h_output_delta/self.n)
        # print("The biases b gradient is:\n", self.H_D_Error_W2)
        # print("The bias c gradient is: \n", self.output_delta)


# Set up
# X = np.array([[1, 2, 3], [-1, -2, -3], [3, 4, -2]])
#
# y = np.array([[1], [0], [0]])
#
# W1_x = np.array([[1, -1], [2, -2], [3, -3]])
#
# bs = np.array([[1, 2]])
#
# W2_h = np.array([[4], [5]])
#
# c = 3
InputNumColumns = 5  # columns
OutputSize = 1  # Categories
HiddenUnits = 5  # one layer with h units
# n = n  # number of training examples, n
print("Initialize NN\n")
# Random W1
W1_x = np.random.randn(InputNumColumns, HiddenUnits)  # c by h

print("INIT W1 is\n", W1_x)

# -----------------------------------------
# NOTE #
#
# The following are all random. However, you can comment this out
# and can set any weights and biases by hand , etc.
#
# ---------------------------------------------

W2_h = np.random.randn(HiddenUnits, OutputSize)  # h by o
print("W2 is:\n", W2_h)

bs = np.random.randn(1, HiddenUnits)
print("The b's are:\n", bs)
# biases for layer 1
c = np.random.randn(1, OutputSize)
print("The c is\n", c)
# bias for last layer

# Initial
NN = neural_nets(X, y, bs, c, W1_x, W2_h)

TotalLoss = []
AverageLoss = []
Epochs = 1000

for i in range(Epochs):
    print("Iteration ", i + 1)
    output = NN.train(X, y)

    print("Total Loss:", .5 * (np.sum(np.square(output - y))))
    TotalLoss.append(.5 * (np.sum(np.square(output - y))))

    print("Average Loss:", .5 * (np.mean(np.square((output - y)))))
    AverageLoss.append(.5 * (np.mean(np.square((output - y)))))


TestLabel = test["target"]
test = test.drop('target', axis=1)

## COnfusion Matrix Accuracies
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# print(y)
# print(np.round(output))
# print("\nThe true test labels are:")
# print(TestLabel)
# print("\nThe predict test labels are:")
# print(NN.FeedForward(test))
# cnf_matrix = confusion_matrix(TestLabel, np.round(NN.FeedForward(test)))
cnf_matrix = confusion_matrix(y, np.round(output))
print("\nThe confusion matrix is:")
print(cnf_matrix)

cnf = accuracy_score(y, np.round(output))
print("\nThe accuracy score is:")
print(cnf)
# Plot

fig1 = plt.figure()
ax = plt.axes()
x = np.linspace(0, 1000, Epochs)
ax.plot(x, TotalLoss)
plt.show()

fig2 = plt.figure()
ax = plt.axes()
x = np.linspace(0, 1000, Epochs)
ax.plot(x, AverageLoss)
plt.show()
