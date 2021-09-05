import streamlit as st
import pandas as pd
import geopandas as gpd 
import matplotlib.pyplot as plt 

# Text
st.title("Geo Application")
st.header("Learning Streamlit")
st.text("This is a text")

# Image
st.image("images/geocoding.jpg")

# DataFrames 

df = pd.DataFrame({
    "city": ["shanghai", "sao paulo", "kinshasa", "london"],
    "population": [14608512, 10021437, 7787832, 7421228],
    "latitude": [31.045556, -23.473293, -4.3, 51.514125],
    "longitude": [121.399722, -46.665803, 15.3, -0.093689],
}
)
#st.write(df)
df

# Charts

#st.bar_chart(df)
#st.line_chart(df)

#fig, ax = plt.subplots()
#plt.bar(df.city, df.population)
#st.pyplot(fig)

#st.map(df)

# Interactivity 

#if st.checkbox("Show me"):
    #st.map(df)

options = st.selectbox(
    "Which City?",
    df["city"]
)


# Layout 

st.sidebar.title("Sidebar title")

if st.sidebar.checkbox("Show me"):
    st.map(df)