# Lista de dispositivos de computo
# La lista es mutable porque su contenido se puede cambiar
#               0            1         2            3
dispositivos =['Impresoras','Scanner','Camara web','Luces']
Ventas = [2021, 2022, 2023, 2024]
factura = [1200, 5000, 6000, 4500]
# Tuplas
# La tupla es inmutable por que su contenido no se puede cambiar
#            0        1              2       3
servidor = ('SUNAT', '198.23.0.10', 'Lima', 'admin')
# Reemplazar impresora por ventilador en la lista
dispositivos[0] = 'Ventilador'

print(dispositivos)
#Reemplazar SUNAT por INDECOPI
#Servidor[0] = 'INDECOPI'
#print(Servidor)