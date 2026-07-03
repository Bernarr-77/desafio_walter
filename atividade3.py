from datetime import date

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mes de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

data_nascimento = date(ano,mes,dia)
data_hoje = date.today()
dias_totais =  data_hoje - data_nascimento

print(dias_totais)