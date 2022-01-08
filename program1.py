import time
import datetime;

# print current time
print(time.time())
print(time.asctime(time.localtime(time.time())))
# or
print(time.asctime())
datetime_object = datetime.datetime.now()
print("Year: ", datetime_object.year())
print("Month: ", datetime_object.month())
print("Day: ", datetime_object.day())
print("Hour: ", datetime_object.hour())

import calendar;

s = calendar.prcal(2022)

count = 5


def increment():
    global count
    count = count + 1
    local = 10
    print(count, local)


increment()
