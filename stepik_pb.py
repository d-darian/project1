

n =  int(input())
r1 = []
r2 = []
for i in range(0, n*n):
    x = int(input())
    r1.append(x)


for i in range(0, n*n):
    x = int(input())
    r1[i] += x


for i in range(n):
   r2.append(r1[i])
   r1.pop(i)
   i-=1

print("Matrici")
# print
print(r1)
print(r2)
print(r1+r2)

