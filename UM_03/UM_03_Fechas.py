#import datetime 
from datetime import datetime,timedelta

fecha_actual=datetime.now()
"""
print(type(fecha_actual))
print(f"La Fecha del Sistema {fecha_actual}")
print(f"El Año {fecha_actual.year}")
print(f"El Mes {fecha_actual.month}")
print(f"El Dia {fecha_actual.day}")
print(f"La Hora {fecha_actual.hour}")
print(f"Los Minutos {fecha_actual.minute}")
print(f"Los Segundo {fecha_actual.second}")
"""
#Operaciones entre Fechas
nueva_fecha=fecha_actual+timedelta(days=7)
#print(f"La Nueva Fecha es {nueva_fecha}")

#Conversion de Fechas
cadena_fecha="2023-08-25"
#strptime convierte de string a un objeto datetime
fecha_desde_cadena=datetime.strptime(cadena_fecha,"%Y-%m-%d")
#print(type(fecha_desde_cadena))
#print(f"La Fecha actual es {fecha_desde_cadena}")

#strftime para formatear un objeto datetime como una cadena de texto
fecha_dt=datetime(2022,3,1,12,30,0)
fecha_str=fecha_dt.strftime("%Y-%m-%d %H:%M:%S")
#print(type(fecha_str))

"""
Calcular los dias  que existen entre dos fechas
"""
fecha1=datetime(2022,5,10)
fecha2=datetime(2022,3,15)
diferencia_entre_fechas=fecha1-fecha2
print(f"Diferencia entre dias {diferencia_entre_fechas.days}")
diferencia_entre_años=diferencia_entre_fechas.days // 365
diferencia_entre_meses=(diferencia_entre_fechas.days) % 365 //30




