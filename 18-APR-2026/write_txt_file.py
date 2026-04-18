with open("data.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Sneha\n")
    file.write("Arjun\n")
#write will overwrite the existing file

#append will add new lines to the file
with open("data.txt", "a") as file:
    file.write("Shiny\n")
    file.write("Zerubba\n")
    file.write("Rajive\n")

# write() → writes one string at a time
# writelines() → writes many strings at once
lang=["Python\n","Java\n","C++\n"]
with open("data.txt", "w") as file:
    file.writelines(lang)