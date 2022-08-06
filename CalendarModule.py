from datetime import datetime
d =input()
c = d.replace(" ","/")

datetime_object = datetime.strptime(c,'%m/%d/%Y')

print(datetime_object.strftime('%A').upper())
