def isLeapYear(year):
    if str(year)[2::] == '00':
        if year % 400 == 0:
            return True
    else:
        if year % 4 == 0:
            return True
        else:
            return False

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
count = 0
for year in range(1901, 2001):
    if isLeapYear(year):
        months[1] = 29
    else:
        months[1] = 28

    for month in months:
        date = 0
        while date < month:
            date += 1
            day = (day % 7)
            day += 1
            if date == 1 and day == 6:
                count += 1

print(count)

# Output: 171
