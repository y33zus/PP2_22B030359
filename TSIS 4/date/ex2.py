from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print("today :", date.today())
print("yesterday:", yesterday)
print("tommorow:", tomorrow)