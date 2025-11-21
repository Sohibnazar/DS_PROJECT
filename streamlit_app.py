import streamlit as st
import pandas as pd
st.title('😂😂😂MY FIRST PROJECT')

st.write('Lets do it!')
with st.expander("Data"):
  st.write('**OUR DATA**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df


with st.expander("Visualisation"):
  st.scatter_chart(data=df, x='bill_length_mm',y='bill_depth_mm', color='species')

with st.sidebar:
  st.header('Input features')
  island = st.selectbox('**Island**', {'Torgesen', 'Dream', 'Biscoe'})
  bill_length_mm = st.slider('bill_length_mm', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('bill_depth_mm', 32.1, 59.6, 43.9)
  flipper_length_mm = st.slider('flipper_length_mm', 32.1, 59.6, 43.9)
  body_mass_g = st.slider('body_mass_g', 32.1, 59.6, 43.9) 
  sex = st.selectbox('**Gender**', {'Male', 'Femail' })
