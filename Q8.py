def cubesofn(n):
    if n>0:
        cubesofn(n-1)
        print(n**3)
    
n=int(input())
cubesofn(n)