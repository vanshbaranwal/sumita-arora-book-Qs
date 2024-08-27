#write a program that reads an integer N from the keyboard computes and
#displays the sum of the numbers from N to (2*N) if N is nonnegative.
#if N is negative number, then it's sum of the numbers from (2*N) to N.
#the starting and ending pints are included in sum.

N=int(input("enter a number : "))
sum=0

if(N>0):
    for i in range(N,2*N+1):
        sum+=i

else:
    for i in range(2*N,N+1):
        sum+=i
        
print(f"\nthe sum of the numbers is {sum}.")

