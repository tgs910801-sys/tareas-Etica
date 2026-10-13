
import streamlit as st
import re
import random

# TAREA 1: Diseño de Intenciones y Patrones
INTENCIONES = {
    "saludo": {
        "patrones": [r"\bhola\b", r"\bbuenos dias\b", r"\bbuenas tardes\b", r"\bhey\b"],
        "respuestas": ["¡Hola! ¿En qué puedo ayudarte hoy?", "¡Hola! Bienvenido al servicio al cliente."]
    },
    "horario": {
        "patrones": [r"\bhorario\b", r"\bque hora abren\b", r"\bhoras\b", r"\bcuando atienden\b"],
        "respuestas": ["Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00 hrs."]
    },
    "envios": {
        "patrones": [r"\benvio", r"\bdespacho", r"\bentrega", r"\btarda"],
        "respuestas": ["Realizamos envíos a todo el país. El tiempo estimado de entrega es de 3 a 5 días hábiles."]
    },
    "contacto": {
        "patrones": [r"\bcontacto\b", r"\btelefono\b", r"\bhumano\b", r"\basesor\b"],
        "respuestas": ["Puedes comunicarte con nosotros al correo soporte@empresa.com o llamando al 555-1234."]
    }
}

# TAREA 2: Procesamiento de Consultas (NLP & Fallback)
def procesar_consulta(mensaje):
    mensaje_limpio = mensaje.lower().strip()
    for intencion, datos in INTENCIONES.items():
        for patron in datos["patrones"]:
            if re.search(patron, mensaje_limpio):
                return random.choice(datos["respuestas"])
    return "Lo siento, no he logrado entender tu consulta. ¿Podrías reformularla o escribir 'contacto' para hablar con un asesor humano?"

# TAREA 3: Interfaz de Usuario (Web, Historial y Evaluación)
st.set_page_config(page_title="Chatbot de Atención al Cliente", page_icon="🤖")

st.title("🤖 Asistente Virtual - Atención al Cliente")
st.write("Escribe tus dudas sobre horarios, envíos o formas de contacto.")

if "historial" not in st.session_state:
    st.session_state.historial = []

for remitente, texto in st.session_state.historial:
    with st.chat_message(remitente):
        st.markdown(texto)

user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    st.session_state.historial.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)
        
    respuesta_bot = procesar_consulta(user_input)
    st.session_state.historial.append(("assistant", respuesta_bot))
    with st.chat_message("assistant"):
        st.markdown(respuesta_bot)

st.sidebar.header("📊 Evaluación de Satisfacción")
satisfaccion = st.sidebar.radio("¿Cómo calificarías la atención recibida?", ["😊 Excelente", "😐 Regular", "😞 Malo"])

if st.sidebar.button("Enviar calificación"):
    st.sidebar.success("¡Muchas gracias por ayudarnos a mejorar!")