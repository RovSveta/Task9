from functions import *

# ask user for input:
serial = input("Give an ISSN-serial:\n")

# call the function:
match = magazine_serial_check(serial)

# print results:
if match:
    print("Valid ISSN.")
else:
    print("Incorrect ISSN.")