def isSubset(a, b):
    return set(b).issubset(set(a))

# Example
print(isSubset([11,7,1,13,21,3,7,3], [11,3,7,1,7]))
