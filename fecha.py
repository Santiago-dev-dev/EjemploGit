dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    dias_mes[1] = 29

dia = dia + 1

if dia > dias_mes[mes - 1]:
    dia = 1
    mes += 1

    if mes > 12:
        mes = 1
        año = año + 1

print("La nueva fecha es:", dia, "/", mes, "/", año)