from sympy import *
from sympy.plotting import plot

x = Symbol('x')
f = 5 * x ** 2 + 10 * x - 30
 
lst = [-oo, oo]
lst[1:1] = solveset(diff(f), x, Reals).evalf(2)
lst.sort()
grow = []
small = []
for i in range(1, len(lst)):
    tmp = is_increasing(f, Interval.open(lst[i - 1], lst[i]))
    print(tmp)
    if tmp:
        grow.append(f'{lst[i - 1], lst[i]}')
    else:
        small.append(f'{lst[i - 1], lst[i]}')
print(f' Increase interval: {grow}\n', f'Decrease interval: {small}')

plot(f, (x, -5, 5))

from random import uniform

lst = sorted(solveset(diff(f), x, Reals).evalf(2))
lst.insert(0, lst[0] - 1)
fdiff = diff(f)
peak = []
for i, val in enumerate(lst):
    peak.append(fdiff.subs(x, uniform(val, lst[i] + 1)))
    if i != 0:
        if peak[i - 1] < 0 < peak[i]:
            print(f'Point minimum: ({val},{f.subs(x, val).evalf(2)})')
        elif peak[i - 1] > 0 > peak[i]:
            print(f'Point maximum: ({val},{f.subs(x, val).evalf(2)})')

solveset(f > 0, x, Reals).evalf(2)

solveset(f < 0, x, Reals).evalf(2)

x = Symbol('x')
y = x ** 3 - 10 * x

