import inspect
import io
import datetime
from contextlib import redirect_stdout
from timeit import default_timer as timer
class decorator:

    arr = {}
    def __init__(self,func):
        self.calls = 0
        self.func=func

    def __call__(self,*args):
        self.args = locals()
        self.calls += 1
        try:
            # create .txt file
            with open('text.txt','a') as q:
                # put into .txt file all outputs from main.py
                with redirect_stdout(q) as f:
                    with redirect_stdout(io.StringIO()) as w:

                        start = timer()
                        out = self.func(*args)
                        end = timer()
                    s = w.getvalue()
                    # print all info about functions...
                    print(self.func.__name__ + ' call ' + str(self.calls) + ' executed in ' + str(end - start) + ' sec')
                    print('Name: ' + self.func.__name__)
                    print('Type: ' + str(type(self.func)))
                    print('Sign: ' + str(inspect.signature(self.func)))
                    print('Args: ' + str(args))
                    print('Doc: ' + str(self.func.__doc__))
                    print('Source: ' + str(inspect.getsource(self.func)))
                    print('Outputs: ', s)
                    print('function outputs: ', out, "\n")
                    decorator.arr[(self.func.__name__,id(self.func)) ]=end-start
        except Exception as err:
            with open('log.txt','a') as e:

                with redirect_stdout(e) as f:
                    print(datetime.datetime.now(), err)


    def plot_table(self):
        '''
        function, that plots ranking table
        '''
        q = dict(sorted(decorator.arr.items(), key=lambda item: item[1]))
        print('PROGRAM | RANK | TIME ELAPSED')
        count = 1
        for i in q:
            print(i[0],'\t',count,'\t',float(q[i])*1000,'ms')
            count += 1










