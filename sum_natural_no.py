def sum(n):
    if n==0:
        return 0
    else:
        return sum(n-1)+n
print(sum(5))
#n=int(input("Enter the number to find sum of natural numbers:"))   
#print(f"The sum of first {n} natural numbers is: {sum(n)}") #
    