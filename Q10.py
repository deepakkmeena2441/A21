def reversethenumber(n):
    if n>0:
    
        print(n%10,end="")
        reversethenumber(n//10)




n=int(input("enter the number"))
reversethenumber(n)