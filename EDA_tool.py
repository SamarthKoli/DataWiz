import pandas as pd
import streamlit as st
import numpy as np
from ydata_profiling import ProfileReport 
import streamlit.components.v1 as components  
import time

# Header Section
st.header("Welcome to DataWiz")
st.markdown('<h3>Created by: Samarth Koli</h3>', unsafe_allow_html=True)

# Information about the tool
st.markdown("""
<p>Exploratory Data Analysis (EDA) is a critical step in the data analysis process. It involves analyzing datasets to summarize their main characteristics, often using visual methods. 
This tool will help you analyze your dataset and uncover insights from it.</p>
""", unsafe_allow_html=True)

# Body Section
st.markdown("<h4>1. Upload your Dataset File (CSV format)</h4>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here's the preview of your uploaded dataset")
    st.write(df.head(20))
    
    report = ProfileReport(df, explorative=True)
    loading_bar=st.progress(0)
   
    for percent_complete in range(0, 101, 10):
            time.sleep(0.8) 
            loading_bar.progress(percent_complete)
    
    report_html = report.to_html()
   
    components.html(report_html, width=650,height=1000, scrolling=True)
else:
    st.write("Please upload a CSV file to get started.")
