# exercise 9_1: define a function, which only prints info:
def show_personal_info():
    print("John Williams")
    print("Rovaniemi")
    print("Software engineer")


# exercise 9_2: define a function to calculate total amount of seconds:

def count_seconds(hours, minutes, sec):
    result = (int(hours) * 3600) + (int(minutes) * 60) + int(sec)
    return result

# exercise 9_3: function checks given by user serial number
# if requirements are met it returns a True Boolean value:


def magazine_serial_check(serial):
    match = False
    if serial[4] == "-":
        serial= serial.replace(serial[4],"")
        if len(serial) == 8 and serial.isdigit():
            match = True
    return match

# exercise 9_4:


def show_numbered_list(title, people):
    print(title)
    counter = 0
    for name in people:
        counter = 1 + counter
        print(f"{counter}. {name}")
    print("")

