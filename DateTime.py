#  Date and Time functionality
"""
Farhan Javed - 11-19-2019
Date and time basic functionality code. Also includes working with Calendars.
Feel free to reach out : farhan.javed47@gmail.com
"""
from datetime import date
from datetime import datetime
from datetime import timedelta
import calendar


def main():

    today = date.today()
    print("Today's date = ", today)
    print("Today's date = " + str(today))
    print("Today's date = " + today.strftime("%d/%m/%Y"))
    print("Today's date = " + today.strftime("%A-%B-%Y"))
    # the strftime(format) function is used to format the date and print it out.
    # more information here : https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
    # use a comma ( , ) instead of plus ( + ) to print the date object without having to use the str() function.

    print("Printing individual components : ", today.day, today.month, today.year )
    print("Printing individual components : " + str(today.day) + str(today.month) + str(today.year))

    # also notice that the comma operator in the print function automatically put a space when printing out objects
    # which is not done by the plus operator since plus concatenates the two strings.

    print("Today's week day number is : ", today.weekday())
    # Weekday function returns the day of the week as an integer starting from Monday = 0 uptil Sunday = 6.
    # This can be used as a list iterator as well in functions.

    days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    print("Today's day : " + days[today.weekday()])
    datetime_now = datetime.now()
    print("Current date and time : ", datetime_now)

    t = datetime.time(datetime_now)
    print("Current Time : ", t)
    print(datetime_now.strftime("%a, %d %B, %y"))

    # localized version of date and time
    print(datetime_now.strftime("Locale date and time : %c"))
    print(datetime_now.strftime("Locale date: %x"))
    print(datetime_now.strftime("Local time : %X"))

    # formatted time

    print(datetime_now.strftime("Current time : %I:%M:%S %p"))
    print(datetime_now.strftime("Current time : %H:%M"))

    # mathematical operations on the date and time objects. We can use the timedelta class
    # we need to import the timedelta package from datetime

    print(timedelta(days=365, hours=5, minutes=1))
    print("Current date and time : ", datetime_now)
    print("One year later : " + str(datetime_now + timedelta(days=365)))
    print("3 weeks and 2 days later : " + str(datetime_now + timedelta(weeks=3, days=2)))

    t = datetime.now() - timedelta(weeks=1)
    print("One week ago it was : " + t.strftime("%A %B %d, %Y"))

    april_fools_day = date(today.year, 4, 1)

    if april_fools_day < today:
        print("April Fools day was %d days ago" % (today-april_fools_day).days)
        april_fools_day = april_fools_day.replace(year=today.year + 1)
        print("Days remaining in next April fools day : ", (april_fools_day-today).days)

    # to work with calendars we need to import the calendar package

    cal = calendar.TextCalendar(calendar.SUNDAY)  # tells the first day of the week
    formatted_cal = cal.formatmonth(2019, 11, 0, 0)

    html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_code = html_cal.formatmonth(2019, 11)

    # for i in cal.itermonthdays(2019, 11):  # 0s represent that those days belong to the previous/next month
    #   print(i)

    # For locale based month and day names
    for month in calendar.month_name:
        print(month)

    for day in calendar.day_name:
        print(day)

    #  for example if we want to have a team meeting on the first Friday of every month in 2020
    #  we can use the following piece of code.

    print("Team meeting in 2020 will be on : ")
    for meeting in range(1,13):  # 13 is non inclusive
        cal = calendar.monthcalendar(2020, meeting)
        week_one = cal[0]
        week_two = cal[1]

        if week_one[calendar.FRIDAY] != 0:
            meet_day = week_one[calendar.FRIDAY]
        else:
            meet_day = week_two[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[meeting], meet_day))


main()