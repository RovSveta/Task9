from functions import *

# ask user for input:
people_string = input("Write all participants, separated by comma:\n")
print("")

# convert a text into a list:
people = people_string.split(",")

# remove extra space characters from each name (beginning and end)
people = [p.strip() for p in people]

# print the list of names in original order by calling the function:
title = "Original order:"
show_numbered_list(title, people)

# print the list of names sorted in alphabetic order by first name
# by calling the same function:
title = "Alphabetic order by first name:"
people = sorted(people)
show_numbered_list(title, people)

# print the list of names sorted in alphabetic order by second name
# by calling the same function:
title = "Alphabetic order by last name:"
people = [" ".join(reversed(p.split(" "))) for p in people]
people = sorted(people)
show_numbered_list(title, people)



