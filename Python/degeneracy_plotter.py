import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ThreeSquares(x):
    abc = []
    x_ = []
    y_ = []
    z_ = []
    degen = 0
    a = 0
    while a ** 2 <= x:
        b = a
        while b ** 2 <= x:
            c = b
            while c ** 2 <= x:
                if a ** 2 + b ** 2 + c ** 2 == x:

                    x_.append(a)
                    x_.append(b)
                    x_.append(c)
                    y_.append(degen)
                    y_.append(degen)
                    y_.append(degen)
                    z_.append(1)
                    z_.append(2)
                    z_.append(3)

                    degen = degen + 1

                c = c + 1
            b = b + 1
        a = a + 1
    if degen == 0:
        return 0, 0
    else:
        return abc, degen, x_, y_, z_


# ----------- #
n = 9998
# ----------- #

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlabel('Value')
ax.set_ylabel('Degeneracy')
ax.set_zlabel('ABC')

combos, d, x, y, z = ThreeSquares(n)
xs = np.asarray(x)
ys = np.asarray(y)
zs = np.asarray(z)
i = 0
for i in range(d):
    a = i * 3
    new_x = [xs[a], xs[a+1], xs[a+2]]
    new_y = [ys[a], ys[a+1], ys[a+2]]
    new_z = [zs[a], zs[a+1], zs[a+2]]
    ax.plot(new_x, new_y, new_z)

print(d)

plt.show()
