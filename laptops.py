import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recomendador de Laptops 🎓", page_icon="💻", layout="wide")

# Conversión rápida PEN a USD
USD_TO_PEN = 3.8

# ===========================
# DATASET DE LAPTOPS
# ===========================
data = [
    {
        "marca": "Acer",
        "modelo": "Aspire 5 A515",
        "precio": 550,
        "pantalla": "No táctil",
        "os": "Windows",
        "cpu": "Intel i5",
        "ram_gb": 8,
        "almacenamiento": "512GB SSD",
        "gpu": "Integrada",
        "peso_kg": 1.7,
        "bateria_h": 8,
        "perfiles": ["Ofimática/Clases", "Negocios"],
        "carreras": ["General", "Negocios", "Comunicación/Multimedia"],
        "descripcion": "Portátil confiable para estudiantes y trabajo ligero. Excelente batería y precio accesible.",
        "link": "https://www.acer.com/pe-es/laptops/aspire/aspire-5"
    },
    {
        "marca": "Apple",
        "modelo": "MacBook Air M1",
        "precio": 999,
        "pantalla": "No táctil",
        "os": "macOS",
        "cpu": "Apple M1",
        "ram_gb": 8,
        "almacenamiento": "256GB SSD",
        "gpu": "Integrada",
        "peso_kg": 1.29,
        "bateria_h": 15,
        "perfiles": ["Programación", "Diseño/Edición", "Ofimática/Clases"],
        "carreras": ["Ingeniería/CS", "Diseño/Arquitectura", "Comunicación/Multimedia"],
        "descripcion": "Ultraligera con excelente autonomía. Ideal para diseño básico y desarrollo.",
        "link": "https://www.apple.com/la/macbook-air-m1/"
    },
    {
        "marca": "ASUS",
        "modelo": "TUF Gaming A15",
        "precio": 1200,
        "pantalla": "No táctil",
        "os": "Windows",
        "cpu": "Ryzen 7",
        "ram_gb": 16,
        "almacenamiento": "1TB SSD",
        "gpu": "RTX 3050",
        "peso_kg": 2.3,
        "bateria_h": 6,
        "perfiles": ["Gaming", "Diseño/Edición"],
        "carreras": ["Diseño/Arquitectura", "Comunicación/Multimedia"],
        "descripcion": "Potencia gráfica para juegos y diseño avanzado. Pantalla de alto rendimiento.",
        "link": "https://www.asus.com/laptops/for-gaming/tuf-gaming/asus-tuf-gaming-a15/"
    },
    {
        "marca": "HP",
        "modelo": "Pavilion 15",
        "precio": 700,
        "pantalla": "No táctil",
        "os": "Windows",
        "cpu": "Intel i5",
        "ram_gb": 8,
        "almacenamiento": "512GB SSD",
        "gpu": "Integrada",
        "peso_kg": 1.75,
        "bateria_h": 9,
        "perfiles": ["Ofimática/Clases", "Programación"],
        "carreras": ["General", "Ingeniería/CS", "Negocios"],
        "descripcion": "Balanceada en precio y rendimiento, ideal para estudiantes universitarios.",
        "link": "https://www.hp.com/pe-es/shop/laptops"
    },
    {
        "marca": "Lenovo",
        "modelo": "ThinkPad X1 Carbon",
        "precio": 1400,
        "pantalla": "No táctil",
        "os": "Windows",
        "cpu": "Intel i7",
        "ram_gb": 16,
        "almacenamiento": "512GB SSD",
        "gpu": "Integrada",
        "peso_kg": 1.13,
        "bateria_h": 15,
        "perfiles": ["Negocios", "Ofimática/Clases"],
        "carreras": ["Negocios", "General"],
        "descripcion": "Laptop empresarial premium, muy ligera y con excelente batería.",
        "link": "https://www.lenovo.com/pe/es/laptops/thinkpad/thinkpad-x1/ThinkPad-X1-Carbon-Gen-11/p/WMD00000463"
    },
    {
        "marca": "MSI",
        "modelo": "Katana GF66",
        "precio": 1300,
        "pantalla": "No táctil",
        "os": "Windows",
        "cpu": "Intel i7",
        "ram_gb": 16,
        "almacenamiento": "1TB SSD",
        "gpu": "RTX 3060",
        "peso_kg": 2.25,
        "bateria_h": 7,
        "perfiles": ["Gaming", "Diseño/Edición"],
        "carreras": ["Diseño/Arquitectura", "Comunicación/Multimedia"],
        "descripcion": "Perfecta para gaming competitivo y edición de video profesional.",
        "link": "https://www.msi.com/Laptop/Katana-GF66-12UX"
    }
]

df = pd.DataFrame(data)

# ===========================
# PREGUNTAS INICIALES
# ===========================
st.title("💻 Encuentra tu Laptop Ideal")
st.write("🎯 Responde estas preguntas para obtener una recomendación personalizada:")

uso = st.selectbox(
    "📌 ¿Para qué usarás principalmente tu laptop?",
    ["Ofimática/Clases", "Programación", "Diseño/Edición", "Datos/Análisis", "Gaming"]
)

carrera = st.selectbox(
    "🎓 ¿En qué área te desarrollas o estudias?",
    ["General", "Ingeniería/CS", "Diseño/Arquitectura", "Negocios", "Comunicación/Multimedia"]
)

presupuesto_soles = st.slider("💰 ¿Cuál es tu presupuesto en Soles?", 1000, 10000, 4000, step=500)
presupuesto = presupuesto_soles / USD_TO_PEN

pantalla_pref = st.radio("🖥️ ¿Prefieres pantalla táctil?", ["Indiferente", "Táctil", "No táctil"])

portabilidad = st.radio(
    "⚖️ ¿Qué tan importante es para ti que sea liviana?",
    ["No es importante", "Me gustaría ligera (≤ 1.4 kg)"]
)
priorizar_portabilidad = portabilidad == "Me gustaría ligera (≤ 1.4 kg)"

so_pref = st.radio("💻 ¿Prefieres algún sistema operativo?", ["Indiferente", "Windows", "macOS"])

# ===========================
# FILTRADO
# ===========================
filtered = df[df["precio"] <= presupuesto]
if pantalla_pref != "Indiferente":
    filtered = filtered[filtered["pantalla"] == pantalla_pref]
if so_pref != "Indiferente":
    filtered = filtered[filtered["os"] == so_pref]
if priorizar_portabilidad:
    filtered = filtered[filtered["peso_kg"] <= 1.4]

# ===========================
# RESULTADOS
# ===========================
st.header("🔍 Laptops Recomendadas")
if filtered.empty:
    st.warning("❌ No encontramos laptops según tus respuestas. Ajusta tu presupuesto o preferencias.")
else:
    for _, row in filtered.iterrows():
        score = 1.0
        if uso in row["perfiles"]:
            score += 0.5
        if carrera in row["carreras"]:
            score += 0.5

        with st.container():
            st.markdown(f"### [{row['marca']} {row['modelo']}]({row['link']})")
            st.markdown(f"💵 **Precio:** ${row['precio']} (~S/ {int(row['precio']*USD_TO_PEN)})")
            st.markdown(f"🖥️ **Pantalla:** {row['pantalla']} | ⚙️ **CPU:** {row['cpu']} | 🧠 **RAM:** {row['ram_gb']}GB | 💾 **Almacenamiento:** {row['almacenamiento']}")
            st.markdown(f"🎮 **GPU:** {row['gpu']} | 🔋 **Batería:** {row['bateria_h']}h | ⚖️ **Peso:** {row['peso_kg']}kg")
            st.info(f"📌 {row['descripcion']}")
            st.progress(min(score/2, 1.0))
            st.divider()

st.caption("💡 App educativa. Precios aproximados y enlaces oficiales.")
