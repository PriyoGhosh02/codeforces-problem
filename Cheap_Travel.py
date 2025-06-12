n,m,a,b=map(int, input().split())
total=0

m_single_value=b/m
if m_single_value< a:
    total= (n//m)*b
    if (n%m)*a>b:
        total += b
    else:
        total += (n%m)*a
else:
    total= n*a

print(total)