import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

def app():
  url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguef.csv'
  df1 = pd.read_csv(url)

  # Define bar properties
  columns1 = df1.columns.tolist()
  selected_columns = st.multiselect("select column", columns1, default='2012')
  s = df1[selected_columns[0]]

  bins = [0, 25, 40, 80, 200]
  labels=["Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
  "Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat",
  "Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
  "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan",
  "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
  #url = 'https://raw.githubusercontent.com/Bhaskar02/dengueapp/main/data/denguef.csv'

  #df = pd.read_csv(url)
  fig = px.bar(df1, x='States/UTs', y=s.values, color='States/UTs')#, barmode="group")#, facet_col='States/UTs')
  fig.update_layout(
      autosize=False,
      width=800,
      height=700,
      margin=dict(
          l=50,
          r=50,
          b=100,
          t=100,
          pad=4
      ),
      #legend=dict(x=0.029, y=1.038, font_size=10),
      paper_bgcolor="LightSteelBlue",
      )
  st.plotly_chart(fig)
