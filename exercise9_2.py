from functions import *

# ask user for input in one line format using split():
hours, minutes, sec = input("Enter accordingly the following info: hours, munites and seconds. "
                            "Please, use space to separate numbers! \n").split()
print("{}h {}min {}sec".format(hours, minutes, sec))

# calculating total amount of sec using created function:

total_sec = count_seconds(hours, minutes, sec)
print(f"{total_sec} seconds in total.")








