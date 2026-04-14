import streamlit as st
import libreria_funciones as lf

st.title("Mi primera app")

st.title("Clase 5 - funciones")

p = st.number_input("Ingrese el monto principal")
t = st.number_input("Ingrese la tasa anual")
a = st.slider("Seleccione el número de años del prestamo",min_value=1, max_value=5)
pa = st.number_input("Cantidad de pagos por año")

cuota = lf.cuota_prestamo(p,t,a,pa)
st.write(cuota)