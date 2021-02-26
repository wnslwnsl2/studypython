def pluslistEntries(a,b):
    return [ea+eb for ea,eb in zip(a,b)]

a = [1,2,3,4,5]
b = [1,1,1,1,1]

print(pluslistEntries(a,b))