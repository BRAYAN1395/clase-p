'''Ingrese nombre del empleado, horas y minutos trabajados y el coto por hora para allar el importe a pagar'''

# int (integer) entero
#flotar (flotante) decimal
print('-------------------------------')
print('CALCULO DE HORAS TRABAJADAS')
print('-------------------------------')

xnom = input('Ingrese nombre:')
xhoras = int(input('Ingrese horas trabajadas:'))
xmin = int (input('Ingrese minutos trabajados :'))
xcosto = float(input('Ingrese el costo por hora:'))

# Calcular
total = xcosto * xhoras + (xcosto/60)*xmin
print('RESULTADOS')
print('Horas tranajadas: ', xhoras)
print('Minutos trabajados : ', xmin)
print('Total a pagar es  : ',(int (total*100))/100 )
