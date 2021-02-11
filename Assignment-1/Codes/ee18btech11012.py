import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex

x = [1,2,3,4,2,1]
#Assuming length of x(n) and h(n) as same
N = len(x)
def h(N):
	h = []
	for i in range(N):
		out = 0;
		if i >= 0:
			out = out+((-0.5)**i)
		if i-2 >= 0:
			out = out+((-0.5)**(i-2))
		h.append(out)
		
	return h

def DFT(f):
	F = []
	N = len(f)
	for k in range(N):
		out = 0 * 1j
		for n in range(N):
			out=out+(f[n]*np.exp(-1j*2*np.pi*k*n/N))
		F.append(out)
	return F
h=h(N)
print ("DFT of x(n)\n",DFT(x))
print()
print ("DFT of h(n)\n",DFT(h))

fig , ax = plt.subplots(nrows = 3, ncols = 2, figsize=(12,14))

ax[0][0].stem(range(0,N),x)
ax[0][0].set_title(r'$x(n)$')
ax[0][0].grid()

ax[0][1].stem(range(0,N),h)
ax[0][1].set_title(r'$h(n)$')
ax[0][1].grid()

ax[1][0].stem(range(0,N),np.abs(DFT(x)))
ax[1][0].set_title(r'$|DFT(x)|$')
ax[1][0].grid()

ax[1][1].stem(range(0,N),np.angle(DFT(x)))
ax[1][1].set_title(r'$phase(DFT(x))$')
ax[1][1].grid()

ax[2][0].stem(range(0,N),np.abs(DFT(h)))
ax[2][0].set_title(r'$|DFT(h)|$')
ax[2][0].grid()

ax[2][1].stem(range(0,N),np.angle(DFT(h)))
ax[2][1].set_title(r'$phase(DFT(h))$')
ax[2][1].grid()
#If using termux
plt.savefig('../figs/ee18btech11012.pdf')
plt.savefig('../figs/ee18btech11012.eps')
subprocess.run(shlex.split("termux-open ../figs/ee18btech11012.pdf"))
#else
#plt.show()

