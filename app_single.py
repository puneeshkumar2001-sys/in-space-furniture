# app_single.py - COMPLETE IN SPACE FURNITURE APP
# Run with: streamlit run app_single.py

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.graph_objects as go
from PIL import Image
import time

# ============================================
# 1. AR SCANNER MODULE
# ============================================
def scan_room():
    """Mock AR room scanning"""
    st.subheader("📱 AR Room Scanner")
    
    # Room upload or mock
    option = st.radio("Choose method:", ["Upload Room Photo", "Use Mock Room"])
    
    if option == "Upload Room Photo":
        room_img = st.file_uploader("Upload room photo (JPEG/PNG)", type=['jpg', 'jpeg', 'png'])
        if room_img:
            image = Image.open(room_img)
            st.image(image, caption="Your Room", use_column_width=True)
    else:
        # Show mock room
        st.info("Using demo room. In production: AR camera scanning with LiDAR.")
    
    # Run scan button
    if st.button("📏 Scan Room", type="primary") or option == "Use Mock Room":
        with st.spinner("Scanning room dimensions and climate..."):
            # Simulate scan progress
            progress_bar = st.progress(0)
            for percent in range(0, 101, 10):
                progress_bar.progress(percent)
                time.sleep(0.1)
            
            # Generate mock scan data
            humidity = random.randint(40, 90)
            temperature = random.randint(20, 38)
            
            # Display results
            st.success("✅ Room scan complete!")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Width", f"{random.randint(10, 20)} ft", "±2mm")
            with col2:
                st.metric("Length", f"{random.randint(12, 25)} ft", "±2mm")
            with col3:
                st.metric("Humidity", f"{humidity}%")
            with col4:
                st.metric("Temperature", f"{temperature}°C")
            
            # Additional data
            with st.expander("📊 Detailed Scan Data"):
                st.write("**Sunlight Analysis:**")
                st.progress(random.randint(30, 90)/100, text=f"{random.randint(3, 8)} hours direct sunlight")
                
                st.write("**Room Features:**")
                features = {
                    "Floor Type": random.choice(["Hardwood", "Tile", "Carpet"]),
                    "Window Count": random.randint(1, 5),
                    "Ceiling Height": f"{random.randint(8, 12)} ft",
                    "Walking Space": f"{random.randint(4, 8)} ft clearance"
                }
                for key, value in features.items():
                    st.write(f"- **{key}:** {value}")
            
            # Store in session state
            scan_data = {
                "dimensions": {
                    "width": random.randint(10, 20),
                    "length": random.randint(12, 25),
                    "height": random.randint(8, 12)
                },
                "climate": {
                    "humidity": humidity,
                    "temperature": temperature,
                    "sunlight_hours": random.randint(3, 8),
                    "location": random.choice(["Chennai", "Mumbai", "Delhi", "Bangalore"])
                },
                "walking_space": random.randint(4, 8),
                "scan_quality": f"{random.randint(95, 99)}% accurate"
            }
            
            st.session_state['room_data'] = scan_data
            return scan_data
    
    return st.session_state.get('room_data', None)

# ============================================
# 2. CLIMATE ADVISOR MODULE
# ============================================
def recommend_wood(climate_data):
    """Recommend wood based on climate data"""
    humidity = climate_data.get('humidity', 50)
    temperature = climate_data.get('temperature', 25)
    location = climate_data.get('location', 'Generic')
    
    # Recommendation logic
    if humidity > 75:
        recommendation = {
            "wood": "Teak",
            "reason": "Excellent for high humidity (75%+). Naturally resistant to water, warping, and pests.",
            "durability": "95/100",
            "maintenance": "Low",
            "sustainability": "FSC Certified Plantation",
            "cost": "$$$"
        }
    elif humidity > 60:
        recommendation = {
            "wood": "Teak/Mango Blend",
            "reason": "Optimal for moderate humidity. Combines Teak's durability with Mango's aesthetics.",
            "durability": "88/100",
            "maintenance": "Medium",
            "sustainability": "Fast-growing Mango with Teak core",
            "cost": "$$"
        }
    elif humidity > 40:
        recommendation = {
            "wood": "Mango Wood",
            "reason": "Ideal for moderate climates. Beautiful grain, sustainable choice.",
            "durability": "82/100",
            "maintenance": "Medium",
            "sustainability": "Highly sustainable (fruit tree byproduct)",
            "cost": "$$"
        }
    else:
        recommendation = {
            "wood": "Walnut/Oak Blend",
            "reason": "Perfect for dry conditions. Rich appearance, stable in low humidity.",
            "durability": "90/100",
            "maintenance": "Low",
            "sustainability": "Responsibly harvested",
            "cost": "$$$$"
        }
    
    # Adjust for temperature extremes
    if temperature > 35:
        recommendation["reason"] += " Heat-treated for tropical conditions."
    elif temperature < 15:
        recommendation["reason"] += " Cold-resistant treatment applied."
    
    return recommendation

def show_recommendation(climate_data):
    """Display wood recommendation with visualization"""
    if not climate_data:
        st.warning("Please scan your room first!")
        return None
    
    st.subheader("🌳 Smart Material Recommendation")
    
    # Get recommendation
    recommendation = recommend_wood(climate_data)
    
    # Display main recommendation
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Wood icon based on type
        wood_icons = {
            "Teak": "🪵",
            "Mango Wood": "🌳",
            "Teak/Mango Blend": "🪴",
            "Walnut/Oak Blend": "🌲"
        }
        icon = wood_icons.get(recommendation["wood"], "🪑")
        st.markdown(f"# {icon}")
        st.metric("Recommended Wood", recommendation["wood"])
        st.metric("Durability", recommendation["durability"])
        st.metric("Cost Level", recommendation["cost"])
    
    with col2:
        st.info(f"**Why {recommendation['wood']}?**")
        st.write(recommendation["reason"])
        st.write(f"**Sustainability:** {recommendation['sustainability']}")
        st.write(f"**Maintenance:** {recommendation['maintenance']}")
        
        # Climate match score
        humidity = climate_data.get('humidity', 50)
        match_score = 100 - abs(humidity - 65)  # Ideal humidity ~65%
        match_score = max(75, min(99, match_score))
        
        st.progress(match_score/100, text=f"Climate Match: {match_score}%")
    
    # Comparison table
    st.subheader("📊 Wood Comparison Table")
    
    woods_data = {
        "Wood Type": ["Teak", "Mango Wood", "Teak/Mango Blend", "Walnut/Oak"],
        "Humidity Resistance": ["95%", "70%", "85%", "80%"],
        "Durability (Years)": ["50+", "25+", "35+", "40+"],
        "Sustainability": ["High", "Very High", "High", "Medium"],
        "Best For": ["Coastal/Humid", "Moderate/Dry", "All-rounder", "Luxury/Dry"],
        "Price per ft³": ["$85", "$45", "$65", "$120"]
    }
    
    df = pd.DataFrame(woods_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.session_state['recommendation'] = recommendation
    return recommendation

# ============================================
# 3. AI DESIGNER MODULE
# ============================================
def ai_refine_design():
    """AI design refinement interface"""
    st.subheader("🎨 AI Design Studio")
    
    # User design input
    st.write("### 1. Your Design Input")
    
    col1, col2 = st.columns(2)
    
    with col1:
        style = st.selectbox(
            "Design Style",
            ["Modern Minimalist", "Traditional", "Bohemian", "Industrial", 
             "Scandinavian", "Mid-Century", "Coastal", "Rustic"],
            index=0
        )
        
        primary_color = st.color_picker("Primary Color", "#2A5C3D")
        secondary_color = st.color_picker("Secondary Color", "#D4A574")
        
        patterns = ["Solid", "Geometric", "Floral", "Striped", "Textured", "Animal Print"]
        pattern = st.multiselect("Patterns", patterns, default=["Geometric"])
    
    with col2:
        furniture_type = st.selectbox(
            "Furniture Type",
            ["Sofa", "Dining Table", "Bed Frame", "Bookshelf", "Coffee Table", "Cabinet"]
        )
        
        size = st.slider("Size Preference", 1, 10, 7, 
                        help="1 = Compact, 10 = Spacious")
        
        elements = st.text_area("Special Elements (e.g., lion motifs, peacock feathers)", 
                               "lion, peacock, geometric shapes")
    
    # AI Processing
    if st.button("✨ AI Refine Design", type="primary"):
        with st.spinner("AI is refining your design..."):
            progress_bar = st.progress(0)
            for percent in range(0, 101, 20):
                progress_bar.progress(percent)
                time.sleep(0.3)
            
            # Generate AI enhancements
            style_map = {
                "Modern Minimalist": "Clean lines, neutral palette, functional elegance",
                "Traditional": "Ornate details, rich woods, classic proportions",
                "Bohemian": "Layered textures, eclectic patterns, warm colors",
                "Industrial": "Raw materials, metal accents, utilitarian aesthetic"
            }
            
            color_palette = {
                "#2A5C3D": ["#3A7D5C", "#1B3D2A", "#E8F5E9"],  # Green theme
                "#D4A574": ["#E6C9A8", "#B08968", "#FAF3E9"]   # Wood theme
            }
            
            # AI suggestions
            ai_style = f"{style} with {random.choice(['contemporary', 'global', 'organic'])} influences"
            
            if "lion" in elements.lower() and "peacock" in elements.lower():
                ai_note = "**AI Insight:** Lion strength + peacock elegance = Regal yet approachable design. Blending motifs in asymmetric balance."
            else:
                ai_note = "**AI Insight:** Creating harmony between your selected elements with proportional balance."
            
            # Display AI refinement
            st.success("✅ Design Refined!")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.write("### Your Original")
                st.write(f"**Style:** {style}")
                st.write(f"**Colors:** {primary_color}, {secondary_color}")
                st.write(f"**Patterns:** {', '.join(pattern)}")
                st.write(f"**Elements:** {elements}")
            
            with col_b:
                st.write("### AI Enhanced Design")
                st.write(f"**Refined Style:** {ai_style}")
                st.write(f"**Color Palette:**")
                
                # Show color palette
                colors = color_palette.get(primary_color, ["#2A5C3D", "#3A7D5C", "#E8F5E9"])
                for color in colors:
                    st.markdown(f'<div style="background-color:{color}; padding:10px; margin:5px; border-radius:5px;">{color}</div>', 
                               unsafe_allow_html=True)
                
                st.write(f"**Pattern Harmony:** {' + '.join(pattern)} in graduated scale")
                st.write(f"**Element Integration:** Focal point with {elements.split(',')[0]}, accents with others")
            
            # Cohesion score
            cohesion_score = random.randint(82, 96)
            st.metric("🎯 Design Cohesion Score", f"{cohesion_score}/100")
            st.progress(cohesion_score/100)
            
            st.write("### 🎨 AI Design Notes")
            st.info(ai_note)
            st.write("**Recommended adjustments:**")
            st.write("1. Scale lion motifs to 60% original size for subtlety")
            st.write("2. Use peacock colors as accent stitching")
            st.write("3. Balance geometric patterns with solid surfaces")
            
            # Save to session
            design_data = {
                "original": {
                    "style": style,
                    "colors": [primary_color, secondary_color],
                    "patterns": pattern,
                    "elements": elements,
                    "furniture_type": furniture_type
                },
                "ai_enhanced": {
                    "style": ai_style,
                    "color_palette": colors,
                    "pattern_scheme": f"Graduated {pattern[0] if pattern else 'Solid'}",
                    "element_balance": "Asymmetric focal points",
                    "cohesion_score": cohesion_score
                }
            }
            
            st.session_state['design_data'] = design_data
            return design_data
    
    return st.session_state.get('design_data', None)

# ============================================
# 4. VIRTUAL TRY-ON MODULE
# ============================================
def create_3d_room(room_data, design_data):
    """Create 3D room visualization with furniture"""
    
    # Room dimensions
    width = room_data['dimensions']['width']
    length = room_data['dimensions']['length']
    height = room_data['dimensions']['height']
    
    # Furniture dimensions based on room size
    if width < 15:
        sofa_width = width * 0.6
        sofa_depth = 3
    else:
        sofa_width = 8
        sofa_depth = 3.5
    
    # Create figure
    fig = go.Figure()
    
    # Room walls (semi-transparent)
    # Floor
    fig.add_trace(go.Mesh3d(
        x=[0, width, width, 0],
        y=[0, 0, length, length],
        z=[0, 0, 0, 0],
        color='lightgray',
        opacity=0.3,
        name='Floor'
    ))
    
    # Furniture - Sofa
    sofa_x = [2, 2 + sofa_width, 2 + sofa_width, 2]
    sofa_y = [2, 2, 2 + sofa_depth, 2 + sofa_depth]
    sofa_z = [0, 0, 0, 0]
    
    # Use design color
    color = "#2A5C3D"  # Default green
    if design_data and 'ai_enhanced' in design_data:
        colors = design_data['ai_enhanced']['color_palette']
        color = colors[0] if colors else "#2A5C3D"
    
    fig.add_trace(go.Mesh3d(
        x=sofa_x + sofa_x,
        y=sofa_y + sofa_y,
        z=sofa_z + [0.8, 0.8, 0.8, 0.8],
        i=[0, 0, 0, 5, 5, 5],
        j=[1, 2, 3, 1, 2, 3],
        k=[2, 3, 1, 6, 7, 5],
        color=color,
        opacity=0.8,
        name='Your Sofa',
        showlegend=True
    ))
    
    # Walking space visualization
    walk_space_x = [2 + sofa_width, width - 2]
    walk_space_y = [2, length - 2]
    
    fig.add_trace(go.Mesh3d(
        x=[walk_space_x[0], walk_space_x[1], walk_space_x[1], walk_space_x[0]],
        y=[walk_space_y[0], walk_space_y[0], walk_space_y[1], walk_space_y[1]],
        z=[0, 0, 0, 0],
        color='lightblue',
        opacity=0.2,
        name=f"Walking Space ({room_data['walking_space']} ft)"
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': "3D Room Preview with Your Furniture",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        scene=dict(
            xaxis_title="Width (ft)",
            yaxis_title="Length (ft)",
            zaxis_title="Height (ft)",
            aspectmode="manual",
            aspectratio=dict(x=1, y=length/width, z=height/width),
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        width=800,
        height=600,
        showlegend=True
    )
    
    return fig

def show_virtual_tryon(room_data, design_data):
    """Display virtual try-on interface"""
    if not room_data:
        st.warning("Please scan your room first!")
        return
    
    st.subheader("👗 Virtual Try-On Experience")
    
    # Create 3D visualization
    fig = create_3d_room(room_data, design_data)
    st.plotly_chart(fig, use_container_width=True)
    
    # Interactive controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        view = st.selectbox("View Angle", ["Front", "Top", "Corner", "Walkthrough"])
    
    with col2:
        lighting = st.select_slider("Lighting", ["Morning", "Afternoon", "Evening", "Night"])
    
    with col3:
        if st.button("🔄 Rotate 360°", use_container_width=True):
            st.info("In production: Full 360° interactive rotation")
    
    # Fit analysis
    st.subheader("📊 Fit Analysis")
    
    # Calculate fit score
    room_area = room_data['dimensions']['width'] * room_data['dimensions']['length']
    sofa_area = 8 * 3.5  # Approximate sofa area
    
    fit_ratio = sofa_area / room_area
    if fit_ratio < 0.15:
        fit_score = 95
        fit_comment = "Perfect fit! Excellent walking space."
    elif fit_ratio < 0.25:
        fit_score = 85
        fit_comment = "Good fit. Comfortable space."
    else:
        fit_score = 70
        fit_comment = "Consider smaller size for better flow."
    
    # Adjust for walking space
    if room_data['walking_space'] > 6:
        fit_score += 5
    elif room_data['walking_space'] < 4:
        fit_score -= 10
    
    fit_score = min(99, max(70, fit_score))
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.metric("Fit Score", f"{fit_score}/100")
        st.progress(fit_score/100)
    
    with col_b:
        st.metric("Walking Space", f"{room_data['walking_space']} ft", 
                 delta="Adequate" if room_data['walking_space'] >= 4 else "Limited")
    
    with col_c:
        st.metric("Room Utilization", f"{int(fit_ratio*100)}%", 
                 delta="Optimal" if fit_ratio < 0.2 else "High")
    
    st.info(f"**Analysis:** {fit_comment}")
    
    # AR simulation note
    with st.expander("📱 AR Experience Preview"):
        st.write("**In the mobile app:**")
        st.write("1. Point camera at your room")
        st.write("2. Sofa appears in AR at exact scale")
        st.write("3. Walk around it, sit virtually")
        st.write("4. Adjust position with drag & drop")
        st.write("5. Change materials in real-time")
        
        # Mock AR image
        st.image("https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=800", 
                caption="AR Furniture Preview Concept")
    
    return fit_score

# ============================================
# 5. CIRCULAR SERVICE MODULE
# ============================================
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

# ============================================
# MAIN APP
# ============================================
def main():
    # Page configuration
    st.set_page_config(
        page_title="IN SPACE FURNITURE",
        page_icon="🪑",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #2A5C3D;
            text-align: center;
            margin-bottom: 1rem;
        }
        .sub-header {
            font-size: 1.2rem;
            color: #666;
            text-align: center;
            margin-bottom: 2rem;
        }
        .feature-card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            border-left: 4px solid #2A5C3D;
        }
        .stProgress > div > div > div > div {
            background-color: #2A5C3D;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'room_data' not in st.session_state:
        st.session_state.room_data = None
    if 'design_data' not in st.session_state:
        st.session_state.design_data = None
    if 'recommendation' not in st.session_state:
        st.session_state.recommendation = None
    if 'quote' not in st.session_state:
        st.session_state.quote = None
    
    # Sidebar navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/armchair.png", width=80)
        st.title("IN SPACE")
        st.caption("Furniture That Fits • AI That Designs • Planet That Benefits")
        
        st.divider()
        
        page = st.radio(
            "Navigate Your Journey:",
            [
                "🏠 Home",
                "📱 1. Scan Room",
                "🌳 2. Material Advisor", 
                "🎨 3. AI Design Studio",
                "👗 4. Virtual Try-On",
                "💰 5. Quote & Order",
                "♻️ 6. Circular Service",
                "📊 Investor View"
            ],
            index=0
        )
        
        st.divider()
        
        if st.session_state.room_data:
            st.success("✅ Room scanned")
        if st.session_state.design_data:
            st.success("✅ Design created")
        
        st.caption("Demo Version 1.0")
        if st.button("🔄 Reset Demo"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Main page routing
    if page == "🏠 Home":
        show_home()
    elif page == "📱 1. Scan Room":
        show_scan_room()
    elif page == "🌳 2. Material Advisor":
        show_material_advisor()
    elif page == "🎨 3. AI Design Studio":
        show_design_studio()
    elif page == "👗 4. Virtual Try-On":
        show_tryon()
    elif page == "💰 5. Quote & Order":
        show_quote()
    elif page == "♻️ 6. Circular Service":
        show_circular_service_page()
    elif page == "📊 Investor View":
        show_investor_view()

# ============================================
# PAGE FUNCTIONS
# ============================================
def show_home():
    st.markdown('<div class="main-header">IN SPACE FURNITURE</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">From Room Scan to Circular Design — Furniture That Fits Your Space, Style, and Planet</div>', unsafe_allow_html=True)
    
    # Hero image
    st.image("https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200", 
             use_column_width=True, 
             caption="Design. Preview. Live Sustainably.")
    
    # Value proposition
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 📱 Scan")
            st.write("AR room mapping + climate analysis")
            st.caption("Know what fits, what lasts")
    
    with col2:
        with st.container(border=True):
            st.markdown("### 🎨 Design")
            st.write("AI-powered furniture designer")
            st.caption("From idea to professional design")
    
    with col3:
        with st.container(border=True):
            st.markdown("### ♻️ Sustain")
            st.write("Circular repair & upcycling")
            st.caption("Lifetime value, zero waste")
    
    st.divider()
    
    # Quick start
    st.markdown("### 🚀 Quick Start")
    start_col1, start_col2, start_col3 = st.columns(3)
    
    with start_col1:
        if st.button("Start with Room Scan", type="primary", use_container_width=True):
            st.session_state.page = "📱 1. Scan Room"
            st.rerun()
    
    with start_col2:
        if st.button("Try AI Designer", use_container_width=True):
            st.session_state.page = "🎨 3. AI Design Studio"
            st.rerun()
    
    with start_col3:
        if st.button("See Circular Service", use_container_width=True):
            st.session_state.page = "♻️ 6. Circular Service"
            st.rerun()
    
    # Stats
    st.divider()
    st.markdown("### 📊 By The Numbers")
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    with stat_col1:
        st.metric("Returns Reduced", "47%", "via virtual try-on")
    with stat_col2:
        st.metric("Lifespan Increased", "3.2x", "with climate-matched materials")
    with stat_col3:
        st.metric("Waste Diverted", "85%", "through circular service")
    with stat_col4:
        st.metric("Design Time", "-70%", "with AI refinement")

def show_scan_room():
    st.title("Step 1: Room Scanning")
    st.write("Scan your space with AR to get precise measurements and climate analysis.")
    
    room_data = scan_room()
    
    if room_data:
        st.session_state.room_data = room_data
        
        # Next step button
        st.divider()
        if st.button("Next: Material Recommendation →", type="primary", use_container_width=True):
            st.rerun()

def show_material_advisor():
    st.title("Step 2: Smart Material Selection")
    st.write("Based on your room's climate, we recommend the perfect wood for durability.")
    
    if st.session_state.room_data:
        recommendation = show_recommendation(st.session_state.room_data['climate'])
        
        if recommendation:
            st.divider()
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button("Next: Design Your Furniture →", type="primary", use_container_width=True):
                    st.rerun()
            with col2:
                if st.button("← Back to Scan", use_container_width=True):
                    st.rerun()
    else:
        st.warning("Please scan your room first!")
        if st.button("Go to Room Scanner", type="primary"):
            st.rerun()

def show_design_studio():
    st.title("Step 3: AI Design Studio")
    st.write("Design your furniture and let AI refine it into a cohesive, professional piece.")
    
    design_data = ai_refine_design()
    
    if design_data:
        st.session_state.design_data = design_data
        
        st.divider()
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("Next: See It In Your Room →", type="primary", use_container_width=True):
                st.rerun()
        with col2:
            if st.button("← Back", use_container_width=True):
                st.rerun()

def show_tryon():
    st.title("Step 4: Virtual Try-On")
    st.write("See your designed furniture in your room before you buy.")
    
    if st.session_state.room_data:
        fit_score = show_virtual_tryon(st.session_state.room_data, st.session_state.design_data)
        
        st.divider()
        if fit_score and fit_score > 80:
            st.success(f"✅ Excellent fit! Ready to order.")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button("Get Quote & Order →", type="primary", use_container_width=True):
                    st.rerun()
            with col2:
                if st.button("← Redesign", use_container_width=True):
                    st.rerun()
        else:
            st.warning("Consider adjusting your design for better fit.")
            if st.button("Redesign with AI", type="primary"):
                st.rerun()
    else:
        st.warning("Please complete previous steps first!")
        if st.button("Start with Room Scan", type="primary"):
            st.rerun()

def show_quote():
    st.title("Step 5: Quote & Order")
    st.write("Transparent pricing and seamless ordering.")
    
    # Calculate quote
    base_price = 1200
    
    if st.session_state.get('recommendation'):
        if st.session_state.recommendation.get('wood') == 'Teak':
            base_price = 1400
        elif st.session_state.recommendation.get('wood') == 'Walnut/Oak Blend':
            base_price = 1800
    
    # Display quote
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Order Summary")
        
        st.write("**Items:**")
        if st.session_state.design_data:
            furniture_type = st.session_state.design_data['original']['furniture_type']
            st.write(f"- {furniture_type} (Custom Design)")
        else:
            st.write("- Custom Sofa")
        
        if st.session_state.get('recommendation'):
            st.write(f"- Material: {st.session_state.recommendation['wood']}")
            st.write(f"- Sustainability: {st.session_state.recommendation['sustainability']}")
        
        st.divider()
        
        st.write("**Cost Breakdown:**")
        st.write(f"- Materials: ${int(base_price * 0.5)}")
        st.write(f"- Craftsmanship: ${int(base_price * 0.35)}")
        st.write(f"- Sustainable Finish: ${int(base_price * 0.1)}")
        st.write(f"- Circular Service Fee: ${int(base_price * 0.05)}")
        
        st.divider()
        st.metric("Total", f"${base_price}", "All-inclusive")
        
        # Order button
        if st.button("🛒 Place Order", type="primary", use_container_width=True):
            st.session_state.quote = base_price
            st.success("Order placed successfully!")
            st.balloons()
            st.info("Expected delivery: 3-4 weeks. You'll receive tracking updates.")
    
    with col2:
        st.subheader("Order Timeline")
        
        timeline = [
            {"Step": "Design Finalization", "Time": "1-2 days", "Status": "✅"},
            {"Step": "Material Sourcing", "Time": "3-5 days", "Status": "⏳"},
            {"Step": "Craftsmanship", "Time": "10-14 days", "Status": "📅"},
            {"Step": "Quality Check", "Time": "2-3 days", "Status": "📅"},
            {"Step": "Delivery", "Time": "3-5 days", "Status": "📅"}
        ]
        
        for item in timeline:
            st.write(f"{item['Status']} **{item['Step']}**")
            st.caption(f"{item['Time']}")
            st.progress(0.2 if item['Status'] == "⏳" else 1.0 if item['Status'] == "✅" else 0.0)
        
        st.divider()
        st.write("**Warranty:** 5 years")
        st.write("**Circular Service:** Included")
    
    st.divider()
    
    if st.button("Next: Learn About Circular Service →", use_container_width=True):
        st.rerun()

def show_circular_service_page():
    st.title("Step 6: Circular Service")
    st.write("Extend your furniture's life. Repair, upcycle, or recycle responsibly.")
    
    show_circular_service()
    
    st.divider()
    st.success("""
    **Complete the Cycle:** 
    Every IN SPACE purchase includes our circular service guarantee.
    Your furniture will never end up in a landfill.
    """)

def show_investor_view():
    st.title("IN SPACE FURNITURE - Investor Overview")
    
    # Executive Summary
    st.header("🎯 Executive Summary")
    st.write("""
    IN SPACE is an AI-powered furniture ecosystem that combines AR room scanning, 
    climate-aware material recommendations, AI design refinement, and circular economy services.
    We're addressing the $800B furniture industry's core problems: poor fit, material failure, 
    design frustration, and environmental waste.
    """)
    
    # Market Opportunity
    st.header("📈 Market Opportunity")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Global Furniture Market", "$800B")
    with col2:
        st.metric("Online Furniture Growth", "18% CAGR")
    with col3:
        st.metric("Sustainable Furniture Demand", "$90B")
    
    # Technology Stack
    st.header("🛠️ Technology Stack")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.write("**Core IP:**")
        st.write("- Proprietary AR scanning algorithm")
        st.write("- Climate-material recommendation engine")
        st.write("- AI design refinement model (GAN-based)")
        st.write("- Circular logistics platform")
    
    with tech_col2:
        st.write("**Development:**")
        st.write("- **MVP:** Streamlit (this demo)")
        st.write("- **Phase 2:** React Native + ARKit/ARCore")
        st.write("- **Phase 3:** Custom AI/ML deployment")
    
    # Business Model
    st.header("💰 Business Model")
    
    revenue_streams = {
        "Stream": ["Furniture Sales", "AI Design License", "Circular Subscriptions", "Data Insights"],
        "Margin": ["40%", "85%", "70%", "90%"],
        "Year 1": ["$500K", "$50K", "$30K", "$20K"],
        "Year 3": ["$8M", "$1.2M", "$800K", "$500K"]
    }
    
    st.dataframe(pd.DataFrame(revenue_streams), use_container_width=True, hide_index=True)
    
    # Funding Ask
    st.header("💵 Funding Request")
    
    funding_col1, funding_col2, funding_col3 = st.columns(3)
    
    with funding_col1:
        st.metric("Seed Round", "$1.5M")
    with funding_col2:
        st.metric("Runway", "18 months")
    with funding_col3:
        st.metric("Valuation (post)", "$8M")
    
    st.write("**Use of Funds:**")
    st.write("- 50%: Tech development (AR/AI team)")
    st.write("- 30%: Pilot program & partnerships")
    st.write("- 15%: Operations & marketing")
    st.write("- 5%: Legal & IP protection")
    
    # Team
    st.header("👥 Team")
    st.write("- **Founder:** [Your Name] - Furniture design + tech vision")
    st.write("- **Seeking:** CTO with AR/AI experience")
    st.write("- **Advisors:** Furniture industry veterans, sustainability experts")
    
    # Next Steps
    st.header("🚀 Next Steps")
    st.write("1. Build native AR app (React Native)")
    st.write("2. Partner with 3 artisan workshops")
    st.write("3. Launch pilot program (100 customers)")
    st.write("4. Raise Series A ($5M) in 18 months")

# ============================================
# RUN THE APP
# ============================================
if __name__ == "__main__":
    main()
