steps = [8200, 6100, 9450, 7300, 5000]
title = "daily step tracker"   

print(steps[0], steps[2], steps[-1])

steps[1] = 86
print(steps)

steps.append(93)

weekly_part = title[0:6]
report_part = title[13:19]
print(weekly_part)
print(report_part)

label = weekly_part + ": " + str(len(steps))

print(label, steps)

# 7. Why list elements can be replaced but string characters cannot:
# Lists in Python are mutable objects, so individual elements can be
# reassigned in place (scores[1] = 86 modifies the same list object).
# Strings, however, are immutable -- once created, their character
# data cannot be changed. Any "modification" (like slicing/concatenation)
# actually creates a brand-new string object rather than editing the
# original one in place.