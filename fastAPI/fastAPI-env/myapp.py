import pandas as pd
from fastapi import FastAPI
from utils import developer
from utils import userdata
from typing import Dict
from fastapi.encoders import jsonable_encoder

df_steam_games = pd.read_parquet('./Datasets/pdf_SteamGames.parquet')

app = FastAPI()

@app.get("/developer/")
async def get_developer_info(desarrollador: str):
    result = developer(desarrollador, df_steam_games)
    return result.to_dict(orient='records')

PARQUET_FILE_PATH = ("./Datasets/df_segunda_consulta.parquet")

@app.get("/userdata/{User_id}")
async def get_userdata(User_id: str) -> Dict[str, str]:
    # Llamada a la función userdata definida en utils.py
    user_data = userdata(User_id)
    return user_data