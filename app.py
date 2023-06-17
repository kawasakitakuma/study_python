import streamlit as st
import pandas as pd
import numpy as np

left_col, center_col, right_col = st.columns(3)
left_col.slider('Pick a Num in Left', 0, 100)
center_col.slider('Pick a Num in Center', 0, 100)
right_col.slider('Pick a Num in right', 0, 100)