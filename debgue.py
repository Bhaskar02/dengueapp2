import streamlit as st
from multiapp import MultiApp
from apps import (
    
    
    #line1,
    line,
    heatmapf,
    dateheat
    #ras
    
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here



#apps.add_app("Bargraph", line1.app)
apps.add_app("BarGraph", line.app)
apps.add_app("HeatMap1", heatmapf.app)
apps.add_app("HeatMap2", dateheat.app)
#apps.add_app("ras", ras.app)

#link = '[Home](https://share.streamlit.io/bhaskar02/display_trend/main/app2.py)'
#st.markdown(link, unsafe_allow_html=True)
# The main app
apps.run()
