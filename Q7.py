def squareofn(n):
    if n>0:
        squareofn(n-1)
        print(n**2)
    



n=int(input())
squareofn(n)