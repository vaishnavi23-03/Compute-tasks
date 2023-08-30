import numpy

def arrays(arr):
    arr.reverse()
    arr2=arr
    a= numpy.array(arr2, float)
    
    return (a)

    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)