def even(n):
    if n>0:
        if n%2==0:
            print(n)
            even(n-1)
            
        else:
            n-=1
            even(n)




n=int(input())
even(n)