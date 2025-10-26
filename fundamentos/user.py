from datetime import datetime
from datetime import date

'''
gener = str(input('''
#Marque seu sexo:
#[1] ou [M] para masculino;
#[2] ou [F] para feminino.
'''.strip()))
email = str(input("Digite seu email: ".strip()))
phone = int(input('Digite seu telefone: '.strip()))
'''

date = date.today()
print('-='*20)
#name
name = str(input('Digite seu nome: ').strip())
if name.count(' ') >= 1:
    print('Digite apenas o primeiro nome: ')
    name = str(input('Digite seu nome: ').strip())
else:
    name = name
print(name.title())
print('-='*20)
#lastname
lastname = str(input('Digite seu sobrenome: '.strip()))
print('-='*20)
lastname = lastname.title().replace('De', 'de').replace('Da', 'da').replace('Dos', 'dos').replace('Das', 'das')
print(lastname)
print('-='*20)
#nickname
nickname = str(input('Digite seu nome de login: ').strip())
if nickname.count(' ') >= 1:
    print('O nickname não pode conter espaços.')
    nickname = str(input('Digite seu nome: ').strip())
else:
    nickname = nickname
print(nickname)
print('-='*20)
#birth date
today_date = datetime.now()
today = today_date.strftime('%d/%m/%Y')
actual_year = datetime.now().year
#day
day = input('Digite o dia do seu nascimento: ')
if(int(day) >= 31 or int(day) <=1):
    print('O dia deve ser entre 1 e 31.')
    day = input('Digite o dia do seu nascimento: ')
#month
month = input('Digite o mês do seu nascimento: ')
if(int(month) > 12 or int(month) <=1):
    print('O mês deve ser entre 1 e 12.')
    month = input('Digite o mês do seu nascimento: ')
#year
year = int(input('Digite o ano do seu nascimento: '))
if 1930 < year <= actual_year:
    year = year
else:
    print('O ano deve ser entre 1930 e ano atual.')
    year = input('Digite o ano do seu nascimento: ')
#date transform
nasc = '{}/{}/{}'.format(day, month, year)
nasc_date = datetime.strptime(nasc, '%d/%m/%Y')
birth_date = nasc_date.strftime('%d/%m/%Y')

print(birth_date)
print('-*'*20)

print('Cadastro concluído com sucesso!')
print('Dados cadastrados:')
print(f'Nome: {name.title()} {lastname}')
print(f'Nickname: {nickname}')
print(f'Data de nascimento: {birth_date} (Idade: {actual_year - year} anos)')
print(f'Data atual: {today}')
print('-*'*20)
print('Obrigado por se cadastrar!')

'''
print(gener)
print(email)
print(phone)
'''

'''
birth_date_ano = int(input('Digite o ANO do seu nascimento: '.strip()))
if 1920 < birth_date_ano <= date.year:
    birth_date_ano = birth_date_ano
else:
    print('Digite um valor entre 1920 e o ano atual.')
    birth_date_ano = int(input('Digite o ANO do seu nascimento: '.strip()))
birth_date = '{}/{}/{}'.format(birth_date_day, birth_date_month, birth_date_ano)
print(birth_date)
idade = date.today().year - birth_date_ano
print(idade, 'anos.')
'''



