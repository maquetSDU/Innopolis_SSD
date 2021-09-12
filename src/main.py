import cmath

print('keywords:\ntask1\ntask2\ntask3\ntask4')
a = input('task name:')
if a == 'task1':
    from task1 import decorator
elif a == 'task2':
    from task2 import decorator
elif a == 'task3':
    from task3 import decorator
elif a == 'task4':
    from task4 import decorator
else:
    print('Incorrect! Please, write ''task'' and task number!')


@decorator
def quad_eq(a, b, c):
    """
    Simple quadratic equation solver!!!
    param a: coefficient before x**2
    param b: coefficient before x
    param c: last coefficient
    """
    discr = (b ** 2) - (4 * a * c)
    first_answer = (-b - cmath.sqrt(discr)) / (2 * a)
    second_answer = (-b + cmath.sqrt(discr)) / (2 * a)
    return first_answer, second_answer


@decorator
def pascal_tri(n):
    """
    Pascal triangle from lab!!!
    param n: height of triangle
    """
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]


# first lambda function
func_lambda_1 = lambda x: x + x  # just addition
func_lambda_1.__doc__ = "It is addition lambda function. "
func_lambda_1 = decorator(func_lambda_1)

# second lambda function
func_lambda_2 = lambda x: x * x  # just multiplication
func_lambda_2.__doc__ = "It is multiplication lambda function."
func_lambda_2 = decorator(func_lambda_2)

# test cases
quad_eq(2, 3, 5)
func_lambda_1(1234568)
pascal_tri(12)
func_lambda_2(12345)

quad_eq(3, 5, 7)
func_lambda_1(1234568)
pascal_tri(12)
func_lambda_2(1234444)

# it allows to plot table
if a == 'task3' or a == 'task4':
    func_lambda_2.plot_table()

# test case for task4 with error...
if a == 'task4':
    quad_eq(3, 5, 7)
    func_lambda_1(1234568)
    pascal_tri()
    func_lambda_2(1234444)
