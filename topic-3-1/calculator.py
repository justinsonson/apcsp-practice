minutes_available = int(input("Minutes available: "))
breaks = int(input("Number of breaks: "))
break_minutes = int(input("Minutes per break: "))
transportation_minutes = int(input("Minutes for transportation: "))

work_minutes = minutes_available - breaks * break_minutes - transportation_minutes

print("Focused work minutes: ", work_minutes)