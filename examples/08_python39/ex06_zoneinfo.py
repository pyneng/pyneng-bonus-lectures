from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

# all zones
# zoneinfo.available_timezones()

meeting = datetime(2021, 5, 16, 10, 0, tzinfo=ZoneInfo("Europe/Kiev"))

# meeting.utcoffset()
# datetime.timedelta(seconds=10800)
# h = timedelta(hours=1)
# meeting.utcoffset() / h

# In [5]: meeting
# Out[5]: datetime.datetime(2021, 5, 16, 10, 0, tzinfo=zoneinfo.ZoneInfo(key='Europe/Kiev'))

# In [6]: meeting.astimezone(ZoneInfo("Australia/Melbourne"))
# Out[6]: datetime.datetime(2021, 5, 16, 17, 0, tzinfo=zoneinfo.ZoneInfo(key='Australia/Melbourne'))


