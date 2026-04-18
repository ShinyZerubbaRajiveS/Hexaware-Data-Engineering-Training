numbers=(10,20,30,40,50)
print(numbers) # tuple are immutable,
# cannot modify the elements
#use when storing confidential values

#accessing elements
fruits=('apple','banana','orange')
print(fruits[0])
print(fruits[1])
print(fruits[-2])
print(fruits[-1])

print(len(fruits))

fruits= ('apple','banana','orange')
for x in fruits:
    print(x)

# num= (1,2,3,4,5)
# num[1]=100
# print(num) ----> cannot happen because tuple are immutable