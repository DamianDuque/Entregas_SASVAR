from datetime import datetime
from datetime import date

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)


dia = format(now.day)
mes = format(now.month)
anio = format(now.year)
hora = format(now.hour)
minuto = format(now.minute)
segundo = format(now.second)


if int(dia) < 10:
    str(dia)
    dia = '0' + dia
print(dia)

if int(mes) < 10:
    str(mes)
    mes = '0' + mes
print(mes)

anio = anio[2:]
print(anio)

if int(hora) < 10:
    str(hora)
    hora = '0' + hora
print(hora)

if int(minuto) < 10:
    str(minuto)
    minuto = '0' + minuto
print(minuto)

if int(segundo) < 10:
    str(segundo)
    segundo = '0' + segundo
print(segundo)


id = dia + mes + anio + hora + minuto + segundo
print(id)
