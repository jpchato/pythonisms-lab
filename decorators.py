from functools import wraps
from time import time
# reference https://codereview.stackexchange.com/questions/169870/decorator-to-measure-execution-time-of-a-function

def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print ('Elapsed time: {}'.format(end-start))
        return result
    return wrapper

@timing
def f(a):
    for _ in range(a):
        pass

print(f(2000000))


#reference https://gist.github.com/jonathan-kosgei/a0e3fb78d81f9f3a09778ced6eca7161
import timeit

def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()

@timer
def addition():
  total = 0
  for i in range(0,1000000):
    total += i
  return total