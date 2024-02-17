"""
Programa que me permita calcular el pago por dia que recibira un Obrero que trabaja por jornal diaria
"""

pago_hora=20.70
horas_trab=int(input("Ingrese las horas Trabajadas:"))
pago_a_recibir=horas_trab * pago_hora
print(f"El Pago a recibir es {round(pago_a_recibir,2)}")
#print(type(horas_trab))