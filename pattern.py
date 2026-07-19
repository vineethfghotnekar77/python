def pattern(n):
    if (n==0):
        return ""
    print("*"*n)
    return pattern(n-1)

a=pattern(int(input("Enter the number:")))
print(a)