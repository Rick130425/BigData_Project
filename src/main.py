import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


@st.cache_data
def get_pandas_dataset():
    data_frame = pd.read_csv('../data/Tarifas por zonas 2016-2017.csv')
    return data_frame


"""
# Análisis de las tarifas de transporte de gas natural 
"""
