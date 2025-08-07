# Author: KaLee

def average(*args):
  """Function to provide average of numbers provided.
  Usage: average(1, 2, 3, 4, 5) returns 3 && average(1, 2, 3) returns 2. This support varying length of arguments"""
  if not args:
    return None # (or) raise ValueError('Values not provided')
  return sum(args)/len(args)

def centroid(*args):
  """Function to provide centroid of any number of points in heterogenous dimensions
  Usage: centroid([1, 2, 3], [1, 2], [1], [2, 3, 4, 5, 6, 7]) returns output as [1.25, 1.75, 1.75, 1.25, 1.5, 1.75]"""
  from itertools import zip_longest
  if not args:
    return None # (or) raise ValueError('Values not provided')
  return [sum(i)/len(i) for i in zip_longest(*args, fillvalue = 0.0)]
