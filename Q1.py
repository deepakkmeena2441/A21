def firstnatural(n):
    if n<1:
        return 1
    else:
        firstnatural(n-1)
        print(n)





n=int(input())
firstnatural(n)