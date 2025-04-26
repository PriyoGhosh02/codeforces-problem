def cla(dollar, count=0):
    if dollar == 0:
        return count  #it returns ans count 
    if dollar >= 100:
        return cla(dollar % 100, count + dollar // 100)
    elif dollar >= 20:
        return cla(dollar % 20, count + dollar // 20)
    elif dollar >= 10:
        return cla(dollar % 10, count + dollar // 10)
    elif dollar >= 5:
        return cla(dollar % 5, count + dollar // 5)
    else:
        return cla(0, count + dollar)  

dollar = int(input())
print(cla(dollar))
