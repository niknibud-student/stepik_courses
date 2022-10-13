from datetime import date, timedelta
Date = [int(x) for x in input().split()]
Days = int(input())
new_date = date(Date[0], Date[1], Date[2]) + timedelta(days=Days)
print(*[int(x) for x in str(new_date).split('-')])