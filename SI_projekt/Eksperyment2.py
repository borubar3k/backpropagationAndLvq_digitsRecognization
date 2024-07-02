import hickle as hkl
from matplotlib import pyplot as plt


[SSE1] = hkl.load('lbp120_90.hkl')
[SSE2] = hkl.load('lbp90_60.hkl')
[SSE3] = hkl.load('lbp70_40.hkl')
[SSE4] = hkl.load('lbp50_35.hkl')
[SSE5] = hkl.load('lbp30_25.hkl')
[SSE6] = hkl.load('lbp20_10.hkl')
plt.plot(SSE1, 'red', label='K1=120, K2=90')
plt.plot(SSE2, 'green', label='K1=90, K2=60')
plt.plot(SSE3, 'blue', label='K1=70, K2=40')
plt.plot(SSE4, 'yellow', label='K1=50, K2=35')
plt.plot(SSE5, 'magenta', label='K1=30, K2=25')
plt.plot(SSE6, 'cyan', label='K1=20, K2=10')
plt.xlabel('epochs')
plt.ylabel('SSE')
plt.yscale('linear')
plt.title('epoch')
plt.grid(True)
plt.legend()
plt.show()
