from codeop import Compile
from distutils.errors import CompileError
'''
@Author: Nayan Tripathi
@Date: 2022-03-29 10:00:00
@Title : Windchill
'''

import math

def Windchill():
    T = float(input("Enter the temperature in Fahrenheit."'\n'))
    print("You entered ",T, "degrees"'\n')
    V = float(input("Enter the wind speed."'\n'))
    print("You entered ",V, "MPH."'\n')
    windchill = 35.74+(0.6215)*T-35.75*math.pow(V,0.16)+0.4275*T*math.pow(V,0.16)
    try :
        if(T>50 or V>120):
            raise CompileError
        else :
            print("Windchill index : ", windchill)
    except CompileError:
        print("Temperature can not be greater than 50 degree and Wind speed can not be greater than 120")

Windchill()