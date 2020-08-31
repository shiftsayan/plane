from collections import namedtuple, OrderedDict

from meetings import m_gbm, m_watercooler, m_hack
from util import Day, get_next_datetime

DEFAULT_DELIVERY_TIME = 10 # AM


PlaneSchema = namedtuple('PlaneSchema', 'id subject delivery_day meetings')


schema = OrderedDict([
    ('template', [ 
        PlaneSchema('weekly', "ScottyLabs Meetings This Week", get_next_datetime(Day.MONDAY, DEFAULT_DELIVERY_TIME), {
            'gbm': m_gbm,
            'watercooler': m_watercooler,
            'hack': m_hack,
        }),
    ]),
    ('reminder', [
        PlaneSchema('gbm', "ScottyLabs GBM Reminder", get_next_datetime(Day.THURSDAY, DEFAULT_DELIVERY_TIME), {
            'reminder': m_gbm,
        }),
        PlaneSchema('watercooler', "ScottyLabs Watercooler Session Reminder", get_next_datetime(Day.FRIDAY, DEFAULT_DELIVERY_TIME), {
            'reminder': m_watercooler,
        }),
        PlaneSchema('hack', "ScottyLabs Hack Session Reminder", get_next_datetime(Day.SATURDAY, DEFAULT_DELIVERY_TIME), {
            'reminder': m_hack,
        }),
    ]),
    ('longform', [
        PlaneSchema('default', None, Day.TODAY, None),
    ]),
])