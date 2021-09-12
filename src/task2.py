import inspect
import io
from contextlib import redirect_stdout
from timeit import default_timer as timer
def decorator(func):
    '''
    Decorator function, that
    shows information about main.py functions
    like: Name of function; Type of function;
        Sign;Arguments; Docstring; Source code;
        and function output
    param func: function from main.py
    '''
    calls=0

    def task(*args):
        nonlocal calls
        calls+=1
        start=timer()
        # we temporarily put main.py functions outputs to f
        with redirect_stdout(io.StringIO()) as f:
            out = func(*args)

        end=timer()
        s = f.getvalue()
        args = locals()
        # print all info...
        print(func.__name__ +' call '+ str(calls) + ' executed in '+ str(end-start) + ' sec')
        print('Name: '+func.__name__)
        print('Type: '+str(type(func)))
        print('Sign: '+str(inspect.signature(func)))
        print('Args: ' + str(args['args']))
        print('Doc: '+str(func.__doc__))
        print('Source: '+str(inspect.getsource(func)))
        print('Outputs: ', s)
        print('function outputs: ', out,"\n")
    return task



