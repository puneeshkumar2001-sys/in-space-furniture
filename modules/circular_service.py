import streamlit as st
import pandas as pd

def show_circular_service():
    """Display circular economy service portal"""
    st.subheader("♻️ Circular Service Program")
    
    st.info("""
    **Our Promise:** No furniture goes to landfill. 
    We repair, upcycle, or responsibly recycle every piece.
    """)
    
    # Service selection
    service = st.radio(
        "Choose a service:",
        ["🛠️ Repair & Restore", "🔄 Upcycle & Transform", "♻️ Responsible Recycling", "📦 Take-Back Program"]
    )
    
    if service == "🛠️ Repair & Restore":
        st.write("### Furniture Repair Service")
        st.write("Extend your furniture's life with expert repairs.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Common Repairs:**")
            repairs = {
                "Structural Repair": "$99-199",
                "Reupholstery": "$299-599",
                "Wood Refinishing": "$149-349",
                "Hardware Replacement": "$49-99",
                "Cushion Replacement": "$129-259"
            }
            
            for repair, price in repairs.items():
                st.write(f"- **{repair}:** {price}")
        
        with col2:
            st.write("**Process:**")
            st.write("1. Upload photos of damage")
            st.write("2. Get instant repair quote")
            st.write("3. Schedule pickup")
            st.write("4. 7-14 day repair time")
            st.write("5. Delivery back to you")
        
        # Damage upload
        st.write("### 📸 Upload Damage Photos")
        uploaded_files = st.file_uploader("Upload up to 5 photos", 
                                         type=['jpg', 'png', 'jpeg'],
                                         accept_multiple_files=True)
        
        if uploaded_files:
            st.success(f"{len(uploaded_files)} photos uploaded for assessment")
            
        # Get quote button
        if st.button("🔄 Get Repair Quote", type="primary"):
            quote = random.randint(99, 599)
            st.success(f"**Estimated Repair Cost: ${quote}**")
            st.write("Price includes: Materials, labor, pickup & delivery")
    
    elif service == "🔄 Upcycle & Transform":
        st.write("### Transform Old into New")
        st.write("Don't replace - transform! We'll upcycle your furniture into something new.")
        
        # Transformation examples
        st.write("### Popular Transformations")
        
        transformations = [
            {"From": "Old Sofa", "To": "2 Chairs + Ottoman", "Cost": "$299", "Time": "2-3 weeks"},
            {"From": "Dining Table", "To": "Desk + Shelves", "Cost": "$199", "Time": "1-2 weeks"},
            {"From": "Wardrobe", "To": "Bookshelf + Cabinet", "Cost": "$249", "Time": "2 weeks"},
            {"From": "Bed Frame", "To": "Bench + Side Tables", "Cost": "$349", "Time": "3 weeks"},
        ]
        
        df = pd.DataFrame(transformations)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Custom upcycle request
        st.write("### 🎨 Custom Upcycle Idea")
        old_item = st.text_input("What furniture would you like to upcycle?")
        new_idea = st.text_area("What would you like it to become?")
        
        if old_item and new_idea:
            st.info(f"Great idea! Turning {old_item} into {new_idea}.")
            if st.button("Get Upcycle Quote"):
                st.success(f"**Estimated Cost: ${random.randint(199, 499)}**")
    
    elif service == "♻️ Responsible Recycling":
        st.write("### Zero-Waste Recycling")
        st.write("When furniture can't be repaired or upcycled, we ensure 100% responsible recycling.")
        
        st.write("**Our Recycling Process:**")
        steps = [
            "1. **Material Separation:** Wood, metal, fabric, foam separated",
            "2. **Wood Processing:** Turned into particle board or biomass energy",
            "3. **Metal Recycling:** Melted and reformed",
            "4. **Fabric Repurposing:** Converted to insulation or industrial rags",
            "5. **Foam Recycling:** Processed for carpet underlay"
        ]
        
        for step in steps:
            st.write(step)
        
        st.write("**Environmental Impact:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("CO₂ Saved", "85%")
        with col2:
            st.metric("Landfill Reduction", "100%")
        with col3:
            st.metric("Materials Recovered", "92%")
        
        st.info("✅ **Free recycling service** for all IN SPACE furniture")
    
    elif service == "📦 Take-Back Program":
        st.write("### Furniture Take-Back Program")
        st.write("Sell your old IN SPACE furniture back to us for store credit.")
        
        st.write("**How it works:**")
        st.write("1. Request a valuation online")
        st.write("2. We assess age, condition, materials")
        st.write("3. Get offer (30-60% of original value)")
        st.write("4. Schedule free pickup")
        st.write("5. Receive store credit instantly")
        
        # Valuation form
        st.write("### Get Your Valuation")
        
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Age (years)", 0, 20, 3)
            condition = st.select_slider("Condition", ["Poor", "Fair", "Good", "Excellent"])
        
        with col2:
            original_price = st.number_input("Original Price ($)", 500, 5000, 1200)
            material = st.selectbox("Primary Material", ["Teak", "Mango", "Blend", "Other"])
        
        if st.button("Calculate Valuation", type="primary"):
            # Simple valuation logic
            base_value = original_price * 0.5
            
            # Age depreciation
            age_factor = max(0.3, 1 - (age * 0.05))
            
            # Condition multipliers
            condition_map = {"Poor": 0.3, "Fair": 0.5, "Good": 0.7, "Excellent": 0.9}
            condition_factor = condition_map.get(condition, 0.5)
            
            # Material factor
            material_map = {"Teak": 1.1, "Mango": 1.0, "Blend": 1.0, "Other": 0.8}
            material_factor = material_map.get(material, 1.0)
            
            valuation = base_value * age_factor * condition_factor * material_factor
            
            st.success(f"**Estimated Value: ${int(valuation)}**")
            st.write(f"Store credit offer: **${int(valuation * 0.9)}**")
    
    # Impact dashboard
    st.divider()
    st.subheader("🌍 Your Circular Impact")
    
    impact_data = {
        "Metric": ["CO₂ Saved", "Trees Preserved", "Landfill Diverted", "Energy Saved"],
        "Your Impact": ["245 kg", "0.5 trees", "85 kg", "120 kWh"],
        "Community Total": ["12,450 kg", "25 trees", "4,250 kg", "6,000 kWh"]
    }
    
    st.dataframe(pd.DataFrame(impact_data), use_container_width=True, hide_index=True)
    
    st.caption("*Based on average furniture lifecycle analysis*")
