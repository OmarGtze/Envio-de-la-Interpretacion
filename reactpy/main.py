from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from components import Cuestionario  # Importar el componente de ReactPy

# Inicializar la aplicación
app = FastAPI()

# Configurar ReactPy con FastAPI
configure(app, Cuestionario)

@app.post("/interpretacion/")
async def generar_interpretacion(data: Cuestionario):
    resultado = f"Interpretación basada en el cuestionario '{data.cuestionario}' y respuestas {data.respuestas}"
    return {"mensaje": "Interpretación generada", "resultado": resultado}

