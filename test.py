mat=[]
n=int(input())
m=int(input())
for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)

print(len(mat))
for row in mat:
    print(row)

