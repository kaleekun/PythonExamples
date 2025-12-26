#Author - KaLee

import functools

def timedecorator(func): # takes in a function pointer
    @functools.wraps(func)     # --> makes sure, original function's documentation and other required attributes are copied to innerfunc below
    def innerfunc(*args, **kwds):
        import time
        start = time.time()
        i = func(*args, **kwds)   # this is remembered
        end = time.time()
        print(b-a, " seconds")
        return i # this matches with the return of actual function sent in.
    return innerfunc # this return statement is for timedecorator function.
# so far, with above code, what we have accomplished is that, wrapped the function that was passed.

def logdecorator(func): # takes in a function pointer
    @functools.wraps(func)     # --> makes sure, original function's documentation and other required attributes are copied to innerfunc below
    def innerfunc(*args, **kwds):
        with open(r"d:/temp/log.txt", "a") as file: # opening file
          file.write("Function started to run\n")
          i = func(*args, **kwds)   # this is remembered
          file.write("Function finished running\n")
          file.close() # close
        return i # this matches with the return of actual function sent in.
    return innerfunc # this return statement is for logdecorator function.

@logdecorator   # this is a cascaded decorator
@timedecorator  # this is equivalent to decoratedFunc = logdecorator(timedecorator(decoratedFunc))
def decoratedFunc():
    """dummy decorator, just for a simple demo"""
    print('decoratedFunc is called')
