n = int(input("enter a no.:"))

def fact(n):

        if (n>0):
            return n*fact(n-1)
        else:
            return(1);
x=fact(n)
print("Factorial:",x)
