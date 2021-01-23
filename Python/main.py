import numpy as np
import math
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import midaco

#  Function to determine three square components of given number
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


# MIDACO function for solving value=(4^a)(8b+7)
def problem_function(x):
    globals()
    f = [0.0] * 1  # Initialize array for objectives F(X)
    g = [0.0] * 3  # Initialize array for constraints G(X)

    # Objective functions F(X)
    f[0] = ((4**x[0])*((8*x[1])+7)) - val

    #  Equality constraints G(X) = 0 MUST COME FIRST in g[0:me-1]
    g[0] = ((4**x[0])*((8*x[1])+7)) - val  # = 0

    # Inequality constraints G(X) >= 0 MUST COME SECOND in g[me:m-1]
    g[1] = x[0]  # >= 0
    g[2] = x[1]  # >= 0

    return f, g

#  ======= MIDACO Setup of constant parameters =======  #

key = b'MIDACO_LIMITED_VERSION___[CREATIVE_COMMONS_BY-NC-ND_LICENSE]'

problem = {}  # Initialize dictionary containing problem specifications
option = {}  # Initialize dictionary containing MIDACO options

problem['@'] = problem_function  # Handle for problem function name
problem['o'] = 1  # Number of objectives
problem['n'] = 2  # Number of variables (in total)
problem['ni'] = 2  # Number of integer variables (0 <= ni <= n)
problem['m'] = 3  # Number of constraints (in total)
problem['me'] = 1  # Number of equality constraints (0 <= me <= m)
problem['xl'] = [0, 0]  # Set lower bound for x
#  problem['xu'] = [round(math.log(val, 4)), val]  # Set upper bound for x (SET BELOW)
problem['x'] = problem['xl']  # Here for example: starting point = lower bounds
option['maxeval'] = 10000  # Maximum number of function evaluation (e.g. 1000000)
option['maxtime'] = 60  # Maximum time limit in Seconds (e.g. 1 Day = 60*60*24)
option['printeval'] = 0  # Print-Frequency for current best solution (e.g. 1000)
option['save2file'] = 0  # Save SCREEN and SOLUTION to TXT-files [0=NO/1=YES]
option['param1'] = 0.0  # ACCURACY
option['param2'] = 0.0  # SEED
option['param3'] = 0.0  # FSTOP
option['param4'] = 0.0  # ALGOSTOP
option['param5'] = 0.0  # EVALSTOP
option['param6'] = 0.0  # FOCUS
option['param7'] = 0.0  # ANTS
option['param8'] = 0.0  # KERNEL
option['param9'] = 0.0  # ORACLE
option['param10'] = 0.0  # PARETOMAX
option['param11'] = 0.0  # EPSILON
option['param12'] = 0.0  # BALANCE
option['param13'] = 0.0  # CHARACTER
option['parallel'] = 0  # Serial: 0 or 1, Parallel: 2,3,4,5,6,7,8...


# Defining the range in which to find the sum of three squares
lower = int(input('Lower bound: '))
upper = int(input('Upper bound: '))
start = time.time()
result = []
ab_all = []
no_three = []
arr_degen = []
rng = np.arange(lower, upper + 1)
for i in np.nditer(rng):
    threes = np.asarray(ThreeSquares(i))
    arr_degen.append(threes[1])
    print(str(i))
    print('    ' + str(threes[0]))
    print('    Degeneracy: ' + str(threes[1]))
    if threes[1] == 0:
        no_three.append(str(i))
        val = i
        problem['xu'] = [round(math.log(val, 4)), val]  # Set upper bound for x
        # Determining the values of a and b in 4^a * (8b + 7)
        solution = midaco.run(problem, option, key)
        a = (round(solution['x'][0]))
        b = (round(solution['x'][1]))
        print('    a = ' + str(a))
        print('    b = ' + str(b))
        ab = [int(str(i)), a, b]
        ab_all.append(ab)

    else:
        a = 0
        b = 0
    result.append([i, threes[0], threes[1], a, b])
    print(':::::::::::::::')

# Setup of summary terminal printout and matplotlib plots
x_plot = rng
y_plot = np.asarray(arr_degen)
ab_plot = np.asarray(ab_all)
p = len(no_three)/rng.size
print('Number of values which cannot be the sum of three squares: ' + str(len(no_three)))
print('Density of such: ' + str(p))
end = time.time()
plt.figure(1)
plt.plot(x_plot, y_plot, '.')
plt.ylabel('Degeneracy')
plt.xlabel('n')
plt.title('Three squares degeneracies')
print('Duration: ' + str(round(end - start, 2)) + ' sec')
plt.figure(2)
ax = plt.axes(projection='3d')
ax.scatter(ab_plot[:,2], ab_plot[:,1], ab_plot[:,0])
ax.set_xlabel('b')
ax.set_ylabel('a')
ax.set_zlabel('n')
print(ab_plot)
plt.show()

