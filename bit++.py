n=int(input())
st=[]
for i in range(n):
    st.append(input())
res=0
for i in range(n):
    if st[i][1]=='+':
        res+=1

    else:
        res-=1
print(res)