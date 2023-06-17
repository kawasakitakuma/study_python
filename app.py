import streamlit as st
import pandas as pd
import numpy as np

number = st.slider('Pick a Num', 0, 100, 40)
st.write(f'number : {number}')