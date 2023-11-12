def unique_in_order(sequence):
    x=sequence
    a=[]
    index=list(range(len(x)))
    for i in index:
        if i==0:
             a.append(x[i])
        else:
            if x[i]==x[i-1]:
                continue
            else:
                a.append(x[i])
    return print(a)    

x=unique_in_order
x("AA")
