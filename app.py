import plotly.express as px
import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title('Correlation App')


@st.cache
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    data = pd.read_csv(url)

    return data


df = fetch_and_clean_data(
    'https://raw.githubusercontent.com/drazenz/heatmap/master/autos.clean.csv')

corr = df.corr()

fig = px.imshow(corr)
st.plotly_chart(fig, use_container_width=True)

if st.button('Show Data'):
    st.table(corr)
else:
    st.write('Click to See Data')
