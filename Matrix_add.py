n = int(input('enter the row '))
a = []
b = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
print('Enter the second arry')
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    b.append(row)
# add the matrix
for i in range(n):
    for j in range(n):
        print(a[i][j]+b[i][j],end=" ")
    print(end="\n")
