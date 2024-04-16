import pandas as pd
from typing import Dict

df_steam_games = pd.read_parquet(r'C:\Users\loren\Desktop\HENRY\pi\STEAM_MLOPS\Datasets\pdf_SteamGames.parquet')

def developer(desarrollador: str, df_steam_games: pd.DataFrame):
    # Filtrar por desarrollador
    df_dev = df_steam_games[df_steam_games['developer'] == desarrollador]
    
    # Obtener la cantidad de ítems por año
    items_por_anio = df_dev.groupby('release_date').size()
    
    # Obtener el porcentaje de contenido Free por año
    contenido_free_por_anio = df_dev[df_dev['price'] == 0].groupby('release_date').size()
    porcentaje_free_por_anio = (contenido_free_por_anio / items_por_anio * 100).round(2)
    
    # Reemplazar valores NaN en "Contenido Free" con "0%"
    porcentaje_free_por_anio.fillna(0, inplace=True)
    
    # Crear un DataFrame con los resultados
    result_df = pd.DataFrame({'Año': items_por_anio.index,
                              'Cantidad de Items': items_por_anio.values,
                              'Contenido Free': porcentaje_free_por_anio.values})
    
    # Ordenar el DataFrame por año
    result_df = result_df.sort_values(by='Año').reset_index(drop=True)
    
    # Formatear los valores en la columna "Contenido Free"
    result_df['Contenido Free'] = result_df['Contenido Free'].astype(str) + '%'
    
    return result_df


# Definir la ruta al archivo parquet
PARQUET_FILE_PATH = r'C:\Users\loren\Desktop\HENRY\pi\STEAM_MLOPS\Datasets\df_segunda_consulta.parquet'

def userdata(User_id: str) -> Dict[str, str]:
    # Cargar el DataFrame desde el archivo parquet
    df_segunda_consulta = pd.read_parquet(PARQUET_FILE_PATH)
    
    # Filtrar el DataFrame para obtener las filas correspondientes al User_id dado
    user_data = df_segunda_consulta[df_segunda_consulta['user_id'] == User_id]
    
    # Calcular la cantidad total de dinero gastado por el usuario
    money_spent = user_data['price'].sum()
    
    # Calcular el porcentaje de recomendación en base a las revisiones
    recommend_percentage = (user_data['recommend'].mean()) * 100
    
    # Obtener la cantidad de items del usuario y convertir a cadena de texto
    items_count = str(user_data['items_count'].sum())
    
    # Retornar un diccionario con los resultados
    return {
        "Usuario": User_id,
        "Dinero gastado": f"{money_spent} USD",
        "% de recomendación": f"{recommend_percentage}%",
        "Cantidad de items": items_count
    }
