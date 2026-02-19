from api.consulta import obtener_datos
from ui.interfaz import pedir_datos, mostrar_tabla

def inicio():
    departamento, limite = pedir_datos()
    datos = obtener_datos(departamento, limite)
    mostrar_tabla(datos)

if __name__ == "__main__":
    inicio()
