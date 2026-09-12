# AP CSP Day 10: input/output scaffold, not a completed binary report.
# In your existing binary_clock_math.py, preserve your lists, labels, index,
# conversion, report features, and test comments. Use your existing variable names.
# These sample lists make this template runnable on its own.
values = [13, 45, 63]
labels = ["Sample A", "Sample B", "Sample C"]
selected_index = 0

# PROVIDED INPUT: Run, click the Terminal, type an integer, and press Enter.
# Text and decimal input handling is outside today's task.
values[selected_index] = int(input("Enter a number: "))
clock_value = values[selected_index]
selected_label = labels[selected_index]
print("You entered:", clock_value)

# YOUR CODE START
if clock_value < 0:
    print("Below zero")
elif clock_value >63:
    print("Too large for six bits")
else:
    bits_text = format(clock_value, "06b")
    check_value = int(bits_text, 2)
    print(selected_label + ": " + bits_text)

    if clock_value % 2 == 0:
        print("Even")
    else:
        print("Odd")

# YOUR CODE END

# OUTPUT PATTERNS: move/uncomment these only in the appropriate branches.
# print(selected_label + ": " + bit_text)
# print("Even")  # or print("Odd")
# print("Outside six-bit range")
