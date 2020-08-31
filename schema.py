from collections import namedtuple, OrderedDict

from meetings import m_gbm, m_watercooler, m_hack
from util import Day

PlaneSchema = namedtuple('PlaneSchema', 'id delivery_day meetings')


schema = OrderedDict([
    ('template', [ 
        PlaneSchema('weekly', Day.MONDAY, {
            'gbm': m_gbm,
            'watercooler': m_watercooler,
            'hack': m_hack,
        }),
    ]),
    ('reminder', [
        PlaneSchema('gbm', Day.THURSDAY, {
            'reminder': m_gbm,
        }),
        PlaneSchema('watercooler', Day.FRIDAY, {
            'reminder': m_watercooler,
        }),
        PlaneSchema('hack', Day.SATURDAY, {
            'reminder': m_hack,
        }),
    ]),
    ('longform', [
        PlaneSchema('default', Day.TODAY, None),
    ]),
])