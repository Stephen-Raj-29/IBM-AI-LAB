s=input("Enter the 1 matrix row X col ").split("x")
n=int(s[0])
m=int(s[1])
print(n,m)
a=[]
b=[]
c=[]
for i in range(n):
    for j in range(m):
        x = int(input())
        c.append(x)
    a.append(c)
    c=[]

s1 = input("Enter the 2 matrix row X col ").split("x")
n1=int(s1[0])
m1=int(s1[1])
print(n1,m1)
for i in range(n1):
    for j in range(m1):
        x = int(input())
        c.append(x)
    b.append(c)
    c=[]

