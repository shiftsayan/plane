from collections import namedtuple, OrderedDict

from meetings import m_gbm, m_watercooler, m_hack
from util import Day

PlaneSettings = namedtuple('PlaneSettingsReminder', 'id delivery_day meeting_details')


schema = OrderedDict([
    ('template', [ 
        PlaneSettings('weekly', Day.MONDAY, None),
    ]),
    ('reminder', [
        PlaneSettings('gbm', Day.THURSDAY, m_gbm),
        PlaneSettings('watercooler', Day.FRIDAY, m_watercooler),
        PlaneSettings('hack', Day.SATURDAY, m_hack),
    ]),
    ('longform', [
        PlaneSettings('default', Day.TODAY, None),
    ]),
])