def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours

print(minutes_to_hours(70))
print(minutes_to_hours(70) + 10)
print(seconds_to_hours(7200))
print(type(seconds_to_hours(7200)))
