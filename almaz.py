myList = [1, 2, 3, 4, 5]
result = 'net double'
for i in myList:
    double = 0
    for j in myList:
        if i == j:
           double=double+1
    if double > 1 :
        result = "est double"
print(result)
