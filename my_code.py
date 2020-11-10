# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def avg_temp():
    with open('temps.txt') as file_object_3:
        line_list = file_object_3.readlines()

    list_length = len(line_list)
    for i in range(list_length):
        line_list[i] = line_list[i].rstrip()
        line_list.remove('High Temps October 2020') # why not remove

    length = len(line_list)
    total = sum(line_list)
    average = total/length

    return average


if __name__ == '__main__':
    print(avg_temp())

