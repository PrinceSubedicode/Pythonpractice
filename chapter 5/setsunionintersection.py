# Define sets
A = {1, 2, 3}
B = {3, 4, 5}
C = {1, 2}

# Union
print("Union:", A | B)                 # or A.union(B)
print("Union:",A.union(B))


# Intersection
print("Intersection:", A & B)          # or A.intersection(B)

# Difference
print("A - B:", A - B)                 # or A.difference(B)
print("B - A:", B - A)                 # or B.difference(A)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)  # or A.symmetric_difference(B)

# Subset / Superset
print("C is subset of A:", C <= A)     # or C.issubset(A)
print("A is superset of C:", A >= C)   # or A.issuperset(C)
