import hickle as hkl
import numpy as np
import nnet as net


def pobieranieDanych():
    bazaDanych = []
    with open('bazaDanych.txt', 'r') as file:
        for line in file:
            bazaDanych.append(list(map(int, line.strip())))
    xTrain = np.array(bazaDanych[10:]).astype(float)
    yTrain = np.array(bazaDanych[:10]).astype(float)
    return xTrain, yTrain


def learnbpaTrain(x, y_t, max_epoch, err_goal, lr, L, mc, K1, K2, K3, hkle):
    SSE_vec = []
    w1, b1 = net.nwtan(K1, L)
    w2, b2 = net.nwtan(K2, K1)
    w3, b3 = net.rands(K3, K2)
    w1_t_1, b1_t_1, w2_t_1, b2_t_1, w3_t_1, b3_t_1 = w1, b1, w2, b2, w3, b3
    for epoch in range(1, max_epoch + 1):
        y1 = net.tansig(np.dot(w1, x), b1)
        y2 = net.tansig(np.dot(w2, y1), b2)
        y3 = net.purelin(np.dot(w3, y2), b3)
        e = y_t - y3
        d3 = net.deltalin(y3, e)
        d2 = net.deltatan(y2, d3, w3)
        d1 = net.deltatan(y1, d2, w2)
        dw1, db1 = net.learnbp(x, d1, lr)
        dw2, db2 = net.learnbp(y1, d2, lr)
        dw3, db3 = net.learnbp(y2, d3, lr)
        w1 += dw1
        b1 += db1
        w2 += dw2
        b2 += db2
        w3 += dw3
        b3 += db3
        w1_temp, b1_temp, w2_temp, b2_temp, w3_temp, b3_temp = \
            w1.copy(), b1.copy(), w2.copy(), b2.copy(), w3.copy(), b3.copy()
        w1 += dw1 + mc * (w1 - w1_t_1)
        b1 += db1 + mc * (b1 - b1_t_1)
        w2 += dw2 + mc * (w2 - w2_t_1)
        b2 += db2 + mc * (b2 - b2_t_1)
        w3 += dw3 + mc * (w3 - w3_t_1)
        b3 += db3 + mc * (b3 - b3_t_1)
        w1_t_1, b1_t_1, w2_t_1, b2_t_1, w3_t_1, b3_t_1 = w1_temp, b1_temp, w2_temp, b2_temp, w3_temp, b3_temp
        SSE = net.sumsqr(e)
        SSE_vec.append(SSE)
        if SSE < err_goal or np.isnan(SSE):
            break
    print("Epoch: %5d | SSE: %5.5e " % (epoch, SSE))
    hkl.dump([SSE_vec], hkle)


X, Y = pobieranieDanych()
maxEpoch = 5000
err_goal = 1e-10
lr = 0.0001
L = X.shape[0]
mc = 0.9
K1 = 50
K2 = 35
K3 = Y.shape[0]
#                                       EKSPERYMENT 1
# LR = [0.001, 0.0005, 0.0003, 0.0002, 0.0001, 0.00005]
# HKL = ['lbp001.hkl', 'lbp0005.hkl', 'lbp0003.hkl', 'lbp0002.hkl', 'lbp0001.hkl', 'lbp00005.hkl']
# for lr, hklee in zip(LR, HKL):
#     learnbpaTrain(x, y_t, maxEpoch, err_goal, lr, L, mc, K1, K2, K3, hklee)

#                                       EKSPERYMENT 2
# K1 = [120, 90, 70, 50, 30, 20]
# K2 = [90, 60, 45, 35, 25, 10]
# HKL = ['lbp120_90.hkl', 'lbp90_60.hkl', 'lbp70_40.hkl', 'lbp50_35.hkl', 'lbp30_25.hkl', 'lbp20_  10.hkl']
# for k1, k2, hklee in zip(K1, K2, HKL):
#     learnbpaTrain(X, Y, maxEpoch, err_goal, lr, L, mc, k1, k2, K3, hklee)

#                                       EKSPERYMENT 3
# MC = [0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
# HKL = ['lbpMC_6.hkl', 'lbpMC_7.hkl', 'lbpMC_8.hkl', 'lbpMC_9.hkl', 'lbpMC_95.hkl', 'lbpMC_99.hkl']
# for mc, hklee in zip(MC, HKL):
#     learnbpaTrain(X, Y, max_epoch, err_goal, lr, L, mc, K1, K2, K3, hklee)

#                                       EKSPERYMENT 6
learnbpaTrain(X, Y, maxEpoch, err_goal, lr, L, mc, K1, K2, K3, 'lbpPOROWNANIE.hkl')