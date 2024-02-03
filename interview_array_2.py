def merge_sor_arr(x,y):
    i,j=0,0
    mer_sor_arr=[]
    while i<len(x) and j<len(y):
        if x[i]<y[j]:
            mer_sor_arr.append(x[i])
            i+=1
        if y[j]<x[i]:
            mer_sor_arr.append(y[j])
            j+=1
        if x[i]==y[j]:
            mer_sor_arr.append(x[i])
            mer_sor_arr.append(y[j])
            i+=1
            j+=1
    if i == len(x):
        mer_sor_arr+=y[j:]
    if j == len(y):
        mer_sor_arr+=x[i:]
    return mer_sor_arr

print(merge_sor_arr([1,2,3,4,5],[]))

