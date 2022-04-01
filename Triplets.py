'''
@Author: Nayan Tripathi
@Date: 2022-03-29 10:00:00
@Title : Quadratic
'''

def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
    if (found == False):
        print(" Triple does not exist ")

arr = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
    ele = int(input())
    arr.append(ele)
     
print(arr)
n = len(arr)
findTriplets(arr, n)