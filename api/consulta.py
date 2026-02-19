import pandas as pd
from sodapy import Socrata

def obtener_datos(nombre_departamento, limite_registros):
    client = Socrata("www.datos.gov.co", None)
    # Esta es la consulta a la API
    results = client.get("gt2j-8ykr", 
                         limit=limite_registros, 
                         departamento_nom=nombre_departamento.upper())
    return pd.DataFrame.from_records(results)
