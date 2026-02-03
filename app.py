# in_space_local.py - COMPLETE IN SPACE APP - RUN LOCALLY
import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="IN SPACE FURNITURE",
    page_icon="🪑",
    layout="wide"
)

# ========== SESSION STATE ==========
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'current_product': None,
        'wood_type': None,
        'design': None,
        'room_size': None,
        'order_placed': False,
        'damage_history': []
    }

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    .product-box {
        border: 2px solid #2A5C3D;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        background: #f8f9fa;
    }
    .damage-card {
        border: 2px solid #dc3545;
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        background: #fff5f5;
    }
</style>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("🪑 IN SPACE")
    st.markdown("---")
    
    section = st.selectbox(
        "**SELECT SECTION:**",
        ["1. 🏠 Home", "2. 🔍 Search Product", "3. 📍 Location Analysis", 
         "4. 📏 Room Scan", "5. 🎨 Design Studio", "6. 👁️ AR View", 
         "7. 💰 Order", "8. ⚡ Damage Report", "9. 🔄 Transform Product"]
    )

# ========== SECTION 1: HOME ==========
if section == "1. 🏠 Home":
    st.title("IN SPACE FURNITURE")
    st.markdown("### Your wood's journey from tree to forever-use")
    
    # Journey visualization
    journey = pd.DataFrame({
        'Stage': ['Tree', 'Sofa', 'Chairs', 'Stool', 'Frame', 'Memory'],
        'Action': ['Harvested', 'Designed by you', 'Made from old sofa', 'Made from chair', 'Made from stool', 'Wood life ends'],
        'Years': [0, 5, 10, 15, 20, 25]
    })
    
    st.dataframe(journey, use_container_width=True)
    
    st.info("**Core Idea:** One piece of wood → Multiple products → Until wood dies")

# ========== SECTION 2: SEARCH PRODUCT ==========
elif section == "2. 🔍 Search Product":
    st.title("Step 1: Choose Your Product")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🛋️ SOFA", use_container_width=True):
            st.session_state.user_data['current_product'] = 'Sofa'
            st.success("Selected: Sofa")
    
    with col2:
        if st.button("🪑 CHAIR", use_container_width=True):
            st.session_state.user_data['current_product'] = 'Chair'
            st.success("Selected: Chair")
    
    with col3:
        if st.button("🛏️ BED", use_container_width=True):
            st.session_state.user_data['current_product'] = 'Bed'
            st.success("Selected: Bed")
    
    if st.session_state.user_data['current_product']:
        st.markdown(f"### ✅ Selected: {st.session_state.user_data['current_product']}")
        st.write("Next: We'll check your location for wood recommendations")

# ========== SECTION 3: LOCATION ANALYSIS ==========
elif section == "3. 📍 Location Analysis":
    st.title("Step 2: Location-Based Wood Recommendation")
    
    # Location input
    location = st.text_input("Enter your city:", "Chennai")
    
    if location:
        # Database of location problems (simulated)
        location_problems = {
            'Chennai': {'issues': ['high_humidity', 'termites'], 'wood': 'Treated Teak'},
            'Mumbai': {'issues': ['bed_bugs', 'humidity'], 'wood': 'Teak with bug-resistant coating'},
            'Delhi': {'issues': ['termites', 'dry_wood'], 'wood': 'Termite-proof Mango'},
            'Bangalore': {'issues': ['moderate_humidity'], 'wood': 'Mango Wood'}
        }
        
        if location in location_problems:
            data = location_problems[location]
            
            st.markdown(f"### 📍 {location} Analysis")
            
            # Issues found
            st.write("**Past problems in this area:**")
            for issue in data['issues']:
                if issue == 'high_humidity':
                    st.write(f"- 🚨 High humidity (wood warping risk)")
                elif issue == 'bed_bugs':
                    st.write(f"- 🐛 Bed bugs history")
                elif issue == 'termites':
                    st.write(f"- 🐜 Termite infestations")
                elif issue == 'dry_wood':
                    st.write(f"- 🌵 Very dry conditions")
            
            # Wood recommendation
            st.markdown(f"### 🪵 Recommended Wood: **{data['wood']}**")
            st.write(f"This wood is specially treated for {location}'s conditions")
            
            st.session_state.user_data['wood_type'] = data['wood']
            st.session_state.user_data['location'] = location
            
        else:
            st.warning("Location not in database. Using default: Mango Wood")
            st.session_state.user_data['wood_type'] = 'Mango Wood'

# ========== SECTION 4: ROOM SCAN ==========
elif section == "4. 📏 Room Scan":
    st.title("Step 3: Room Scanning & Placement")
    
    st.write("### 📱 Camera opens - Scan your room")
    
    # Room dimensions input
    col1, col2 = st.columns(2)
    
    with col1:
        width = st.slider("Room Width (ft)", 8, 30, 15)
    
    with col2:
        length = st.slider("Room Length (ft)", 8, 30, 12)
    
    # Furniture placement
    st.write("### 📍 Where to place the sofa?")
    
    placement = st.select_slider(
        "Position in room",
        options=["Near window", "Center", "Against wall", "Corner"]
    )
    
    # Calculate walking space
    if st.session_state.user_data['current_product'] == 'Sofa':
        sofa_size = 8  # ft
        walking_space = width - sofa_size if placement in ["Near window", "Against wall"] else min(width, length) - sofa_size
        
        st.metric("Walking Space", f"{walking_space} ft")
        
        if walking_space >= 4:
            st.success("✅ Good walking space maintained")
        else:
            st.warning("⚠️ Limited walking space. Consider smaller size.")
    
    st.session_state.user_data['room_size'] = f"{width}x{length}ft"
    st.session_state.user_data['placement'] = placement

# ========== SECTION 5: DESIGN STUDIO ==========
elif section == "5. 🎨 Design Studio":
    st.title("Step 4: AI Design Studio")
    
    st.write("### Empty product appears")
    st.markdown('<div class="product-box"><h3 style="text-align:center">[EMPTY PRODUCT]</h3></div>', unsafe_allow_html=True)
    
    # Design sidebar
    st.write("### 🎨 Design Elements (Sidebar)")
    
    designs = ["Peacock 🦚", "Lion 🦁", "Flowers 🌸", "Geometric ▢", "Tree 🌳", "Birds 🐦"]
    
    selected_designs = st.multiselect(
        "Choose design elements:",
        designs,
        default=["Peacock 🦚", "Lion 🦁"]
    )
    
    if selected_designs:
        st.write("**Selected:**", ", ".join(selected_designs))
        
        # AI Transformation
        if st.button("✨ AI Transform Design", type="primary"):
            with st.spinner("AI is creating a natural scene..."):
                time.sleep(2)
                
                if "Peacock 🦚" in selected_designs and "Lion 🦁" in selected_designs:
                    st.success("### 🧠 AI Transformation Complete!")
                    st.write("**Before:** Peacock + Lion randomly placed")
                    st.write("**After:** Lion sitting under peacock-feather tree")
                    st.write("**Scene:** Peaceful jungle setting")
                    
                    # Show transformed design
                    st.markdown("""
                    <div class="product-box">
                    <h4 style="text-align:center">🏞️ AI TRANSFORMED DESIGN</h4>
                    <p style="text-align:center">Lion resting under tree<br>made from peacock feathers</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.session_state.user_data['design'] = "Lion under peacock-tree"
                else:
                    st.info("AI will harmonize your selected elements")
    
    # Background context
    st.write("### 🏠 Room Context")
    room_type = st.selectbox("Where will this be placed?", 
                            ["Living Room", "Bedroom", "Office", "Balcony"])
    
    if room_type:
        st.write(f"AI will adjust design for: **{room_type}**")
        if room_type == "Living Room":
            st.write("- Creating cozy, welcoming scene")
        elif room_type == "Bedroom":
            st.write("- Creating peaceful, calm scene")

# ========== SECTION 6: AR VIEW ==========
elif section == "6. 👁️ AR View":
    st.title("Step 5: AR Preview")
    
    if not st.session_state.user_data.get('design'):
        st.warning("Please design your product first!")
    else:
        st.write("### 📱 AR Camera View")
        st.write("*(In real app: Your phone camera shows your room)*")
        
        # Simulated AR view
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Your Room**")
            st.image("https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400", 
                    caption="Your actual room", use_container_width=True)
        
        with col2:
            st.write("**With Furniture (AR)**")
            st.image("https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=400",
                    caption="Sofa placed in your room", use_container_width=True)
        
        # Controls
        st.write("### 🎮 AR Controls")
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.button("🔄 360° Rotate")
        with c2:
            st.button("👣 Walk Around")
        with c3:
            st.button("🌞 Change Lighting")
        with c4:
            st.button("📏 Adjust Position")
        
        st.success("✅ Perfect fit! Ready to order.")

# ========== SECTION 7: ORDER ==========
elif section == "7. 💰 Order":
    st.title("Step 6: Order & Delivery")
    
    # Display order summary
    st.markdown("### 📦 Order Summary")
    
    order_data = {
        'Product': [st.session_state.user_data.get('current_product', 'Sofa')],
        'Wood Type': [st.session_state.user_data.get('wood_type', 'Mango Wood')],
        'Design': [st.session_state.user_data.get('design', 'Custom Design')],
        'Room Size': [st.session_state.user_data.get('room_size', '15x12ft')],
        'Price': ['$1,200']
    }
    
    st.dataframe(pd.DataFrame(order_data), use_container_width=True, hide_index=True)
    
    # Place order
    if st.button("🚀 PLACE ORDER", type="primary", use_container_width=True):
        st.session_state.user_data['order_placed'] = True
        st.session_state.user_data['order_date'] = datetime.now().strftime("%Y-%m-%d")
        
        st.balloons()
        st.success("### ✅ ORDER CONFIRMED!")
        st.write("**Delivery:** 3-4 weeks")
        st.write("**You'll receive:**")
        st.write("- Your custom designed furniture")
        st.write("- Wood care instructions")
        st.write("- Circular service warranty")

# ========== SECTION 8: DAMAGE REPORT ==========
elif section == "8. ⚡ Damage Report":
    st.title("Step 7: Years Later - Damage Report")
    
    if not st.session_state.user_data.get('order_placed'):
        st.warning("Please place an order first to report damage!")
    else:
        st.markdown(f"### 📜 Purchase History")
        st.write(f"Product: {st.session_state.user_data.get('current_product')}")
        st.write(f"Purchase Date: {st.session_state.user_data.get('order_date', '2024-01-01')}")
        st.write(f"Wood Type: {st.session_state.user_data.get('wood_type')}")
        
        st.markdown("---")
        st.write("### 📸 Take photos of damage")
        
        # Photo upload simulation
        damage_angles = st.multiselect(
            "Take photos from these angles:",
            ["Front", "Back", "Left Side", "Right Side", "Top", "Bottom", "Close-up damage"],
            default=["Front", "Back", "Left Side", "Right Side"]
        )
        
        if damage_angles:
            st.write(f"**Photos taken from:** {', '.join(damage_angles)}")
            
            # AI Damage Analysis
            if st.button("🔍 ANALYZE DAMAGE", type="primary"):
                with st.spinner("AI analyzing damage percentage..."):
                    time.sleep(2)
                    
                    # Simulated damage analysis
                    good_wood = random.randint(40, 70)
                    damaged_wood = 100 - good_wood
                    
                    st.markdown('<div class="damage-card">', unsafe_allow_html=True)
                    st.markdown("### ⚡ DAMAGE ANALYSIS REPORT")
                    st.metric("Good Wood Remaining", f"{good_wood}%")
                    st.metric("Damaged Wood", f"{damaged_wood}%")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # What can be made
                    if good_wood >= 60:
                        new_products = ["2 Chairs", "Small Table"]
                    elif good_wood >= 40:
                        new_products = ["1 Chair", "Bookshelf"]
                    elif good_wood >= 20:
                        new_products = ["Stool", "Picture Frame"]
                    else:
                        new_products = ["Small decorative items"]
                    
                    st.write("### 🔄 What can be made:")
                    for product in new_products:
                        st.write(f"- {product}")
                    
                    # Save damage data
                    damage_entry = {
                        'date': datetime.now().strftime("%Y-%m-%d"),
                        'good_wood': good_wood,
                        'new_products': new_products
                    }
                    
                    if 'damage_history' not in st.session_state.user_data:
                        st.session_state.user_data['damage_history'] = []
                    
                    st.session_state.user_data['damage_history'].append(damage_entry)
                    st.session_state.user_data['current_good_wood'] = good_wood
                    st.session_state.user_data['possible_products'] = new_products

# ========== SECTION 9: TRANSFORM PRODUCT ==========
elif section == "9. 🔄 Transform Product":
    st.title("Step 8: Transform Old into New")
    
    if not st.session_state.user_data.get('current_good_wood'):
        st.warning("Please analyze damage first!")
    else:
        st.write(f"### ♻️ From: {st.session_state.user_data.get('current_product')}")
        st.write(f"### 🔄 To: New Product from {st.session_state.user_data['current_good_wood']}% good wood")
        
        # Select what to make
        possible = st.session_state.user_data.get('possible_products', ['Chair'])
        new_product = st.selectbox("What would you like to make?", possible)
        
        if new_product:
            st.markdown(f'<div class="product-box"><h3 style="text-align:center">[EMPTY {new_product.upper()}]</h3></div>', unsafe_allow_html=True)
            
            # Design the new product
            st.write("### 🎨 Design your new product")
            
            # Inherit previous designs?
            if st.checkbox("Keep previous designs (peacock + lion)"):
                st.write("Designs will be adapted to new product shape")
                
                if st.button("✨ AI Adapt Design", type="secondary"):
                    st.success("Design adapted! Peacock-tree scene adjusted for chair")
            
            # Add new designs
            new_designs = st.multiselect(
                "Add new design elements:",
                ["Peacock 🦚", "Lion 🦁", "Flowers 🌸", "Geometric ▢", "Tree 🌳", "Birds 🐦", "New Pattern ✨"]
            )
            
            if st.button("🚀 CREATE NEW PRODUCT", type="primary"):
                # Update product history
                old_product = st.session_state.user_data.get('current_product', 'Sofa')
                
                if 'product_history' not in st.session_state.user_data:
                    st.session_state.user_data['product_history'] = []
                
                st.session_state.user_data['product_history'].append({
                    'from': old_product,
                    'to': new_product,
                    'date': datetime.now().strftime("%Y-%m-%d"),
                    'wood_used': st.session_state.user_data['current_good_wood']
                })
                
                # Update current product
                st.session_state.user_data['current_product'] = new_product
                st.session_state.user_data['design'] = f"Adapted design for {new_product}"
                
                st.balloons()
                st.success(f"### ✅ {new_product} CREATED!")
                st.write(f"From old {old_product} → New {new_product}")
                st.write(f"Wood life extended by 5+ years")
                
                # Show complete journey
                st.markdown("---")
                st.write("### 🌳 Wood's Complete Journey:")
                
                if 'product_history' in st.session_state.user_data:
                    journey_df = pd.DataFrame(st.session_state.user_data['product_history'])
                    st.dataframe(journey_df, use_container_width=True)
                
                st.info("**Until the wood dies, we keep making new products from it**")

# ========== FOOTER ==========
st.markdown("---")
st.caption("🪑 IN SPACE FURNITURE | Core Idea Demo | Run locally for full features")

# Debug info (optional)
with st.expander("🔧 Debug Info"):
    st.write(st.session_state.user_data)
