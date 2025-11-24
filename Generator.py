# Author - KaLee

from typing import Iterator
import operator
from itertools import zip_longest
def myRange(start: int, stop: int|None = None, step: int|float = 1)->Iterator[int|float]:
  """This function is layed out as a generator to mimic 'range' builtin"""
  if stop is None:
    stop = start
    start = 0
  loopOp = operator.lt if step > 0 else operator.gt
  if abs(step):
    while(loopOp(start, stop)):
      yield start
      start += step


for i in zip_longest(range(10), myRange(10)):
  print(i)

for i in zip_longest(range(0,10), myRange(0,10)):
  print(i)

for i in zip_longest(range(0,10, 2), myRange(0,10, 2)):
  print(i)


for i in zip_longest(range(0,10, -2), myRange(0,10, -2)):
  print(i)

for i in zip_longest(range(10,0, 2), myRange(10,0, 2)):
  print(i)

for i in zip_longest(range(10,0, -2), myRange(10,0, -2)):
  print(i)
