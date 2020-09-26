from collections import namedtuple
from util import Day, get_next_datetime_formatted

Meeting = namedtuple('Meeting', 'name date time zoom')

m_gbm = Meeting(
    'General Body Meeting',
    get_next_datetime_formatted(Day.THURSDAY),
    '6pm ET',
    'http://href.scottylabs.org/zoom',
)

m_watercooler = Meeting(
    'Watercooler Session',
    get_next_datetime_formatted(Day.FRIDAY),
    '9pm ET',
    'zoom',
)

m_hack = Meeting(
    'Hack Session',
    get_next_datetime_formatted(Day.SATURDAY),
    '1pm ET',
    'http://href.scottylabs.org/tech-zoom',
)

m_planning = Meeting(
    'Weekly Planning Meeting',
    get_next_datetime_formatted(Day.SATURDAY),
    '12pm ET',
    'http://href.scottylabs.org/planning-zoom',
)