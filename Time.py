# Use the if statement to check the time 

def convert_to_24_hour(hour, minute, period):
    if period == "am" and hour == 12:
        hour = 0
    elif period == "pm" and hour != 12:
        hour += 12
    
    return f"{hour:02d}:{minute:02d}"

print(convert_to_24_hour(7, 29, "pm"))