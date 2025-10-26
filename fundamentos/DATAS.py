from datetime import datetime, date

nasc = input('digite data: ')
nasc_date = datetime.now()
print(nasc)
data = nasc_date.strftime('%d/%m/%Y')
data_nasc = datetime.strptime(nasc, '%d/%m/%Y')
idade = nasc_date - data_nasc
newIdade = idade.days / 365 - 1
print(nasc)
print(nasc_date)
print(data)
print(data_nasc)
print(idade)
print('{:.0f} anos'.format(newIdade))
