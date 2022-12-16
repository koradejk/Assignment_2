

x=int(input("Enter the number:"))
print("Factors of",x,"is:")
for i in range(1,x+1):
    if x%i==0:
        print(i,end="  ")
n=str(i)
def sum(n):
    s=0
    for i in range(1,x+1):
        if x%i==0:
            s+=i
    return s
print()
print("Addition of Factor is:"+str(sum(n)))


