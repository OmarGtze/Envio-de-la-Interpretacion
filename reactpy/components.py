from reactpy import component, html, use_state
import asyncio
import httpx

@component
def Cuestionario():
    cuestionario, set_cuestionario = use_state("")
    respuestas, set_respuestas = use_state("")
    resultado, set_resultado = use_state(None)

    async def enviar_cuestionario(event):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://127.0.0.1:8000/interpretacion/",
                json={"cuestionario": cuestionario, "respuestas": respuestas.split(",")}
            )
            if response.status_code == 200:
                set_resultado(response.json()["resultado"])
            else:
                set_resultado("Error al generar interpretación")

    return html.div(
        html.h1("Cuestionario"),
        html.label("Nombre del Cuestionario: "),
        html.input({"type": "text", "value": cuestionario, "on_input": lambda e: set_cuestionario(e["target"]["value"])}),
        html.br(),
        html.label("Respuestas (separadas por comas): "),
        html.input({"type": "text", "value": respuestas, "on_input": lambda e: set_respuestas(e["target"]["value"])}),
        html.br(),
        html.button({"on_click": enviar_cuestionario}, "Enviar"),
        html.div(f"Resultado: {resultado}" if resultado else "Esperando resultado...")
    )
