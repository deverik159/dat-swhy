from fastapi import FastAPI, HTTPException
from typing import List, Optional
import requests, os, time
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

# App FastAPI
app = FastAPI(
    title="API Dat's Why",
    description="Consulta sitios, geojson y análisis de SEL desde SmartAudience",
    version="1.0.0"
)

# Config
TOKEN = os.getenv("DATSWHY_TOKEN")
BASE_URL = "https://ooh-saas-back-qa.datswhy.io/api/v1"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json"
}

# 🔹 Endpoint 1: Todos los sitios (con paginación automática)
@app.get("/sites", summary="Todos los sitios", tags=["Sitios"])
def obtener_todos_los_sites(limit: int = 1000):
    all_sites = []
    skip = 0

    while True:
        url = f"{BASE_URL}/sites/?skip={skip}&limit={limit}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        if not data:
            break

        all_sites.extend(data)
        skip += limit

        # Opcional: proteger contra sobrecarga
        time.sleep(0.2)

    return all_sites

# 🔹 Endpoint 2: GeoJSON simplificado (lat, lon)
@app.get("/sites-geojson", summary="Sitios GeoJSON", tags=["Sitios"])
def obtener_sites_geojson():
    url = f"{BASE_URL}/sites/geojson/?limit=1000&skip=0&retrieve_all=true"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        geojson = response.json()
        sitios = []

        for feature in geojson.get("features", []):
            sitio = feature.get("properties", {})
            sitio["lat"] = feature["geometry"]["coordinates"][1]
            sitio["lon"] = feature["geometry"]["coordinates"][0]
            sitios.append(sitio)

        return sitios
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

# 🔹 Endpoint 3: Análisis SEL por sitio (individual)
@app.get("/sel-data/{site_id}", summary="Datos de análisis SEL", tags=["Sitios"])
def obtener_sel_data(site_id: int):
    url = f"{BASE_URL}/utils/get-sel-data/?site={site_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)
