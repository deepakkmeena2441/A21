def odd(n):
    if n>0:
        if n%2!=0:
            print(n)
            odd(n-1)
            
        else :
            n-=1
            odd(n)

n=int(input())
odd(n)

