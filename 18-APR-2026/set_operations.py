set1={10,20,30}
set2={20,30,40,50}

#Combines all unique elements from both sets.
result1= set1.union(set2)
print(result1)

#Returns elements in the first set but not in the second
result2= set1.difference(set2)
print(result2)

# Returns only the elements present in both sets.
result3= set1.intersection(set2)
print(result3)

# Returns elements in either set, but not both
result4= set1.symmetric_difference(set2)
print(result4)