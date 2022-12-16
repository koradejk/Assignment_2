def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
no=int(input("Enter the number:"))
result=fact(no)
print(result)