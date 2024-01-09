Challenge 1
a = np.arange(10,30)
print(a)

Challenge 2
a[-3:]
a[3:6]
a[12:]
a[::2]
Challenge 3
np.flip(a)
Challenge 4
b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
nz_indices # note this is a tuple
Challenge 5
from numpy.random import random
z = random((3,3,3))
z
Challenge 6
x = np.linspace(0, 100, num=9)
print(x)
x.shape
Challenge 7
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()
