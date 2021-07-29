def prime_num(x):
    n=1
    if x==1:
        print("1 is neither Prime number nor composite number")
    while (x!=0):
        n+=1
        i=2
        while(n%i!=0):
            i+=1
        if(n==i):
            print(n)
            x-=1
        
a=int(input("Enter the number:"))
prime_num(a)