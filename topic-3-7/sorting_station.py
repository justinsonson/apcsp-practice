label = input()

shape = label[0:4]
color= label[4:7]
size = int(label[7:10])
mass = int(label[10:14])
condition = label[14]

is_damaged = condition == "D"
is_oversize = size > 50
is_overweight = mass > 2000
needs_inspection = is_damaged or is_oversize or is_overweight

is_ball = shape == "BALL"
is_cube = shape == "CUBE"
is_red = color == "RED"
is_blue_or_green = color == "BLU" or color == "GRN"
is_small = size <= 10

if needs_inspection:
    print("INSPECT")
else:
    if is_ball:
        if is_red and not is_small:
            print("B")
        else:
            print("A")
    elif is_cube:
        if is_blue_or_green and is_small:
            print("C")
        else:
            print("D")
    else:
        print("E")