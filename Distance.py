'''
@Author: Nayan Tripathi
@Date: 2022-03-29 10:00:00
@Title : Distance
'''

from distutils.errors import CompileError
import math

def distance():

    print("Enter the first point A")
    x1, y1 = map(int, input().split())
    print("Enter the second point B")
    x2, y2 = map(int, input().split())
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    try :
        if (dist==0):
            raise CompileError
        else :
            print("The Euclidean Distance is " + str(dist))
        
    except CompileError:
        print("Distance can not be zero")

distance()