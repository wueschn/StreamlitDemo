import streamlit as st 

def quadrieren(z1):
    ergebnis = z1 ** 2
    return ergebnis

st.title("Quadrierer von Mario Wüschner")
st.header("Stark vereinfacht, aber praktisch!")
st.image("summe.jpg", width=200)

wert = st.number_input("Geben Sie Ihre Zahl ein!")
st.write("Ihr gewünschtes Ergebnis, das Quadrat: ",quadrieren(wert))