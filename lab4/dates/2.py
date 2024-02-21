import datetime

today = datetime.datetime.now()

yesterday = today - datetime.timedelta(days=1)

tommorow = today + datetime.timedelta(days=1)

print(f"{today},\n {yesterday},\n {tommorow}")