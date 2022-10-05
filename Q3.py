def odd(n):
    if n>0:
        if n%2!=0:
            
            odd(n-1)
            print(n)
        else :
            n-=1
            odd(n)

n=int(input())
odd(n)

