'''
@Author: Nayan Tripathi
@Date: 2022-03-29 10:00:00
@Title : Quadratic
'''

import cmath
from distutils.errors import CompileError

class complexerror:
    def quadratic():
        a=int(input("Enter a: "))
        b=int(input("Enter b: "))
        c=int(input("Enter c: "))
        d=(b**2)-(4*a*c)
        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)
        try:
            if(d<0):
                raise CompileError
            else :
                    print('The solution are {0} and {1}'.format(sol1,sol2))
        except CompileError:
                print('Roots are imaginery so calculation stopped')

obj=complexerror
obj.quadratic()