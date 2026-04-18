sentence = "python is easy and python is powerful"

# Step 1: Split sentence into words
words = sentence.split()

# Step 2: Count frequency
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
