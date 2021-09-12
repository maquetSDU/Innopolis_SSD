import io
from contextlib import redirect_stdout
from timeit import default_timer as timer
def decorator(func):
    '''
    Decorator function, that
    counts functions(from main.py) execution time
    and number of calls
    param func: function from main.py
    '''
    calls=0
    def task(*args):
        nonlocal calls
        calls+=1
        start=timer()
        # redirects main.py functions outputs to f, because we don't need them!
        with redirect_stdout(io.StringIO()) as f:
            func(*args)
        end=timer()
        print(func.__name__ +' call '+ str(calls) + ' executed in '+ str(end-start) + ' sec')

    return task
