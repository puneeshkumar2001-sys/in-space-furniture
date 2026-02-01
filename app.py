# app.py - IN SPACE FURNITURE - COMPLETE APP
import streamlit as st
import pandas as pd
import numpy as np

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="IN SPACE FURNITURE",
    page_icon="🪑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2A5C3D;
        font-weight: 900;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        border: 3px solid #2A5C3D;
        text-align: center;
        box-shadow: 0 5px 15px rgba(42, 92, 61, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("# 🪑 IN SPACE")
    st.markdown("**AR + AI Furniture Ecosystem**")
    st.markdown("---")
    
    page = st.radio(
        "## 🧭 NAVIGATION",
        [
            "🏠 HOME - Vision",
            "📱 1. AR ROOM SCAN", 
            "🌳 2. SMART MATERIALS",
            "🎨 3. AI DESIGN STUDIO",
            "👗 4. VIRTUAL TRY-ON",
            "💰 5. QUOTE & ORDER",
            "♻️ 6. CIRCULAR SERVICE",
            "📊 7. INVESTOR DASHBOARD"
        ]
    )
    
    st.markdown("---")
    st.success("🚀 Live on Streamlit Cloud")
    st.caption("Complete Ecosystem Demo")

# ========== PAGE ROUTING ==========
if page == "🏠 HOME - Vision":
    st.markdown('<div class="main-header">IN SPACE FURNITURE</div>', unsafe_allow_html=True)
    st.subheader("From Room Scan to Circular Design — Furniture That Fits Your Space, Style, and Planet")
    
    # Hero Section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📱 AR Scanning")
        st.write("Millimeter-accurate room measurement with climate analysis")
        st.image("https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=400", use_container_width=True)
    
    with col2:
        st.markdown("### 🎨 AI Design")
        st.write("Professional design refinement from your ideas")
        st.image("https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400", use_container_width=True)
    
    with col3:
        st.markdown("### ♻️ Circular Service")
        st.write("Repair, upcycle, recycle ecosystem")
        st.image("https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=400", use_container_width=True)
    
    # Metrics
    st.markdown("---")
    st.markdown("### 📊 By The Numbers")
    
    metrics = pd.DataFrame({
        "Metric": ["Market Size", "Returns Reduced", "Lifespan Increased", "Waste Diverted"],
        "Value": ["$800B", "47%", "3.2x", "85%"],
        "Description": ["Global furniture market", "Via virtual try-on", "Climate-matched materials", "Circular service"]
    })
    
    st.dataframe(metrics, use_container_width=True, hide_index=True)

elif page == "📱 1. AR ROOM SCAN":
    st.title("Step 1: AR Room Scanning")
    st.write("Mock AR room scanning interface")
    
    # Room scan simulation
    if st.button("📏 Scan Room with AR", type="primary"):
        st.success("✅ Room scanned: 15×12 ft, 78% humidity, 32°C")
        
        scan_data = pd.DataFrame({
            "Parameter": ["Width", "Length", "Humidity", "Temperature", "Sunlight"],
            "Value": ["15.2 ft", "12.8 ft", "78%", "32°C", "6.5 hrs/day"],
            "Status": ["✅", "✅", "⚠️ High", "✅", "✅"]
        })
        
        st.dataframe(scan_data, use_container_width=True, hide_index=True)

elif page == "🌳 2. SMART MATERIALS":
    st.title("Step 2: Climate-Aware Material Selection")
    
    # Material recommendations
    materials = pd.DataFrame({
        "Wood": ["Teak", "Mango", "Teak/Mango Blend", "Walnut/Oak"],
        "Humidity Resistance": ["95%", "70%", "85%", "80%"],
        "Best For": ["Coastal/Humid", "Moderate/Dry", "All-rounder", "Luxury/Dry"],
        "Sustainability": ["High", "Very High", "High", "Medium"],
        "Price/ft³": ["$85", "$45", "$65", "$120"]
    })
    
    st.dataframe(materials, use_container_width=True, hide_index=True)
    
    st.info("🌡️ **AI Recommendation:** For 78% humidity → **Teak Wood** (98% resistance)")

elif page == "🎨 3. AI DESIGN STUDIO":
    st.title("Step 3: AI Design Studio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Before AI:**")
        st.write("• Lion + Peacock design")
        st.write("• Mismatched scales")
        st.write("• Color clashes")
    
    with col2:
        st.write("**After AI Refinement:**")
        st.write("• Regal fusion design")
        st.write("• Balanced proportions")
        st.write("• Harmonious color palette")
    
    st.success("🎯 **Design Cohesion Score: 92/100**")

elif page == "👗 4. VIRTUAL TRY-ON":
    st.title("Step 4: Virtual Try-On")
    
    # Fit analysis
    fit_data = pd.DataFrame({
        "Parameter": ["Room Size", "Furniture Fit", "Walking Space", "Climate Match"],
        "Score": ["15×12 ft", "95%", "5.8 ft", "92%"],
        "Status": ["✅ Adequate", "✅ Excellent", "✅ Optimal", "✅ High"]
    })
    
    st.dataframe(fit_data, use_container_width=True, hide_index=True)
    
    st.info("📱 **AR Experience:** Point camera, see furniture in your room at exact scale")

elif page == "💰 5. QUOTE & ORDER":
    st.title("Step 5: Quote & Order")
    
    # Pricing breakdown
    pricing = pd.DataFrame({
        "Component": ["Custom Sofa", "Teak Material", "AI Design", "Circular Service", "Total"],
        "Cost": ["$800", "$400", "$150", "$50", "$1,400"],
        "Description": ["3-seater, custom design", "Premium teak wood", "AI refinement", "5-year warranty", "All inclusive"]
    })
    
    st.dataframe(pricing, use_container_width=True, hide_index=True)
    
    if st.button("🛒 Place Order", type="primary"):
        st.success("🎉 Order placed! Delivery: 3-4 weeks")

elif page == "♻️ 6. CIRCULAR SERVICE":
    st.title("Step 6: Circular Service Program")
    
    services = pd.DataFrame({
        "Service": ["Repair", "Upcycle", "Recycle", "Take-Back"],
        "Cost": ["$99-299", "$199-499", "FREE", "30-60% value"],
        "Time": ["1-2 weeks", "2-3 weeks", "1 week", "Instant"],
        "Impact": ["Extends life 5+ years", "New furniture", "Zero waste", "Store credit"]
    })
    
    st.dataframe(services, use_container_width=True, hide_index=True)

elif page == "📊 7. INVESTOR DASHBOARD":
    st.title("IN SPACE FURNITURE - Investor Dashboard")
    
    # Key metrics
    st.markdown("## 📈 Market Opportunity")
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    with metrics_col1:
        st.metric("Market Size", "$800B")
    with metrics_col2:
        st.metric("Target Segment", "$120B")
    with metrics_col3:
        st.metric("Seed Ask", "$1.5M")
    with metrics_col4:
        st.metric("Valuation", "$8M")
    
    # Financial projections
    st.markdown("## 💰 Financial Projections")
    
    financials = pd.DataFrame({
        "Year": [1, 2, 3],
        "Revenue": ["$600K", "$3.2M", "$10.5M"],
        "Customers": ["1,000", "10,000", "50,000"],
        "Margin": ["40%", "45%", "50%"]
    })
    
    st.dataframe(financials, use_container_width=True, hide_index=True)

# ========== FOOTER ==========
st.markdown("---")
st.caption("🪑 IN SPACE FURNITURE © 2024 | Complete Ecosystem Demo | Live on Streamlit Cloud")
