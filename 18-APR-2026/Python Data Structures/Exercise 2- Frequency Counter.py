numbers = [10,20,10,30,20,10,40]

#  1. Count how many times each number appears .
count={}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
#  2. Store the result in a dictionary
print(count)