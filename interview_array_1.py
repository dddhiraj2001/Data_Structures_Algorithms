def reverse(x):
    reverse_str=""
    for i in range(len(x)-1,-1,-1):
        reverse_str+=x[i]
    print(reversed(x))
    return reverse_str

print(type(2))
print(str([1,2,34,5]))
print(reverse("Fuck off"))