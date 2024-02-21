import datetime

today = datetime.datetime.now()

without_miliseconds = today.replace(microsecond=0)
print(today)
print(without_miliseconds)