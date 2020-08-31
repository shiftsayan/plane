from enum import IntEnum
import datetime as dt

class Day(IntEnum):
    TODAY = -1
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SUNDAY = 5
    SATURDAY = 6


def get_next_datetime(day, hour=0):
    '''
    Takes in a day and an hour and returns the soonest possible datetime that is on the day and after the hour
    '''
    date = dt.datetime.now()

    # If after hour on day, return current time (with a 1 minute buffer)
    if date.weekday() == day and date.hour >= hour:
        return dt.datetime.now() + dt.timedelta(minutes=1)

    # Otherwise, increment date to required day and hour
    date += dt.timedelta(days=day-date.weekday())
    return dt.datetime(date.year, date.month, date.day, hour, 0, 0, 0)


def get_next_datetime_formatted(day, hour=0):
    date = get_next_datetime(day, hour)
    return date.strftime("%A, %-d %B") # Friday, 1 March