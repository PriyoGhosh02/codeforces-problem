n=int(input())
count=0

for i in range(n):
    s=input()
    if s=="Tetrahedron":
        count+=4
        continue
    if s=="Cube":
        count+=6
        continue
    if s=="Octahedron":
        count+=8
        continue
    if s=="Dodecahedron":
        count+=12
        continue
    if s=="Icosahedron":
        count+=20
        continue

print(count)
