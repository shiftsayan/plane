from collections import namedtuple, OrderedDict

from meetings import m_gbm, m_watercooler, m_hack
from util import Day

PlaneSchema = namedtuple('PlaneSchema', 'id delivery_day meeting_details')


schema = OrderedDict([
    ('template', [ 
        PlaneSchema('weekly', Day.MONDAY, None),
    ]),
    ('reminder', [
        PlaneSchema('gbm', Day.THURSDAY, m_gbm),
        PlaneSchema('watercooler', Day.FRIDAY, m_watercooler),
        PlaneSchema('hack', Day.SATURDAY, m_hack),
    ]),
    ('longform', [
        PlaneSchema('default', Day.TODAY, None),
    ]),
])