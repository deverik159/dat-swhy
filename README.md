# 📊 Dat's Why API - FastAPI + Render + Power BI

Este proyecto expone una API personalizada que conecta con los endpoints oficiales de **Dat's Why** y los simplifica para consumir desde **Power BI, Postman o cualquier cliente HTTP**.

---

## 🚀 Base URL de producción (Render)

📌 **URL para Power BI:**
https://dat-swhy.onrender.com/


---

## 🔐 Seguridad

Esta API ya usa un token JWT interno (desde variable de entorno), por lo tanto **no necesitas autenticación adicional** al consumirla desde Power BI.

---

## 📚 Endpoints disponibles

### 🔹 1. Todos los sitios (JSON)

📌 **URL para Power BI:**
https://dat-swhy.onrender.com/sites



✅ Devuelve todos los sitios, paginando automáticamente.

---

### 🔹 2. Sitios GeoJSON simplificado (con lat/lon)


📌 **URL para Power BI:**
https://dat-swhy.onrender.com/sites-geojson



✅ Devuelve los sitios con lat/lon para mapas.

---

### 🔹 3. Buscar sitios por texto

📌 **URL para Power BI:**
https://dat-swhy.onrender.com/sites-search?q=Lumina


✅ Devuelve sitios cuyo client code o nombre contiene el texto buscado.

---

### 🔹 4. Datos de análisis SEL por sitio

https://dat-swhy.onrender.com/sel-data/207513


✅ Devuelve los datos analíticos (SEL) del sitio.

---

### 🔹 5. Desempeño histórico de un sitio



✅ Devuelve datos de rendimiento del sitio.

---

### 🔹 6. Atributos del sitio



✅ Devuelve KPIs y estadísticas generales de campaña.

---

## 📊 ¿Cómo conectarlo a Power BI?

1. Ir a **Inicio > Obtener datos > Web**
2. Pegar la URL del endpoint (por ejemplo: `https://dat-swhy.onrender.com/sites`)
3. Elegir **anónimo**
4. Expandir campos en el editor Power Query

---

## 🧠 Recomendaciones

- Usa `/sites-search` para filtrar antes de cargar todo el dataset.
- Limita las llamadas a `/sel-data/{id}` o `/performance` cuando sea necesario.
- Puedes crear un dashboard de selección que combine campaña + sitios.

---

## 🛠️ Tecnologías

- FastAPI
- Render
- requests
- dotenv
- Power BI (consumo)

---

## 📬 Contacto

Erik Mejía – Integrador de Dat's Why con Power BI



