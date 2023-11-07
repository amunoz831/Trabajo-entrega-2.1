import datetime

def calcular_duracion_alquiler(fecha_inicio, fecha_fin):
    diferencia_fecha = fecha_fin - fecha_inicio
    segundos = diferencia_fecha.total_seconds()
    minutos = segundos // 60
    return minutos


fecha_inicio = datetime.datetime(2023, 11, 7, 12, 0, 0)
fecha_fin = datetime.datetime(2023, 11, 7, 12, 30, 0)

duracion = calcular_duracion_alquiler(fecha_inicio, fecha_fin)

print(duracion)