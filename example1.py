from z3 import *
x,y = Ints('x y')
s = Solver()
s.add(x + y > -5)
s.add(x - y < 5)
s.add( Or (2*x - y < 15 ,  x + 3*y >7))
print(s.check())
print(s.model())
