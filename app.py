import streamlit as st
import pandas as pd
import numpy as np
st.title('Sample App')
df = pd. DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c'])

st.bar_chart(df)