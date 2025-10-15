#Author - kalaiselvan (KaLee)

import random
from typing import Sequence
def tria_gen(point1 :Sequence[float], point2 :Sequence[float], point3 :Sequence[float]):
    """Given three points in a list or tuple format, a generator is created yielding all points
uniformly distributed.
Usage: a = tria_gen([0, 0, 0], [1, 0,0], [1,1,0])
       for i in range(10):
          print(next(a)) #-> this should print 10 random points inside the triangle provided
       (or) you could write it to a file as shown below
       with open('d:/temp/triaPoints.csv', 'w') as f:
           for i in range(1000):
               pt = next(a)
               f.write(str(pt[0])+', ' + str(pt[1]) + ', ' + str(pt[2])+'\n')
"""
    while True:
        a = random.random()        # assume this is a percentage
        b = (1-a)*random.random()  # reminder of the percentage's percentage
        c = 1-a-b                  # negating a and b we will have this condition
                                   #        satisfied --> 0 <= a <= b <= c <= 1 &&
                                   #                      a + b + c = 1
        [x1, y1, z1], [x2, y2, z2], [x3, y3, z3] = point1, point2, point3
        yield [a*x1+b*x2+c*x3,
                a*y1+b*y2+c*y3,
                a*z1+b*z2+c*z3]
