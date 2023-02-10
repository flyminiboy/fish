"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

import os
import openai

st.title('飞🐶')

i = st.text_input(label='输入问题', max_chars=30, value='', help='把你想要通过chatGPT回答的问题输入在这里', placeholder='请输入')


# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("ENV_OPENAPI_KEY")

response = openai.Completion.create(model="text-davinci-003",
  prompt=i,
  temperature=0, 
  max_tokens=1500,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0)


st.write(response.choices[0].text)

st.write("我是分割线----------")
st.json(response)

# 图表


# 侧边栏
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?", 
#     ("Email", "Home phone", "Mobile phone")
# )