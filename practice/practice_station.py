label = input("Input: ")

type = label[0:4]
color = label[4:7]
size = int(label[7:10])
weight = int(label[10:14])
condition = label[14]

if condition == "B" or size < 40 or weight > 300:
    print("DISCARD")
elif type == "APPL" and color == "RED" and size > 70:
    print("PREMIUM")
elif type == "APPL":
    print("STANDARD")
elif type == "PEAR" and (color == "GRN" or color == "YEL") and size <= 60:
    print("SNACK")
elif type == "PEAR":
    print("RESERVE")
else:
    print("MISC")

