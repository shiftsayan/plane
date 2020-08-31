from collections import namedtuple
from util import Day, get_next_datetime_formatted

Meeting = namedtuple('Meeting', 'name date time zoom')

m_gbm = Meeting(
    'General Body Meeting',
    get_next_datetime_formatted(Day.THURSDAY),
    '6:00pm EDT/3:00pm PDT',
    'zoom',
)

m_watercooler = Meeting(
    'Watercooler Session',
    get_next_datetime_formatted(Day.FRIDAY),
    '9:00pm EDT/6:00pm PDT',
    'zoom',
)

m_hack = Meeting(
    'Hack Session',
    get_next_datetime_formatted(Day.SATURDAY),
    '2:00pm EDT/11:00am PDT',
    'zoom',
)