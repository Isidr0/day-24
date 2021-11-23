# Open a file, read the contents and save to a variable, print the contents, and then close the file.
# Closing the file will free up the resources it was using while open.

# file = open("my_file.txt")
# you can also use the "with" keyword. it works the same way as assigning a variable. but you don't need to close it.
# it will only stay open as long as it's being used with the indented code
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close()

# mode "w" will make the file writable. it will overwrite existing data.
# it will also create a new file if it doesn't already exist. "a" will append data to file.
# "r" is the default mode. which is read only.
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")