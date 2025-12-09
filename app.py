import streamlit as st
import requests

st.title("💱 FX Converter USD → THB")

usd = st.number_input("Enter USD amount:", min_value=0.0, step=0.01)

def get_rate():
    url = "https://api.frankfurter.app/latest?from=USD&to=THB"
    data = requests.get(url).json()
    return data["rates"]["THB"]

if st.button("Convert"):
    rate = get_rate()
    thb = usd * rate
    st.success(f"{usd} USD = {thb:.2f} THB (Rate: {rate})")
