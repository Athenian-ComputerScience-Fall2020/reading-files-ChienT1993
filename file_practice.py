# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#


# Read temps.txt and print it without the blank line at the end
with open('temps.txt') as file_object_1:
    contents = file_object_1.read()
print(contents.rstrip())


# Read temps.txt line by line and print with no whitespace
with open('temps.txt') as file_object_2:
    for line in file_object_2:
        print(line.rstrip())


# Make a list of lines from the file
with open('temps.txt') as file_object_3:
    line_list = file_object_3.readlines()

list_length = len(line_list)
for i in range(list_length):
    line_list[i] = line_list[i].rstrip()

print(line_list)


# Edit the elements to eliminate whitespace in the list




