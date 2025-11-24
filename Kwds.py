# Author - KaLee

def func(*args, **kwds): # --> This is the most general function and can mimic any other function. No wonder, its used in decorator
  print(args, kwds)   # - Prints tuple (args) and dictionary (kwds)
  print(*args, *kwds) # - Prints by streaming all values from tuple into print function as parameter and 
                      # - also streams all the keys from dictionary to print function
  print(**kwds)       # - This will work only if, the keywords in dictionary matches keyword arguments of the 'print' function

def func1(a, b, /, c, d, *, e): # --> Arguments before "/" are position only arguments. Arguments between "/" and "*" are both positional and keyword arguments.
  print(a, b, c, d, e)          # --> Arguments after "*" are keyword arguments only.

func1(1, 2, e = 90, c = 89, d = 34) #-> This calls the function correctly.
func1(a = 1, b = 2, e = 90, c = 89, d = 34) #-> This is an error, since, I have given first two arguments as keyword arguments.
