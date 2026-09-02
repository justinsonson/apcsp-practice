clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("seconds")

selected_index = 2

clock_value = clock_values[selected_index]
label = labels[selected_index]

bits = [
    clock_value // 32 % 2,
    clock_value // 16 % 2,
    clock_value // 8 % 2,
    clock_value // 4 % 2,
    clock_value // 2 % 2,
    clock_value // 1 % 2,
]

bit_text = (
    str(bits[0]) + str(bits[1]) + str(bits[2])
    + str(bits[3]) + str(bits[4]) + str(bits[5])
)

check_value = (
    bits[0] * 32 + bits[1] * 16 + bits[2] * 8
    + bits[3] * 4 + bits[4] * 2 + bits[5] * 1
)

print(f"{label}: {clock_value} -> {bit_text}")
print("original value:", clock_value)
print("reconstructed value:", check_value)