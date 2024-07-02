import hickle as hkl
from matplotlib import pyplot as plt


[SSE1] = hkl.load('lbpMC_6.hkl')
[SSE2] = hkl.load('lbpMC_7.hkl')
[SSE3] = hkl.load('lbpMC_8.hkl')
[SSE4] = hkl.load('lbpMC_9.hkl')
[SSE5] = hkl.load('lbpMC_95.hkl')
[SSE6] = hkl.load('lbpMC_99.hkl')
plt.plot(SSE1, 'red', label='mc=0.6')
plt.plot(SSE2, 'green', label='mc=0.7')
plt.plot(SSE3, 'blue', label='mc=0.8')
plt.plot(SSE4, 'yellow', label='mc=0.9')
plt.plot(SSE5, 'magenta', label='mc=0.95')
plt.plot(SSE6, 'cyan', label='mc=0.99')
plt.xlabel('epochs')
plt.ylabel('SSE')
plt.yscale('linear')
plt.title('epoch')
plt.grid(True)
plt.legend()
plt.show()
