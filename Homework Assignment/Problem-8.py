arr = [-12, 11, -13, -5, 6, -7, 5]
neg = []
pos = []

for x in arr:
    if x < 0:
        neg.append(x)
    else:
        pos.append(x)

print(neg + pos)
