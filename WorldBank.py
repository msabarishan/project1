import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

India=pd.read_csv('World_Bank_India1.csv',skiprows=4,index_col='Indicator Name',usecols=["Indicator Name","2010","2011","2012","2013","2014","2015","2016","2017","2018"])
IndiaT=India.T
indianew=IndiaT[['Physicians (per 1,000 people)','Number of deaths ages 5-9 years','People using safely managed sanitation services, rural (% of rural population)']]
indianew1=indianew.reindex()
df = indianew1.rename_axis(None, axis=1)
st.dataframe(df)
st.set_page_config(page_title="World Bank Data for India",layout="wide",initial_sidebar_state="expanded")
st.title("World Bank Data for India")

