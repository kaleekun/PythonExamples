# Author - KaLee

from typing import Iterator
def myRange(start: int, stop: int|None = None, step: int = 1)->Iterator[int|float]:
  """This function is layed out as a generator to mimic 'range' builtin"""
  if stop is None:
    stop = start
    start = 0
  i = start
  if(stepSize > 0):
    while(i < stop):
      yield i
      i += stepSize
  elif(stepSize < 0):
    while(i > stop):
      yield i
      i += stepSize
