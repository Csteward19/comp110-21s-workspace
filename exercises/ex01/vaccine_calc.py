"""A vaccination calculator."""

__author__ = "730404260"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop_0 = str(input("Enter population: "))
doses_admin = int(input("Enter doses administered: "))
dose_day = int(input("Enter doses per day: "))
target = int(input("Enter target percent vaccinated: "))
pop_0 = int(pop_0)
e = float(((pop_0 * (target / 100)) - (doses_admin / 2)) / (dose_day / 2))
rounded_e = round(e)
today: datetime = datetime.today()
e_days: timedelta = timedelta(e)
future: datetime = today + e_days
f = future.strftime("%B %d, %Y")
target = str(target)
print('We will reach', target + '% vaccination', 'in', round(rounded_e, 0), 'days, which falls on', f)