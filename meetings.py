from collections import namedtuple

Meeting = namedtuple('Meeting', 'name day time zoom')

m_gbm = Meeting(
    'General Body Meeting',
    'Thursday',
    '6:30pm EDT/3:30pm PDT',
    'zoom',
)

m_watercooler = Meeting(
    'Watercooler Session',
    'Friday',
    '9:00pm EDT/6:00pm PDT',
    'zoom',
)

m_hack = Meeting(
    'Hack Session',
    'Saturday',
    '2:00pm EDT/11:00pm PDT',
    'zoom',
)