#Print Function

N=int(input())
m=str(N)             #here of N is stored as a string in m which will be concatenated to our output
for i in range(1,N,1):
    j=N-i               #here we are subtracting value of i from N  and storing it as string in m to get desired output
    m=str(j) + m            #string concatenation
    print(m)
