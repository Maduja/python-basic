my_set={1,2,3}
my_set1={1,"hello",(1,2,3)}

print(my_set1)

my_set.add(4)
print(my_set)

my_set.update([3,4,5])
print(my_set)

my_set.remove(4)
print(my_set)

print('-----------------------------------------')

A={1,2,3}
B={2,3,4,5}

print(A|B)
print(A.union(B))
print(B.union(A))

print(A&B)
print(A.intersection(B))
print(B.intersection(A))

print(A-B)
print(B-A)


