"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# 图表
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

chart_data = pd.DataFrame(
     np.random.randn(50, 3), 
     columns=["a", "b", "c"])
st.bar_chart(chart_data)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),     
     columns=['a', 'b', 'c'])
st.area_chart(chart_data)

# 侧边栏
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", 
    ("Email", "Home phone", "Mobile phone")
)