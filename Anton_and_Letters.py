
str=input()
str=str.replace('{','')
str=str.replace('}','')
str=str.replace(' ','')
str=str.replace(',','')

str=set(str)
print(len(str))