import streamlit as st
import pandas as pd

st.title("🪑 IN SPACE FURNITURE - Phase 1")
st.write("✅ Basic app + pandas working")

# Test pandas
data = pd.DataFrame({
    'Feature': ['AR Scan', 'AI Design', 'Circular Service'],
    'Status': ['✅', '✅', '✅']
})
st.dataframe(data)
