import pandas as pd
import plotly.express as px
import streamlit as st
import time

# Set the title of the app
st.title('Survey Data')

# Load data
df_training = pd.read_csv('https://raw.githubusercontent.com/manmeet3591/sholayar_sdb/main/sholayar_sentinel_landsat.csv')

# Create Plotly figure
fig = px.scatter_mapbox(df_training, lat="lat", lon="lon", color="bathy",
                        color_continuous_scale=px.colors.sequential.PuBu, size_max=5, zoom=11,
                        mapbox_style="carto-positron")

# Display the figure
st.plotly_chart(fig)

# Button to generate the dataset
if st.button('Generate Supervised Learning Dataset'):
    # Display loading message
    st.write('Sentinel 2A, Landsat 8 data being loaded')

    # Simulating data loading
    time.sleep(2)  # Waits for 1 minute
    st.success('Data loading complete.')
