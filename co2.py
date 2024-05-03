import streamlit as st
import pandas as pd
st.title("Global Carbon di Oxide Emission")
df=pd.read_csv("GlobalCO2Emissions.csv")
st.line_chart(df)