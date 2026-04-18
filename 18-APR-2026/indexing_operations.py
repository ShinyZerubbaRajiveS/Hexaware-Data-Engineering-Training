# accessing elements at specified index
fruits=["apple","orange","grapes","banana","pineapple"]
print(fruits[0])
print(fruits[1])
print(fruits[-2])

# modify elements
numbers=[1,2,3,4,5]
numbers[1]= 200
print(numbers)

#add elements
numbers.append(6) #add one element at end
print(numbers)
numbers.extend([7,8,9]) # add more element at end
print(numbers)
numbers.insert(1,10) # insert at specified index
print(numbers)

#remove elements
numbers.remove(1)
print(numbers) # remove element 1
numbers.pop()
print(numbers) #remove last element

print(len(numbers))