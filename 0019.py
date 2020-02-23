from datetime import date,timedelta
from dateutil.relativedelta import *
sundays=0
T=date(1901,1,1)
while T<date(2000,12,31):
    if T.weekday()==6:
        sundays+=1
    T+=relativedelta(months=1)
print(sundays)