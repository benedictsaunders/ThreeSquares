import numpy as np
import matplotlib.pyplot as plt

# Function to return a given integer x's combinations and degeneracy of the sum of Three-Squares

def ThreeSquares(x):
    abc = []
    degen = 0
    a = 0
    while a ** 2 <= x:
        b = a
        while b ** 2 <= x:
            c = b
            while c ** 2 <= x:
                if a ** 2 + b ** 2 + c ** 2 == x:
                    degen = degen + 1
                    abc.append([a, b, c])
                c = c + 1
            b = b + 1
        a = a + 1
    if degen == 0:
        return 0, 0
    else:
        return abc, degen

#
# Function to give an array, such as
# >>> updown(7)
#   [1, 2, 3, 4, 3, 2, 1]
#
#       OR
#
# >>> updown(8)
#   [1, 2, 3, 4, 4, 3, 2, 1]
#
# The returned array has 1 added to each term and then the reciprocal is given
# The example is given as above for simplicity
#

def updown(k):
    if k%2 == 0:
        even = True
    else:
        even = False
    arr = np.zeros(k)
    if even == True:
        for i in range(k):
            if i < k/2:
                arr[i] = i + 1
            elif i == k/2:
                arr[i] = arr[i - 1]
            else:
                arr[i] = k - i
    if even == False:
        for i in range(k):
            if i < (k + 1)/2:
                arr[i] = i + 1
            else:
                arr[i] = k - i
    arr = arr + 1
    arr = 1/arr
    return arr
    
# Begin main program #

i = 0
n = 1000
nz_counter = 0
ds = []
d_prob = []
nz_dist = []
max = int
n = int(input('Upper bound: '))

tagged = np.zeros(shape=(n+1, 4))
for i in range(n + 1):
    combs, d = ThreeSquares(i)
    ds.append(d)
i = 0
ds.append(0)
# Get distance between zeros
for i in range(n + 2):
    if ds[i] != 0:
        nz_counter = nz_counter + 1
    else:
        d_prob.append(1)
        nz_counter = 0
    nz_dist.append(nz_counter)
i = 0

for i in range(n + 1):
    # Populating array with:
    # [n values, distance from last 0, degeneracy, probability (set as 1, updated later)]
    tagged[i] = [i, nz_dist[i], ds[i], 1]
    if tagged[i][1] == 0:
        max = (tagged[i - 1][1].astype(int))
        probs = updown(max)
        # Populating probabilities, cycling though updown generated array
        # d = 0 skipped over to give default p = 1
        for l in range(max):
            tagged[i + l - max][3] = probs[l]
    else:
        None
print(tagged)
# Initialised np array with unplottable dimensions
# so transpose necessary (as only 2D)
x = tagged.transpose()[0]
y = tagged.transpose()[3]

# FT of probabilities
fourier = np.fft.fft(y)

# Making FT real and plottable
xft = [a.real for a in fourier]
yft = [a.imag for a in fourier]

#
# Here:
#
# x = x-axis of the number, n
# y = y-axis of probability
#
# xft = real axis of fourier transform of y
# yft = imaginary axis of fourier transform of y
#

plt.figure(1)
plt.plot(x, y)
plt.title('Probabilities of degen = 0 along Z')

plt.figure(2)
plt.title('Fourier Transform of Probabilities')
plt.plot(x, yft)

plt.show()
