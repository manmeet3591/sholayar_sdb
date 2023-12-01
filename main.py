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
                        color_continuous_scale=px.colors.sequential.PuBu, size_max=5, zoom=10,
                        mapbox_style="carto-positron", range_color=[0, 50])

# Display the figure
st.plotly_chart(fig)

# Button to generate the dataset
if st.button('Generate Supervised Learning Dataset'):
    # Display loading message
    st.write('Sentinel 2A, Landsat 8 data being loaded')

    # Simulating data loading
    time.sleep(2)  # Waits for 1 minute
    st.success('Data loading complete. Supervised learning dataset ready for Satellite Derived Bathymetry using machine learning')

# Button to train machine learning model
if st.button('Train Machine Learning Model'):
    # Display training message
    st.write('Training machine learning model with satellite inputs and bathymetry survey targets...')
    st.write('Full hyperparameter optimization using XGBoost in progress...')

    # Simulate model training
    # In a real app, replace this with actual model training code
    time.sleep(1)  # Simulating time taken for model training
    st.success('Model training complete.')

# Button to display predicted bathymetry lines
if st.button('Display Predicted Bathymetry Lines'):
    # Load predicted dataset
    df_predicted = pd.read_csv('https://raw.githubusercontent.com/manmeet3591/sholayar_sdb/main/sholayar_full_bathy_predicted.csv')

    # Create Plotly figure for predicted data
    fig_predicted = px.scatter_mapbox(df_predicted, lat="y", lon="x", color="y_test_pred",
                                      color_continuous_scale=px.colors.sequential.PuBu, size_max=5, zoom=10,
                                      mapbox_style="carto-positron", range_color=[0, 50])

    # Display the predicted figure
    st.plotly_chart(fig_predicted)
