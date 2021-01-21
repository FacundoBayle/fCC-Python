def add_time(start, duration, day=None):

    days_of_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    start = start.split(" ")
    time = start[0]
    time_convention = start[1]
    initial_modifier = time_convention

    hour = int(time.split(":")[0]) + int(duration.split(":")[0])
    minutes = int(time.split(":")[1]) + int(duration.split(":")[1])
    days = 0
    day_count = ""
    hour_modifier = hour
    modifiers_later = 0

    if minutes > 59:
        hour += 1
        minutes -= 60

    hour_modifier = hour

    while hour > 12:
        hour -= 12

    while hour_modifier > 11:
        hour_modifier -= 12
        time_convention = "PM" if time_convention == "AM" else "AM"
        modifiers_later += 1

    if modifiers_later % 2 != 0:
        if initial_modifier == "PM":
            modifiers_later += 1
        else:
            modifiers_later -= 1

    days = int(modifiers_later / 2)

    if day:
        weekday = days_of_week.index(day.title())
        weekday_new = int((weekday + days) % 7)
        day_count = f", {days_of_week[weekday_new]}"

    if days == 1:
        day_count += " (next day)"
    elif days > 1:
        day_count += f" ({days} days later)"

    return f"{hour}:{str(minutes).zfill(2)} {time_convention}{day_count}"