import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap



def app():

    st.title('Heatmaps')

    filepath = "https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguelatdata.csv"
    url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguelatdata.csv'
    df1 = pd.read_csv(url)
    columns1 = df1.columns.tolist()
    selected_columns = st.multiselect("select column", columns1, default='2012')
    #selected_columns =st.selectbox('Select the year',('2010', '2011', '2012','2013','2014','2015','2016','2017','2018'))
    filepath = "https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/"+selected_columns[0]+".csv"
    s = df1[selected_columns[0]]
    m = leafmap.Map(location=[20.5937, 78.9629],zoom_start=5,tiles="stamentoner")
    m.add_heatmap(
        url,
        latitude='lat',
        longitude='long',
        value=selected_columns[0],
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(width=700, height=700)
