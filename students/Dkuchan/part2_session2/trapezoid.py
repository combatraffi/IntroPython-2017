# trapezoid.py
# this takes an arbitrary mathmatical function and computes
# the area under the function using the trapezoidal rule.trapezoidal


def mathfunc1(x):
    # parabola function
    return x**2 + 32.2


def mathfunc2(x):
    # line function
    return x + 10


def mathfunc3(x):
    return 10


def trapz(line, start, end, steps):
    area = 0
    stepvals = []
    mathfuncvals = []
    areas = []
    single_step = (end - start) / steps
    stepvals = [single_step * n for n in range(start, steps)]
    # print(stepvals)
    mathfuncvals = [line(stepvals[n]) for n in range(start, steps)]
    # print(mathfuncvals)
    areas = [(mathfuncvals[n] * single_step) + .5 * single_step * abs(mathfuncvals[n + 1] - mathfuncvals[n]) for n in range(start, steps-1)] 
    for i in range(start, steps - 1):
        area += areas[i]
    return area


print(trapz(mathfunc3, 0, 30, 10000))



''' 
get the step size from the user. 
Compute the y value of x at a given point.
compute the y value at x+1 steps.
area (to be summed to completion) = step size * x0 value + step size * .5* abs(x1-x0)
repeat until xn is reached 
'''


