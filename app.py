import streamlit as st
import requests

st.title("Chatbot de Commande de Restaurant")

user_input = st.text_input("Que souhaitez-vous commander ?")

if user_input:

    response = requests.get(f"http://localhost:8000/ask", params={"prompt": user_input})

    if response.status_code == 200:
        st.write(response.json()["response"])
    else:
        st.write("Erreur lors de la communication avec le chatbot.")