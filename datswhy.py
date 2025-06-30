from flask import Flask, Response, jsonify
import requests

app = Flask(__name__)

# 🔐 TU TOKEN JWT AQUÍ
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTM0Nzc1MzAsInN1YiI6IjEwMTc5In0.PaOE7f72WBxruHmWqHgBYPqWj5KiGrnqJwPTF7KHKzQ"

BASE_URL = "https://ooh-saas-back-qa.datswhy.io/api/v1"

@app.route("/sites-geojson", methods=["GET"])
def obtener_sites_geojson():
    url = f"{BASE_URL}/sites/geojson/?limit=1000&skip=0&retrieve_all=true"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        geojson = response.json()

        # Convertimos GeoJSON → tabla simplificada
        sitios = []
        for feature in geojson.get("features", []):
            sitio = feature.get("properties", {})
            sitio["lat"] = feature["geometry"]["coordinates"][1]
            sitio["lon"] = feature["geometry"]["coordinates"][0]
            sitios.append(sitio)

        return jsonify(sitios)
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(port=5000)
