def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n-1)
print(power(4,5))