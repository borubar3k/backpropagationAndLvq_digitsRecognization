import hickle as hkl
from matplotlib import pyplot as plt

[lbpSSE] = hkl.load('lbpPOROWNANIE.hkl')
[lvqSSE] = hkl.load('lvqPOROWNANIE.hkl')
plt.plot(lbpSSE, 'red', label='learnbpa')
plt.plot(lvqSSE, 'green', label='LVQ')

plt.xlabel('epochs')
plt.xscale('linear')
plt.ylabel('SSE')
plt.yscale('linear')
plt.title('epoch')
plt.grid(True)
plt.legend()
plt.show()
