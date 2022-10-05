def printn(n):
    if n>0:
        print(n)
        printn(n-1)


n=int(input())
printn(n)