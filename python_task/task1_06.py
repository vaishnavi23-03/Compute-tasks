cube = lambda x: x*x*x
 
def fibonacci(n):
    a=[]
    if  n==0:
        
        return (a)
    
    a.append(0)
    if n==1:
        return (a)
    a.append(1)
    x=0
    y=1
    if n==2:
        return (a)
    
    for i in range(n-2):
        c=x+y
        a.append(c)
        x=y
        y=c
    return (a)
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))