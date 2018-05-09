Title: PyQt5 tutorial(Date and time)
Date: 2017-10-12 21:54:28
Category: PyQt
Tags: PyQt, Python

QDate, QTime, QDateTime
=======================

* PyQt5 has `QDate`, `QDateTime`, `QTime` classes to work with date and time.
* The `QDate` is a class for working with a calendar date in the Gregorian calendar. It has methods for determining the date, comparing, or manipulating dates.
* The `QTime` class works with a clock time. It provides methods for comparing time, determining the time and various other time manipulating methods.
* The `QDateTime` is a class that combines both QDate and QTime objects into one object.

Current date and time
=====================

* PyQt5 has `currentDate()`, `currentTime()` and `currentDateTime()` methods for determining current date and time.

```python
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))
```

UTC time
========

> The UTC (Universal Coordinated time) was chosen to be the primary time standard. UTC is used in aviation, weather forecasts, flight plans, air traffic control clearances, and maps. Unlike local time, UTC does not change with a change of seasons.

```python
from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Local datetime: ", now.toString(Qt.ISODate))
print("Universal datetime: ", now.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))
```

Number of days
==============

* The number of days in a particular month is returned by the `daysInMonth()` method and the number of days in a year by the `daysInYear()` method.

```python
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

d = QDate(1945, 5, 7)

print("Days in month: {0}".format(d.daysInMonth()))
print("Days in year: {0}".format(d.daysInYear()))
```

Difference in days
==================

* The `daysTo()` method returns the number of days from a date to another date.

```python
from PyQt5.QtCore import QDate

xmas1 = QDate(2016, 12, 24)
xmas2 = QDate(2017, 12, 24)
nextyear = QDate(2018, 1, 1)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last XMas".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next XMas".format(nofdays))

print("There are {0} days until next year".format(now.daysTo(nextyear)))
```

Datetime arithmetic
===================

* We often need to add or subtract days, seconds, or years to a datetime value.

```python
from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Today:", now.toString(Qt.ISODate))
print("Adding 12 days: {0}".format(now.addDays(12).toString(Qt.ISODate)))
print("Subtracting 22 days: {0}".format(now.addDays(-22).toString(Qt.ISODate)))

print("Adding 50 seconds: {0}".format(now.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 months: {0}".format(now.addMonths(3).toString(Qt.ISODate)))
print("Adding 12 years: {0}".format(now.addYears(12).toString(Qt.ISODate)))
```

Daylight saving time
====================

> Daylight saving time (DST) is the practice of advancing clocks during summer months so that evening daylight lasts longer. The time is adjusted forward one hour in the beginning of spring and adjusted backward in the autumn to standard time.

```python
from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()

print("Time zone: {0}".format(now.timeZoneAbbreviation()))

if now.isDaylightTime():
    print("The current date falls into DST time")
else:
    print("The current date does not fall into DST time")
```

Unix epoch
==========

> The Unix epoch is the time 00:00:00 UTC on 1 January 1970 (or 1970- 01-01T00:00:00Z ISO 8601). The date and time in a computer is determined according to the number of seconds or clock ticks that have elapsed since the defined epoch for that computer or platform.
> Unix time is the number of seconds elapsed since Unix epoch.

```python
from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch() 
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))
```

Julian day
==========

> Julian day refers to a continuous count of days since the beginning of the Julian Period. It is used primarily by astronomers. It should not be confused with the Julian calendar. The Julian Period started in 4713 BC. The Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC.

> The Julian Day Number (JDN) is the number of days elapsed since the beginning of this period. The Julian Date (JD) of any instant is the Julian day number for the preceding noon plus the fraction of the day since that instant. (Qt does not compute this fraction.) Apart from astronomy, Julian dates are often used by military and mainframe programs.

```python
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print("Gregorian date for today: ", now.toString(Qt.ISODate))
print("Julian day for today: ", now.toJulianDay()) 
```

Historical battles
==================

> With Julian day it is possible to do calculations that span centuries.

```python
from PyQt5.QtCore import QDate, Qt

borodino_battle = QDate(1812, 9, 7)
slavkov_battle = QDate(1805, 12, 2)

now = QDate.currentDate()

j_today = now.toJulianDay()
j_borodino = borodino_battle.toJulianDay()
j_slavkov = slavkov_battle.toJulianDay()

d1 = j_today - j_slavkov
d2 = j_today - j_borodino

print("Days since Slavkov battle: {0}".format(d1))
print("Days since Borodino battle: {0}".format(d2))
```


