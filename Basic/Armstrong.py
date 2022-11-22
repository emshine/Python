n=int(input("Enter the number"))
m=n
c=0
s=0
while n>0:
    n//=10
    c+=1
print("%d" %c)
n=m
while n>0:
    v=n%10
    s+=(v**c)

    n//=10

if s==m:
    print("The number %d is  an Armstrong number"%m)
else:
    print("The number %d is not an Armstrong number"%m)
