label = input("Label: ")

shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
mass = int(label[10:14])
condition = [14]

if condition == "D" or size > 50 or mass > 2000:
    print("INSPECT")
elif color == "RED" and size > 10:
    print("B")
elif shape == "BALL":
    print("A")
elif shape == "CUBE" and (color == "BLU" or color == "GRN") and size <= 10:
    print("C")
elif shape == "CUBE":
    print("D")
else:
    print("E")

