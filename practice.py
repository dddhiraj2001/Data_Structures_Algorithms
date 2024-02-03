x = [1,2,3,4,5]
y = [1,2,3,6,25]
dict={}
sum = 20
for i in x:
    if sum-i in dict:
        continue
    else:
        dict[sum-i]=True

for i in y:
    if i in dict:
        print("True")
        break
    else:
        continue
else:
    print("false")

print([None for x in range(5)])

