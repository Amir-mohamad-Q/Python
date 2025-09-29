import requests
import streamlit as st
import currencies
from Currency_Converter import convert_currency


st.title(':dollar: Currency Converter')
st.markdown("""
This Currency Converter app provides a straightforward and user-friendly interface for 
converting between different currencies. It leverages real-time exchange rates to ensure
accurate conversions. The design is clean and intuitive, making it easy for users to select 
currencies and input amounts. Overall, it's a practical tool for anyone needing quick currency
conversions.""")

list_of_currencies = list(currencies.MONEY_FORMATS)

amount = st.number_input("Amount", value=100, min_value=0)
base_currency = st.selectbox("From Currency", list_of_currencies, index=110)
target_currency = st.selectbox("To Currency", list_of_currencies, index=26)

if amount > 0 and base_currency and target_currency:
    result = convert_currency(amount, base_currency, target_currency)
    st.text(result)