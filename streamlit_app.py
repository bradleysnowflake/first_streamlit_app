import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Snowflake Web Application')
st.header('Deployed via Streamlit')

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write('Example Randomized Dataplot', c)


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.text('Smoothie Macro Calculator')
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt', index_col = 'Fruit')
# Supreme overload Snowflake requests a picklist:
st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple','Mango'])

st.write(my_fruit_list)



st.text('gg ez')
