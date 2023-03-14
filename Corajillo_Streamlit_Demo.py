import pandas as pd
import streamlit as st
import plotly.express as px


#Streamlit will perform internal magic so that the data will be downloaded only once and cached for future use.
@st.cache_data
def get_data():
#    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2022-12-04/visualisations/listings.csv"
#    return pd.read_csv(url, low_memory=False)
     return pd.read_csv('DataSetCarajilloDummy.csv', low_memory=False)

df = get_data()


st.title("Hello World Corajillo")
#st.markdown("Welcome")
#st.header("Header")
#st.markdown("*bold*")

st.dataframe(df.head())

