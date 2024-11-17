import datetime, time

def number_days_between(date1, date2):
    date_format = '%Y%m%d'
    datetime1 = datetime.datetime.strptime(str(date1), date_format)
    datetime2 = datetime.datetime.strptime(str(date2), date_format)
    delta = abs(datetime1-datetime2)
    print (delta.days)
    return

number_days_between(20231019, 20241101)