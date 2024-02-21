import datetime

five_days_ago = datetime.datetime.now() - datetime.timedelta(days=5)

print(five_days_ago)