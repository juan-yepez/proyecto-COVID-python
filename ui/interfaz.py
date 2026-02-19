import pandas as pd

def pedir_datos():
    depto = input("Ingrese el nombre del Departamento (ej: ANTIOQUIA): ")
    try:
        limite = int(input("Ingrese el número de registros: "))
    except ValueError:
        limite = 10
    return depto, limite

def mostrar_tabla(df):
    if df is None or df.empty:
        print("\nNo se encontraron resultados.")
        return

    
    if 'pais_viajo_1_nom' not in df.columns:
        df['pais_viajo_1_nom'] = "COLOMBIA"
    
    
    col_api = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']
    
  
    df_final = df[col_api].copy()
    
    
    df_final.columns = ['CIUDAD', 'DEPARTAMENTO', 'EDAD', 'TIPO', 'ESTADO', 'PAIS']
    
    
    df_final = df_final.fillna("---")

  
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'left')

    print("\n" + "="*95)
   
    print(df_final.to_string(index=False, justify='left'))
    print("="*95)
    print(f"Registros encontrados: {len(df_final)}\n")
