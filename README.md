# Three Squares

A combination of three separate repos from a project from Summer, 2019. The inspiration was that not all integers an be formed by the sum of three squares, yet energy levels in a 3D potential well can only be formed by the sum of three squared intgers. It may therefore be a possibility that some levels are inaccessible, paricularly lower ones.

## Python
main.py calculates and prints the combinations of each integer that is the sum of three squares, as well as determining `a` and `b` for the equation `n = (8^a)(b+7)`, where n is the integer for which `n = x^2 + y^2 + z^2`. 

The degeneracy_plotter.py graphically shows the degeneracy combinations for a given integer.

The probility sctipt is used to determine the probability of getting a degeneracy of 0 when determining the sum-of-three-squares degeneracy along Z.

## C++
The C++ implementation is simply a faster calculation for combinations, and does not offer any additional functionality. Additioanlly, it does not plot frequencies/probabilities of different combinations.

## Dependencies
### Python
The python portion of this project uses the numpy, scipy and matplotlib packages, as well as the MIDACO solver, available [here](http://www.midaco-solver.com/)

### C++
As well as [MIDACO](http://www.midaco-solver.com/), the C++ requires Lava's implementation of [matplotlib for C++](https://github.com/lava/matplotlib-cpp) which is to be added as a header.
