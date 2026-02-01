# app.py - IN SPACE FURNITURE - BASIC VERSION
import streamlit as st

st.set_page_config(page_title="IN SPACE", layout="wide")
st.title("🪑 IN SPACE FURNITURE")
st.subheader("AR + AI Furniture Platform")

# Navigation
page = st.sidebar.selectbox("Menu", ["Home", "Demo", "Investor", "Contact"])

if page == "Home":
    st.write("### Complete Furniture Ecosystem")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**AR Room Scan**")
    with col2:
        st.info("**AI Design**")
    with col3:
        st.info("**Circular Service**")
    
    st.success("✅ App deployed successfully!")
    
elif page == "Demo":
    st.write("### Feature Preview")
    
    # Room scan demo
    if st.button("📏 Scan Room"):
        st.success("Room: 15×12 ft | Humidity: 78%")
        st.write("**Recommended:** Teak Wood")
    
    # AI design demo
    idea = st.text_input("Your design idea", "Lion + peacock sofa")
    if st.button("✨ AI Refine"):
        st.success(f"AI Enhanced: 'Regal fusion design'")
    
elif page == "Investor":
    st.write("### Investor Dashboard")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Market", "$800B")
    with col2:
        st.metric("Ask", "$1.5M")
    with col2:
        st.metric("Valuation", "$8M")

elif page == "Contact":
    st.write("### Get in Touch")
    st.write("**Email:** hello@inspace.furniture")
    st.write("**Demo:** [Streamlit App]")
