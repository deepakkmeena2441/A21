def even(n):
    if n>0:
        if n%2==0:
            
            even(n-1)
            print(n)
        else:
            n-=1
            even(n)




n=int(input())
even(n)