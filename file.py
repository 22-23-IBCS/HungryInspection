

lst = []
fact = 1
for i in range(1,25):
    fact = 1
    for n in range(1,i+1):
        fact = fact*n
    lst.append(fact)

print(sorted(lst))
