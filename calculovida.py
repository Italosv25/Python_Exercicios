from datetime import date

nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
dia, mes, ano = map(int, nascimento.split("/"))

Data_Nascimento = date(ano, mes, dia)
Hoje = date.today()

Anos = Hoje.year - Data_Nascimento.year - ((Hoje.month, Hoje.day) < (Data_Nascimento.month, Data_Nascimento.day))
Meses = Anos * 12 + (Hoje.month - Data_Nascimento.month)
Dias = (Hoje - Data_Nascimento).days
Minutos = Dias * 24 * 60
Segundos = Minutos * 60

print(f"Idade em anos:    {Anos}")
print(f"Idade em meses:   {Meses}")
print(f"Idade em dias:    {Dias}")
print(f"Idade em minutos: {Minutos}")
print(f"Idade em segundos:{Segundos}")

