#FIBONACCI SERIES
    
def fib(n):
    if (n==1 || n==2):
        return(1)
     return(fib(n-1)+fib(n-2))
     
n=int(input("Enter a no."))
for i in range(2,n):

#IMP note for loop starts from 2 onwards

    print(fib(i))
    
