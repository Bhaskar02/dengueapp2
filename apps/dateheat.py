
import datetime
from glob import glob
import numpy as np
import folium
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd
import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title('heatmap with Date')

    
    
    df = pd.read_csv('https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/dengue11f.csv')
    df['dat'] = pd.to_datetime(df['dat'], format='%Y-%m-%d')
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    #m = folium.Map([20.5937, 78.9629], tiles='stamentoner', zoom_start=5)
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    today=today - datetime.timedelta(days=200)
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', tomorrow)
    data=df[(df.dat>=str(start_date)) & (df.dat<=str(end_date))]
    st.write('', data)
    data=data[['lat','lon','cases']]
    HeatMap(data).add_to(m)#(folium.FeatureGroup(name='Heat Map').add_to(m))
    #st.write('', data)
    #folium.LayerControl().add_to(m)
    m.to_streamlit(width=700, height=700)
