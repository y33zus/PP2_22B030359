from datetime import datetime, time
def date_diff_in_Seconds(date2, date1):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2022-02-26 20:37:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))