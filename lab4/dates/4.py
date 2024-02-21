import datetime 
date_1 = datetime.datetime.now()


date_2 = datetime.datetime(2023, 1, 15, 16, 53, 11 , 22)

diff = date_1 - date_2

print(date_1)
print(date_2)

print(int(diff.total_seconds()))

print(diff.seconds + diff.days*86400)