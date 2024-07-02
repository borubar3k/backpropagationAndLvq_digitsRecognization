import nnet as net
import numpy as np
import math
import hickle as hkl


def pobieranieDanych():
    bazaDanych = []
    with open('bazaDanych.txt', 'r') as file:
        for line in file:
            bazaDanych.append(list(map(int, line.strip())))
    xTrain = np.array(bazaDanych).astype(float)
    yTrain = np.array([i % 10 for i in range(100)])
    return xTrain, yTrain


def lvqTraining(xt, y, lr, hckle, max_epoch, err_goal):
    SSE_vec = []
    label, train_idx = np.unique(y, return_index=True)
    W = xt[train_idx].astype(np.float64)
    filtrX = np.array([e for i, e in enumerate(xt) if i not in train_idx])
    filtrY = np.array([e for i, e in enumerate(y) if i not in train_idx])
    for epoch in range(1, max_epoch + 1):
        SSE = 0.0
        predicted_labels = []
        for i, x in enumerate(filtrX):
            d = [math.sqrt(sum((w - x) ** 2)) for w in W]
            Dmin = np.argmin(d)
            predicted_labels.append(label[Dmin])
            if filtrY[i] == label[Dmin]:
                W[Dmin] = W[Dmin] + lr * (x - W[Dmin])
            else:
                W[Dmin] = W[Dmin] - lr * (x - W[Dmin])
            SSE = net.sumsqr((W[Dmin] - x).reshape(1, -1)) / len(x)
        if epoch % 10:
            SSE_vec.append(SSE)
            print("Epoch: %5d | SSE: %5.5e" % (epoch, SSE))
        hkl.dump([SSE_vec], hckle)
        if SSE < err_goal or np.isnan(SSE) or np.isinf(SSE):
            print("Epoch: %5d | SSE: %5.5e" % (epoch, SSE))
            break
    return W, label


def lvqTest(x, W):
    weights, label = W
    d = [math.sqrt(sum((w - x) ** 2)) for w in weights]
    return label[np.argmin(d)]


X, Y = pobieranieDanych()
lr = 0.0001
maxEpoch = 5000
err_goal = 1e-10

#                                   EKSPERYMENT 4
# LR = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]
# HKL = ['lvqLR1.hkl', 'lvqLR05.hkl', 'lvqLR01.hkl', 'lvqLR005.hkl', 'lvqLR001.hkl', 'lvqLR0005.hkl']
# for lr, hckl in zip(LR, HKL):
#     weight, labels = lvqTraining(X, Y, lr, hckl, max_epoch=100, err_goal=1e-10)

#                                   EKSPERYMENT 5
# x0 = [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
# x1 = [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1]
# x2 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
# x3 = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1]
# x4 = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
# x5 = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]
# x6 = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# x7 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# x8 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
# x9 = [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
# xTest = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]
# zmienne = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
# polaczone = list(zip(xTest, zmienne))
# random.shuffle(polaczone)
# xTestLosowo, zmienneLosowo = zip(*polaczone)
# for x, z in zip(xTestLosowo, zmienneLosowo):
#     output = lvqTest(x, (weight, labels))
#     print('Zmienna:', z, 'przechowuje liczbę:', output)

#                                   EKSPERYMENT 6
weight, labels = lvqTraining(X, Y, lr, 'lvqPOROWNANIE.hkl', maxEpoch, err_goal)
