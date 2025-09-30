import streamlit as st
import pandas as pd
import numpy as np


"""
Author: amir Q
"""

col1, col2, col3 = st.columns(3)
col1.write('1sr')
col2.write('2nd')
col3.write('3rd')

with col1:
    x = st.slider('select a value',0,100,37)
    st.write(f"your value is: {x}")

    contact_type = st.selectbox(
        'what is your favorite contact type?',
        ('Email','home phone','Mobile phone')
    )
    st.write(f"your favorite is: __{contact_type}__")

    contact_type_r = st.radio(
        'what is your favorite contact type?',
        ('Email','home phone','Mobile phone')
    )
    st.write(f"your favorite is: __{contact_type_r}__")

    contact_type_m = st.multiselect(
        'what is your favorite contact type?',
        ('Email','home phone','Mobile phone')
    )
    st.write(f"your favorite is: __( {'\t-\t'.join(contact_type_m)} )__")

df = pd.DataFrame({
    'First Column':[1, 2, 3],
    'Second Column':[4, 5, 6]
})
col2.write(df)

with col3:    
    if st.checkbox('show DataFrame'):
        chart_data = pd.DataFrame(
            np.random.randn(20,3),
            columns=['A','B','C']
        )
        chart_data