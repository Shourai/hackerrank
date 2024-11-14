def timeConversion(s):
    hour = int(s[0:2])
    minute = s[3:5]
    second = s[6:8]
    am_or_pm = s[8:10]

    if "AM" in am_or_pm and hour >= 12:
        hour -= 12
    elif "PM" in am_or_pm and hour <= 11:
        hour += 12

    return(f"{hour:02}:{minute}:{second}")
    # Write your code here


s = "07:05:45PM"
s = "12:01:45AM"
s = "00:00:00AM"
print(timeConversion(s))
