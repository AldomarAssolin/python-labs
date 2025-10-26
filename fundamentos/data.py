
from datetime import datetime, date

today_date = datetime.now()
today = today_date.strftime('%d/%m/%Y')
actual_year = str(datetime.now().year)
#day
day = input('Dia: ')
if '1' >= day >= '31':
    print('ola')
else:
    day = day
#month
month = input('Mês: ')
#year
year = str(input('Year: '))

#date transform
nasc = '{}/{}/{}'.format(day, month, year)
nasc_date = datetime.strptime(nasc, '%d/%m/%Y')
birth_date = nasc_date.strftime('%d/%m/%Y')

print(birth_date)

