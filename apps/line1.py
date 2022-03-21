import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import leafmap.foliumap as leafmap

def app():
  st.title('BarGraph')
  url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguef.csv'
  df1 = pd.read_csv(url)
  #df = df.groupby(['States/UTs', '2012'])
  columns1 = df1.columns.tolist()
  selected_columns = st.multiselect("select column", columns1, default='2012')
  s = df1[selected_columns[0]]

  trace = go.Bar(x=df1['States/UTs'],y=s.values,showlegend = True)
  layout = go.Layout(title = "test")
  data = [trace]
  fig = go.Figure(data=data,layout=layout)
  fig.update_layout(
    autosize=False,
    width=1000,
    height=700,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    legend=dict(x=0.029, y=1.038, font_size=10),
    paper_bgcolor="LightSteelBlue",
)
  st.plotly_chart(fig)
