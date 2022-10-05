def multiples(n,N):
    if N>0:
        multiples(n,N-1)
        print(n*N)
        



n=int(input("enter the number"))
N=int(input("how many multiple of n is to print"))
multiples(n,N)