# app.py - COMPLETE IN SPACE FURNITURE WITH ALL FEATURES
import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import altair as alt
import base64
from io import BytesIO

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
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0;
        color: white;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .metric-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        border: 3px solid #2A5C3D;
        text-align: center;
        box-shadow: 0 5px 15px rgba(42, 92, 61, 0.1);
    }
    .stButton button {
        background: linear-gradient(135deg, #2A5C3D 0%, #3A7D5C 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ========== SESSION STATE ==========
if 'room_data' not in st.session_state:
    st.session_state.room_data = None
if 'design_data' not in st.session_state:
    st.session_state.design_data = None
if 'wood_recommendation' not in st.session_state:
    st.session_state.wood_recommendation = None
if 'order_placed' not in st.session_state:
    st.session_state.order_placed = False

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
    
    # Progress tracker
    progress = 0
    if st.session_state.room_data:
        progress += 25
        st.success("✅ Room Scanned")
    if st.session_state.wood_recommendation:
        progress += 25
        st.success("✅ Materials Selected")
    if st.session_state.design_data:
        progress += 25
        st.success("✅ Design Created")
    if st.session_state.order_placed:
        progress += 25
        st.success("✅ Order Placed")
    
    st.progress(progress/100)
    st.caption(f"**Journey:** {progress}% complete")
    
    st.markdown("---")
    st.info("🚀 **All Features Active**")
    st.caption("3D • AI • AR • Circular Economy")

# ========== PAGE 1: HOME ==========
if page == "🏠 HOME - Vision":
    st.markdown('<div class="main-header">IN SPACE FURNITURE</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-size: 1.5rem; color: #666; margin-bottom: 3rem;">From Room Scan to Circular Design — Complete Ecosystem</div>', unsafe_allow_html=True)
    
    # Hero Section
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### 🚀 **The Complete Furniture Revolution**")
        st.markdown("""
        **We're building what IKEA, Wayfair, and Amazon haven't:**
        
        ✅ **📱 AR Room Scanning** - Millimeter accuracy, climate sensing  
        ✅ **🌳 AI Material Science** - Wood recommendations based on local weather  
        ✅ **🎨 AI Design Refinement** - Turn amateur ideas into professional designs  
        ✅ **👗 Virtual Try-On** - See furniture in your space before buying  
        ✅ **♻️ Circular Economy** - Repair, upcycle, recycle forever-system  
        ✅ **📊 Data Intelligence** - Climate + design trends for brands
        
        **This isn't an app — it's an ecosystem.**
        """)
        
        # CTA Buttons
        col1a, col1b, col1c = st.columns(3)
        with col1a:
            if st.button("🚀 Start Demo", use_container_width=True):
                st.rerun()
        with col1b:
            if st.button("📊 Investor View", use_container_width=True):
                st.rerun()
        with col1c:
            if st.button("🎥 Watch Video", use_container_width=True):
                st.info("Video: AR scanning + AI design in action")
    
    with col2:
        # Interactive 3D Visualization with Altair
        st.markdown("### 🏠 **3D Room Preview**")
        
        # Create 3D-like visualization with Altair
        data = pd.DataFrame({
            'x': np.random.randn(200),
            'y': np.random.randn(200),
            'z': np.random.randn(200)
        })
        
        chart = alt.Chart(data).mark_circle(size=60).encode(
            x='x:Q',
            y='y:Q',
            color=alt.value('#2A5C3D'),
            tooltip=['x', 'y']
        ).properties(
            width=400,
            height=300
        ).interactive()
        
        st.altair_chart(chart, use_container_width=True)
        
        st.markdown("**Features:**")
        st.write("• Interactive 3D room visualization")
        st.write("• Furniture placement simulation")
        st.write("• Walking space analysis")
        st.write("• Lighting simulation")
        
        # Quick Stats
        st.markdown("### 📈 **Live Metrics**")
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("Fit Accuracy", "97%", "±2mm")
        with metric_col2:
            st.metric("Returns Reduced", "63%", "via AR")

# ========== PAGE 2: AR ROOM SCAN ==========
elif page == "📱 1. AR ROOM SCAN":
    st.title("📱 Step 1: AR Room Scanning")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏠 **Live Room Analysis**")
        
        # Room upload with preview
        uploaded_file = st.file_uploader("📸 Upload room photo or use AR camera", 
                                        type=['jpg', 'png', 'jpeg'])
        
        if uploaded_file:
            # Convert to base64 for display
            bytes_data = uploaded_file.getvalue()
            st.image(bytes_data, caption="Your Room", use_container_width=True)
        
        # AR Controls
        st.markdown("### 🎮 **AR Controls**")
        ar_col1, ar_col2, ar_col3 = st.columns(3)
        with ar_col1:
            if st.button("📏 Measure Room", use_container_width=True):
                with st.spinner("Measuring with LiDAR..."):
                    time.sleep(2)
                    st.success("Dimensions: 15.2×12.8 ft")
        with ar_col2:
            if st.button("🌡️ Scan Climate", use_container_width=True):
                with st.spinner("Analyzing humidity, sunlight..."):
                    time.sleep(1.5)
                    humidity = random.randint(65, 85)
                    st.success(f"Humidity: {humidity}% | Temp: {random.randint(25, 35)}°C")
        with ar_col3:
            if st.button("📐 3D Map", use_container_width=True):
                with st.spinner("Creating 3D point cloud..."):
                    time.sleep(2.5)
                    st.success("3D mesh generated: 95% accuracy")
        
        # Start Full Scan
        if st.button("🚀 **START COMPLETE AR SCAN**", type="primary", use_container_width=True):
            with st.spinner("Initializing AR session..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                    time.sleep(0.03)
                
                # Generate comprehensive scan data
                scan_data = {
                    "dimensions": {
                        "width": 15.2,
                        "length": 12.8,
                        "height": 10.5,
                        "area": 194.56,
                        "volume": 2042.88
                    },
                    "climate": {
                        "humidity": 78,
                        "temperature": 32,
                        "sunlight_hours": 6.5,
                        "uv_index": 8,
                        "location": "Chennai",
                        "climate_zone": "Tropical Wet"
                    },
                    "features": {
                        "windows": 3,
                        "doors": 2,
                        "floor_type": "Marble",
                        "wall_color": "Off-White",
                        "lighting": "Natural + Artificial"
                    },
                    "walking_space": 5.8,
                    "scan_metrics": {
                        "accuracy": "98.7%",
                        "points_scanned": "2.4M",
                        "processing_time": "4.2s",
                        "data_size": "45.8 MB"
                    }
                }
                
                st.session_state.room_data = scan_data
                
                # Success animation
                st.balloons()
                st.success("""
                ✅ **AR SCAN COMPLETE!**
                
                **Room:** 15.2×12.8×10.5 ft  
                **Climate:** 78% humidity, 32°C (Chennai)  
                **Accuracy:** 98.7% (±2mm)  
                **Data:** 2.4M points scanned
                """)
    
    with col2:
        st.markdown("### 📊 **Scan Analytics**")
        
        if st.session_state.room_data:
            data = st.session_state.room_data
            
            # Metrics display
            st.metric("Room Area", f"{data['dimensions']['area']} ft²", "Precise")
            st.metric("Humidity", f"{data['climate']['humidity']}%", "High")
            st.metric("Walking Space", f"{data['walking_space']} ft", "Optimal")
            st.metric("Scan Accuracy", data['scan_metrics']['accuracy'], "")
            
            # Climate visualization
            st.markdown("#### 🌡️ Climate Analysis")
            climate_df = pd.DataFrame({
                'Parameter': ['Humidity', 'Temperature', 'Sunlight', 'UV Index'],
                'Value': [
                    data['climate']['humidity'],
                    data['climate']['temperature'],
                    data['climate']['sunlight_hours'],
                    data['climate']['uv_index']
                ],
                'Optimal': [65, 25, 6, 5]
            })
            
            chart = alt.Chart(climate_df).mark_bar().encode(
                x='Parameter:N',
                y='Value:Q',
                color=alt.condition(
                    alt.datum.Value > alt.datum.Optimal,
                    alt.value('#ff6b6b'),  # red if above optimal
                    alt.value('#2A5C3D')   # green if optimal or below
                )
            ).properties(height=200)
            
            st.altair_chart(chart, use_container_width=True)
            
            # Recommendations
            st.markdown("#### 💡 **Immediate Insights**")
            if data['climate']['humidity'] > 70:
                st.warning("⚠️ **High humidity detected** - Recommend moisture-resistant materials")
            if data['walking_space'] < 4:
                st.warning("⚠️ **Limited walking space** - Consider compact furniture")
            
            st.info(f"📍 **Location:** {data['climate']['location']} ({data['climate']['climate_zone']})")
        else:
            st.info("👆 **Start an AR scan to see real-time analytics here**")
            st.image("https://images.unsplash.com/photo-1556228453-efd6c1ff04f6", 
                    caption="AR Furniture Preview", use_container_width=True)

# ========== PAGE 3: SMART MATERIALS ==========
elif page == "🌳 2. SMART MATERIALS":
    st.title("🌳 Step 2: Climate-Aware Material Science")
    
    if not st.session_state.room_data:
        st.warning("⚠️ Please scan your room first to get climate-specific recommendations!")
        if st.button("← Go to Room Scanner", type="secondary"):
            st.rerun()
    else:
        climate_data = st.session_state.room_data['climate']
        humidity = climate_data['humidity']
        location = climate_data['location']
        
        st.markdown(f"### 🌍 **Your Climate Profile: {location}**")
        
        # Climate Score Calculation
        base_score = 100 - abs(humidity - 65)
        temp_score = 100 - abs(climate_data['temperature'] - 25)
        overall_score = (base_score + temp_score) // 2
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Humidity", f"{humidity}%", f"{'High' if humidity > 70 else 'Optimal'}")
        with col2:
            st.metric("Temperature", f"{climate_data['temperature']}°C", "Tropical")
        with col3:
            st.metric("Climate Score", f"{overall_score}/100", "Match")
        
        # Wood Recommendation Engine
        st.markdown("### 🎯 **AI Material Recommendation**")
        
        if humidity > 75:
            recommendation = {
                "wood": "**Premium Teak**",
                "icon": "🪵",
                "reason": "**EXCELLENT for tropical climates** - Natural oils repel water, resistant to termites, expands/contracts minimally",
                "properties": {
                    "Humidity Resistance": "98%",
                    "Durability": "50+ years",
                    "Maintenance": "Low",
                    "Sustainability": "FSC Certified",
                    "Cost Index": "9/10"
                },
                "science": "Teak contains natural tectoquinones and silica that prevent fungal growth and water absorption.",
                "best_for": "Coastal areas, high humidity (>70%), outdoor furniture"
            }
        elif humidity > 65:
            recommendation = {
                "wood": "**Teak-Mango Hybrid**",
                "icon": "🌳",
                "reason": "**OPTIMAL balance** - Teak core for structure, Mango exterior for aesthetics and sustainability",
                "properties": {
                    "Humidity Resistance": "88%",
                    "Durability": "35+ years",
                    "Maintenance": "Medium",
                    "Sustainability": "Very High",
                    "Cost Index": "7/10"
                },
                "science": "Engineered lamination: Teak provides structural integrity, Mango reduces cost and environmental impact.",
                "best_for": "Moderate humidity (60-75%), indoor furniture, mixed climates"
            }
        elif humidity > 50:
            recommendation = {
                "wood": "**Solid Mango Wood**",
                "icon": "🪴",
                "reason": "**SUSTAINABLE & BEAUTIFUL** - Fast-growing, unique grain patterns, carbon-negative",
                "properties": {
                    "Humidity Resistance": "75%",
                    "Durability": "25+ years",
                    "Maintenance": "Medium",
                    "Sustainability": "Excellent",
                    "Cost Index": "5/10"
                },
                "science": "Mango wood is a fruit tree byproduct. Denser than pine, beautiful grain, formaldehyde-free finishes available.",
                "best_for": "Moderate climates (50-65% humidity), eco-conscious buyers, indoor use"
            }
        else:
            recommendation = {
                "wood": "**Walnut-Oak Fusion**",
                "icon": "🌲",
                "reason": "**LUXURY & STABILITY** - Rich aesthetics, minimal movement in dry conditions, heirloom quality",
                "properties": {
                    "Humidity Resistance": "85%",
                    "Durability": "40+ years",
                    "Maintenance": "Low",
                    "Sustainability": "Good",
                    "Cost Index": "10/10"
                },
                "science": "Quarter-sawn construction minimizes wood movement. Walnut provides richness, Oak provides strength.",
                "best_for": "Dry climates (<50% humidity), luxury interiors, statement pieces"
            }
        
        # Display Recommendation
        st.markdown(f"## {recommendation['icon']} {recommendation['wood']}")
        st.success(recommendation['reason'])
        
        # Properties Table
        st.markdown("#### 📊 **Material Properties**")
        props_df = pd.DataFrame({
            'Property': list(recommendation['properties'].keys()),
            'Value': list(recommendation['properties'].values())
        })
        st.dataframe(props_df, use_container_width=True, hide_index=True)
        
        # Scientific Insight
        with st.expander("🔬 **Materials Science Details**"):
            st.write(recommendation['science'])
            st.write(f"**Best for:** {recommendation['best_for']}")
            
            # Comparative Chart
            woods = ['Teak', 'Mango', 'Teak-Mango', 'Walnut-Oak']
            humidity_resist = [98, 75, 88, 85]
            sustainability = [8, 10, 9, 7]
            cost = [9, 5, 7, 10]
            
            chart_data = pd.DataFrame({
                'Wood': woods * 3,
                'Metric': ['Humidity Resist']*4 + ['Sustainability']*4 + ['Cost Index']*4,
                'Value': humidity_resist + sustainability + cost
            })
            
            chart = alt.Chart(chart_data).mark_bar().encode(
                x='Wood:N',
                y='Value:Q',
                color='Metric:N',
                column='Metric:N'
            ).properties(width=150, height=200)
            
            st.altair_chart(chart)
        
        # Action Button
        st.session_state.wood_recommendation = recommendation
        
        if st.button("✅ **SELECT THIS MATERIAL & CONTINUE**", type="primary", use_container_width=True):
            st.balloons()
            st.success(f"Selected: {recommendation['wood']} for your {location} climate")
            st.rerun()

# ========== PAGE 4: AI DESIGN STUDIO ==========
elif page == "🎨 3. AI DESIGN STUDIO":
    st.title("🎨 Step 3: AI Design Studio")
    
    # Lion + Peacock Example
    st.markdown("### 🦁 **Case Study: Lion + Peacock Fusion**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Before AI Refinement**")
        st.markdown("""
        **User Input:**
        - Lion motifs (large, dominant)
        - Peacock feathers (colorful, detailed)
        - Traditional Indian style
        - Dark wood finish
        
        **Problems:**
        1. Scale mismatch (lion too large)
        2. Color clash (too many bright colors)
        3. Style confusion (traditional vs modern)
        4. Visual overload (no focal point)
        """)
    
    with col2:
        st.markdown("#### **After AI Refinement**")
        st.markdown("""
        **AI-Enhanced Design:**
        - Lion motifs scaled to 60% (subtle strength)
        - Peacock colors as accent stitching
        - Modern-traditional fusion style
        - Teak wood with satin finish
        
        **Improvements:**
        1. ✅ Balanced proportions
        2. ✅ Harmonious color palette
        3. ✅ Clear style direction
        4. ✅ Defined focal points
        """)
    
    st.markdown("---")
    
    # Interactive Design Studio
    st.markdown("### 🎨 **Design Your Furniture**")
    
    design_col1, design_col2 = st.columns(2)
    
    with design_col1:
        st.markdown("#### **Basic Parameters**")
        furniture_type = st.selectbox(
            "Furniture Type",
            ["Sofa", "Dining Table", "Bed Frame", "Bookshelf", "Coffee Table", "Cabinet", "Console Table"],
            index=0
        )
        
        style = st.selectbox(
            "Design Style",
            ["Modern Minimalist", "Traditional", "Bohemian", "Industrial", "Scandinavian", 
             "Mid-Century Modern", "Coastal", "Rustic", "Art Deco", "Japanese Wabi-Sabi"],
            index=0
        )
        
        primary_color = st.color_picker("Primary Color", "#2A5C3D")
        secondary_color = st.color_picker("Secondary Color", "#D4A574")
    
    with design_col2:
        st.markdown("#### **Advanced Features**")
        
        elements = st.text_area(
            "Special Elements & Inspiration",
            "e.g., lion motifs, peacock feathers, geometric patterns, floral carvings, metallic accents",
            height=100
        )
        
        complexity = st.slider("Design Complexity", 1, 10, 7,
                             help="1 = Simple, 10 = Highly Ornate")
        
        sustainability = st.slider("Sustainability Priority", 1, 10, 8,
                                 help="1 = Cost-focused, 10 = Eco-maximalist")
    
    # AI Processing
    if st.button("✨ **PROCESS WITH AI DESIGN ENGINE**", type="primary", use_container_width=True):
        with st.spinner("AI is analyzing and refining your design..."):
            # Simulate AI processing
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            steps = [
                "Analyzing style coherence...",
                "Evaluating color harmony...",
                "Optimizing proportions...",
                "Checking material compatibility...",
                "Generating refinement suggestions...",
                "Creating final design..."
            ]
            
            for i, step in enumerate(steps):
                progress_bar.progress((i + 1) * 100 // len(steps))
                status_text.text(f"🔄 {step}")
                time.sleep(0.8)
            
            # Generate AI results
            ai_style = f"{style} with {random.choice(['contemporary', 'global fusion', 'organic modern'])} influences"
            
            if "lion" in elements.lower() and "peacock" in elements.lower():
                ai_insight = "**AI Insight:** Lion (strength) + Peacock (elegance) = Regal yet approachable. Blending motifs in asymmetric balance creates visual interest without overwhelm."
                color_palette = ["#2A5C3D", "#3A7D5C", "#D4A574", "#F5E6D3", "#1B3D2A"]
            else:
                ai_insight = "**AI Insight:** Creating harmony between your selected elements with proportional balance and graduated contrasts."
                color_palette = [primary_color, secondary_color, "#FFFFFF", "#000000", "#F0F0F0"]
            
            cohesion_score = max(70, min(99, 85 + complexity - sustainability + random.randint(-5, 5)))
            
            # Store results
            st.session_state.design_data = {
                "original": {
                    "furniture_type": furniture_type,
                    "style": style,
                    "colors": [primary_color, secondary_color],
                    "elements": elements,
                    "complexity": complexity,
                    "sustainability": sustainability
                },
                "ai_enhanced": {
                    "refined_style": ai_style,
                    "color_palette": color_palette,
                    "cohesion_score": cohesion_score,
                    "ai_insight": ai_insight,
                    "recommendations": [
                        f"Scale dominant motifs to {60 + complexity}% for balanced presence",
                        "Use graduated color transitions instead of sharp contrasts",
                        f"Incorporate sustainable joinery for {sustainability}/10 eco-rating",
                        "Balance ornate elements with clean surfaces for visual rest"
                    ]
                }
            }
            
            # Display Results
            status_text.empty()
            progress_bar.empty()
            
            st.balloons()
            st.success("### ✅ **DESIGN REFINED SUCCESSFULLY!**")
            
            # Results Display
            results_col1, results_col2 = st.columns(2)
            
            with results_col1:
                st.markdown("#### **Your Original Design**")
                st.write(f"**Type:** {furniture_type}")
                st.write(f"**Style:** {style}")
                st.write(f"**Complexity:** {complexity}/10")
                st.write(f"**Elements:** {elements[:50]}...")
                
                # Color preview
                st.write("**Colors:**")
                color_html = f"""
                <div style="display: flex; gap: 10px; margin: 10px 0;">
                    <div style="width: 50px; height: 50px; background-color: {primary_color}; border-radius: 5px;"></div>
                    <div style="width: 50px; height: 50px; background-color: {secondary_color}; border-radius: 5px;"></div>
                </div>
                """
                st.markdown(color_html, unsafe_allow_html=True)
            
            with results_col2:
                st.markdown("#### **AI-Enhanced Design**")
                st.write(f"**Refined Style:** {ai_style}")
                st.metric("🎯 Cohesion Score", f"{cohesion_score}/100")
                st.progress(cohesion_score/100)
                
                # AI Color Palette
                st.write("**Optimized Color Palette:**")
                palette_html = "<div style='display: flex; gap: 5px; margin: 10px 0;'>"
                for color in color_palette:
                    palette_html += f"<div style='width: 40px; height: 40px; background-color: {color}; border-radius: 5px;'></div>"
                palette_html += "</div>"
                st.markdown(palette_html, unsafe_allow_html=True)
            
            # AI Insights
            st.markdown("---")
            st.markdown("#### 🧠 **AI Design Insights**")
            st.info(ai_insight)
            
            st.markdown("#### 📋 **Recommended Adjustments**")
            for i, rec in enumerate(st.session_state.design_data['ai_enhanced']['recommendations'], 1):
                st.write(f"{i}. {rec}")
            
            # 3D Preview Button
            st.markdown("---")
            if st.button("👗 **VIEW IN 3D VIRTUAL TRY-ON**", type="primary", use_container_width=True):
                st.rerun()

# ========== PAGE 5: VIRTUAL TRY-ON ==========
elif page == "👗 4. VIRTUAL TRY-ON":
    st.title("👗 Step 4: Virtual Try-On Experience")
    
    if not st.session_state.room_data or not st.session_state.design_data:
        st.warning("⚠️ Complete Steps 1-3 first to see your furniture in your room!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Go to Room Scan", use_container_width=True):
                st.rerun()
        with col2:
            if st.button("← Go to Design Studio", use_container_width=True):
                st.rerun()
    else:
        room_data = st.session_state.room_data
        design_data = st.session_state.design_data
        
        st.markdown("### 🏠 **Your Room + Your Design**")
        
        # Room and Design Summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Room Size", f"{room_data['dimensions']['width']}×{room_data['dimensions']['length']} ft")
        with col2:
            st.metric("Furniture", design_data['original']['furniture_type'])
        with col3:
            st.metric("Style", design_data['ai_enhanced']['refined_style'].split()[0])
        
        # 3D Visualization with Altair
        st.markdown("### 📐 **3D Room Visualization**")
        
        # Create interactive 3D-like visualization
        np.random.seed(42)
        n_points = 200
        
        # Room points
        room_points = pd.DataFrame({
            'x': np.concatenate([
                np.random.uniform(0, room_data['dimensions']['width'], n_points//2),
                np.random.uniform(2, 6, n_points//4),  # Furniture area
                np.random.uniform(room_data['dimensions']['width']-2, room_data['dimensions']['width'], n_points//4)  # Walking space
            ]),
            'y': np.concatenate([
                np.random.uniform(0, room_data['dimensions']['length'], n_points//2),
                np.random.uniform(2, 5, n_points//4),  # Furniture area
                np.random.uniform(0, room_data['dimensions']['length'], n_points//4)  # Walking space
            ]),
            'type': ['Room']*(n_points//2) + ['Furniture']*(n_points//4) + ['Walking Space']*(n_points//4),
            'size': [20]*(n_points//2) + [40]*(n_points//4) + [30]*(n_points//4)
        })
        
        # Create scatter plot
        selection = alt.selection_point(fields=['type'], bind='legend')
        
        chart = alt.Chart(room_points).mark_circle().encode(
            x=alt.X('x:Q', scale=alt.Scale(domain=[0, room_data['dimensions']['width']]), title='Width (ft)'),
            y=alt.Y('y:Q', scale=alt.Scale(domain=[0, room_data['dimensions']['length']]), title='Length (ft)'),
            color=alt.Color('type:N', 
                          scale=alt.Scale(
                              domain=['Room', 'Furniture', 'Walking Space'],
                              range=['#E0E0E0', design_data['ai_enhanced']['color_palette'][0], '#87CEEB']
                          )),
            size=alt.Size('size:Q', legend=None),
            opacity=alt.condition(selection, alt.value(0.8), alt.value(0.1)),
            tooltip=['type:N', 'x:Q', 'y:Q']
        ).properties(
            width=800,
            height=500,
            title=f"Room Layout: {room_data['dimensions']['width']}ft × {room_data['dimensions']['length']}ft"
        ).add_params(selection).interactive()
        
        st.altair_chart(chart, use_container_width=True)
        
        # Fit Analysis
        st.markdown("### 📊 **Fit & Comfort Analysis**")
        
        # Calculate fit metrics
        room_area = room_data['dimensions']['width'] * room_data['dimensions']['length']
        
        # Approximate furniture area based on type
        furniture_sizes = {
            "Sofa": 8 * 3.5,
            "Dining Table": 6 * 3.5,
            "Bed Frame": 7 * 6,
            "Bookshelf": 3 * 1.5,
            "Coffee Table": 4 * 2,
            "Cabinet": 5 * 2,
            "Console Table": 5 * 1.5
        }
        
        furniture_type = design_data['original']['furniture_type']
        furniture_area = furniture_sizes.get(furniture_type, 20)
        
        space_ratio = furniture_area / room_area
        walking_space = room_data['walking_space']
        
        # Calculate fit score
        fit_score = 100
        if space_ratio > 0.25:
            fit_score -= 20
        elif space_ratio < 0.15:
            fit_score -= 10
        
        if walking_space < 4:
            fit_score -= 15
        elif walking_space > 6:
            fit_score += 5
        
        if room_data['climate']['humidity'] > 75 and st.session_state.wood_recommendation['wood'] == '**Premium Teak**':
            fit_score += 10
        
        fit_score = max(60, min(99, fit_score))
        
        # Display metrics
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        with metric_col1:
            st.metric("🎯 Fit Score", f"{fit_score}/100")
            st.progress(fit_score/100)
        with metric_col2:
            space_status = "Optimal" if space_ratio < 0.2 else "High" if space_ratio < 0.25 else "Very High"
            st.metric("Space Used", f"{space_ratio*100:.1f}%", space_status)
        with metric_col3:
            walk_status = "Adequate" if walking_space >= 4 else "Limited"
            st.metric("Walking Space", f"{walking_space} ft", walk_status)
        with metric_col4:
            climate_match = 100 - abs(room_data['climate']['humidity'] - 65)
            st.metric("Climate Match", f"{climate_match}%")
        
        # Recommendations
        st.markdown("#### 💡 **Room Optimization Suggestions**")
        
        if space_ratio > 0.25:
            st.warning("""
            ⚠️ **Furniture may dominate the room**  
            Consider:  
            • Choosing a smaller size variant  
            • Opting for multi-functional furniture  
            • Using lighter color palette to create openness
            """)
        elif space_ratio < 0.15:
            st.info("""
            💡 **Room can accommodate more**  
            Consider:  
            • Adding complementary pieces (side tables, ottomans)  
            • Larger statement furniture  
            • Creating multiple seating zones
            """)
        else:
            st.success("""
            ✅ **Perfect furniture-room balance**  
            • Optimal space utilization  
            • Good walking clearance  
            • Comfortable proportions
            """)
        
        if walking_space < 4:
            st.warning("""
            ⚠️ **Walking space is limited**  
            Minimum recommended: 4 ft  
            Consider:  
            • Repositioning furniture  
            • Slimmer furniture profile  
            • Traffic flow optimization
            """)
        
        # AR Preview Note
        st.markdown("---")
        st.markdown("#### 📱 **AR Experience Preview**")
        
        ar_col1, ar_col2 = st.columns([3, 2])
        with ar_col1:
            st.markdown("""
            **In the mobile app with AR:**  
            1. **Point camera** at your room  
            2. **Furniture appears** at exact scale in AR  
            3. **Walk around it** virtually  
            4. **Adjust position** with drag & drop  
            5. **Change materials** in real-time  
            6. **Test different** lighting conditions  
            
            **Features:**  
            • LiDAR scanning for millimeter accuracy  
            • Real-time shadow rendering  
            • Material texture simulation  
            • Multiple viewing angles  
            • Save and share configurations
            """)
        
        with ar_col2:
            st.image("https://images.unsplash.com/photo-1556228453-efd6c1ff04f6",
                    caption="AR Furniture Preview in Action",
                    use_container_width=True)
        
        # Continue to Quote
        st.markdown("---")
        if st.button("💰 **GET QUOTE & PROCEED TO ORDER**", type="primary", use_container_width=True):
            st.success("✅ Perfect fit confirmed! Ready for purchase.")
            st.rerun()

# ========== PAGE 6: QUOTE & ORDER ==========
elif page == "💰 5. QUOTE & ORDER":
    st.title("💰 Step 5: Transparent Pricing & Order")
    
    if not all([st.session_state.room_data, st.session_state.wood_recommendation, st.session_state.design_data]):
        st.error("❌ Complete all previous steps to get your quote")
        st.info("Required: Room Scan + Material Selection + Design")
        if st.button("← Start from Beginning", type="primary"):
            st.session_state.room_data = None
            st.session_state.wood_recommendation = None
            st.session_state.design_data = None
            st.rerun()
    else:
        # Calculate dynamic pricing
        base_prices = {
            "Sofa": 1200,
            "Dining Table": 1500,
            "Bed Frame": 1800,
            "Bookshelf": 600,
            "Coffee Table": 800,
            "Cabinet": 1000,
            "Console Table": 700
        }
        
        furniture_type = st.session_state.design_data['original']['furniture_type']
        base_price = base_prices.get(furniture_type, 1200)
        
        # Material multiplier
        wood_type = st.session_state.wood_recommendation['wood']
        if "Premium Teak" in wood_type:
            material_multiplier = 1.4
        elif "Walnut-Oak" in wood_type:
            material_multiplier = 1.6
        elif "Teak-Mango" in wood_type:
            material_multiplier = 1.2
        else:  # Mango
            material_multiplier = 1.0
        
        # Complexity multiplier
        complexity = st.session_state.design_data['original']['complexity']
        complexity_multiplier = 1 + (complexity - 5) * 0.05
        
        # Sustainability discount
        sustainability = st.session_state.design_data['original']['sustainability']
        sustainability_discount = (sustainability - 5) * 0.02
        
        # Calculate final price
        material_cost = base_price * material_multiplier
        design_cost = material_cost * complexity_multiplier
        final_price = design_cost * (1 - sustainability_discount)
        
        # Round to nearest 50
        final_price = round(final_price / 50) * 50
        
        st.markdown("### 🛒 **Your Custom Furniture Package**")
        
        order_col1, order_col2 = st.columns([2, 1])
        
        with order_col1:
            # Order Details Card
            with st.container(border=True):
                st.markdown("#### 📋 **Order Summary**")
                
                # Itemized list
                st.markdown("**Items Included:**")
                st.markdown(f"""
                1. **{furniture_type}** - Custom Design  
                   • Style: {st.session_state.design_data['ai_enhanced']['refined_style']}  
                   • Cohesion Score: {st.session_state.design_data['ai_enhanced']['cohesion_score']}/100
                
                2. **{wood_type.replace('**', '')}** - Climate-Matched Material  
                   • Humidity Resistance: {st.session_state.wood_recommendation['properties']['Humidity Resistance']}  
                   • Durability: {st.session_state.wood_recommendation['properties']['Durability']}
                
                3. **Circular Service Package**  
                   • 5-Year Repair Warranty  
                   • Free Upcycle Service  
                   • End-of-Life Recycling
                
                4. **Digital Assets**  
                   • 3D Model & AR Files  
                   • Material Passport  
                   • Care & Maintenance Guide
                """)
                
                st.markdown("---")
                
                # Cost Breakdown
                st.markdown("#### 💰 **Cost Breakdown**")
                
                cost_data = pd.DataFrame({
                    "Component": [
                        "Base Furniture",
                        f"{wood_type.replace('**', '')} Material Premium",
                        f"Design Complexity ({complexity}/10)",
                        f"Sustainability Reward ({sustainability}/10)",
                        "Circular Service Package",
                        "Digital Assets & Files",
                        "Quality Assurance",
                        "Shipping & Installation"
                    ],
                    "Amount": [
                        f"${base_price}",
                        f"${int(material_cost - base_price)}",
                        f"${int(design_cost - material_cost)}",
                        f"-${int(design_cost * sustainability_discount)}",
                        "$150",
                        "$50",
                        "$100",
                        "FREE"
                    ]
                })
                
                st.dataframe(cost_data, use_container_width=True, hide_index=True)
                
                st.markdown("---")
                st.markdown(f"### 🎯 **Total Investment: ${int(final_price)}**")
                st.caption("All prices inclusive of taxes | Free shipping worldwide | 30-day satisfaction guarantee")
            
            # Order Button
            if not st.session_state.order_placed:
                if st.button("🚀 **CONFIRM & PLACE ORDER**", type="primary", use_container_width=True):
                    st.session_state.order_placed = True
                    st.balloons()
                    st.success("""
                    🎉 **ORDER CONFIRMED!**
                    
                    **Thank you for choosing IN SPACE.**  
                    Your custom furniture journey has begun.
                    
                    **Next Steps:**
                    1. Design proofs within **48 hours**  
                    2. Craftsmanship begins in **3-5 days**  
                    3. Estimated delivery: **3-4 weeks**  
                    4. You'll receive tracking updates
                    
                    **Order Reference:** `INSP-{random.randint(10000, 99999)}`
                    """)
            else:
                st.success("✅ **Order Already Placed!** Check your email for confirmation.")
        
        with order_col2:
            # Order Timeline
            st.markdown("#### 📅 **Production Timeline**")
            
            timeline = [
                {"phase": "Week 1", "tasks": ["Design Finalization", "Material Sourcing"], "status": "⚡"},
                {"phase": "Week 2-3", "tasks": ["Craftsmanship", "Quality Checks"], "status": "🛠️"},
                {"phase": "Week 4", "tasks": ["Finishing", "Packaging"], "status": "🎨"},
                {"phase": "Week 5", "tasks": ["Shipping", "Installation"], "status": "🚚"}
            ]
            
            for item in timeline:
                with st.container(border=True):
                    st.markdown(f"**{item['phase']}** {item['status']}")
                    for task in item['tasks']:
                        st.markdown(f"• {task}")
            
            st.markdown("---")
            
            # Guarantees
            st.markdown("#### ✅ **Our Guarantees**")
            st.markdown("""
            • **Perfect Fit Guarantee** - or we remake it  
            • **5-Year Warranty** - covers all defects  
            • **Climate Resistance** - guaranteed for your location  
            • **Circular Promise** - never goes to landfill  
            • **Design Satisfaction** - unlimited revisions
            """)
            
            st.markdown("---")
            
            # Financing Options
            st.markdown("#### 💳 **Financing Available**")
            st.markdown(f"**${int(final_price/12)}/month** for 12 months")
            if st.button("Learn About Financing", use_container_width=True):
                st.info("0% APR for qualified buyers | Instant approval")

# ========== PAGE 7: CIRCULAR SERVICE ==========
elif page == "♻️ 6. CIRCULAR SERVICE":
    st.title("♻️ Step 6: Circular Service Ecosystem")
    
    st.markdown("""
    ## ♻️ **The IN SPACE Circular Promise**
    
    Your furniture never goes to landfill. Ever.
    
    We've designed a **complete circular economy** where every piece of furniture has multiple lives.
    """)
    
    # Circular Diagram
    st.markdown("### 🔄 **The Circular Journey**")
    
    circular_data = pd.DataFrame({
        'Stage': ['Design', 'Craft', 'Use', 'Repair', 'Upcycle', 'Recycle', 'New Life'],
        'Years': [0, 0, 15, 5, 10, 0, '∞'],
        'Impact': ['Low', 'Medium', 'High', 'Low', 'Medium', 'Low', 'Restart']
    })
    
    # Create circular visualization
    base = alt.Chart(circular_data).encode(
        theta=alt.Theta("Years:Q", stack=True),
        radius=alt.Radius("Impact", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
        color=alt.Color("Stage:N", scale=alt.Scale(scheme="category20b")),
        tooltip=['Stage', 'Years', 'Impact']
    )
    
    chart = base.mark_arc(innerRadius=20, stroke="#fff")
    text = base.mark_text(radiusOffset=30).encode(text="Stage:N")
    
    st.altair_chart(chart + text, use_container_width=True)
    
    # Service Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🛠️ Repair", "🔄 Upcycle", "♻️ Recycle", "📦 Take-Back"])
    
    with tab1:
        st.markdown("### 🛠️ **Repair & Restore Service**")
        st.write("Extend your furniture's life with expert repairs.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Popular Repairs:**")
            repairs = {
                "🪚 Structural Repair": "$99-299",
                "🧵 Reupholstery": "$299-899",
                "🎨 Wood Refinishing": "$149-449",
                "🔩 Hardware Replacement": "$49-149",
                "🛋️ Cushion Rebuild": "$129-329",
                "✨ Finish Restoration": "$79-199"
            }
            
            for repair, price in repairs.items():
                st.markdown(f"- **{repair}:** {price}")
        
        with col2:
            st.markdown("**Process:**")
            st.markdown("""
            1. **Upload photos** of damage  
            2. **Instant quote** within 24 hours  
            3. **Schedule free pickup**  
            4. **7-14 day** repair time  
            5. **Delivery back** to you  
            
            ✅ **Warranty:** 2 years on all repairs
            """)
        
        # Repair Calculator
        st.markdown("---")
        st.markdown("#### 🧮 **Repair Cost Calculator**")
        
        damage_type = st.selectbox("Type of Damage", 
                                 ["Minor Scratches", "Structural Damage", "Fabric Tear", "Finish Damage", "Hardware Issue"])
        severity = st.slider("Severity (1-10)", 1, 10, 5)
        
        if st.button("Calculate Repair Cost", type="secondary"):
            base_costs = {
                "Minor Scratches": 99,
                "Structural Damage": 299,
                "Fabric Tear": 199,
                "Finish Damage": 149,
                "Hardware Issue": 79
            }
            cost = base_costs[damage_type] * (severity / 5)
            st.success(f"**Estimated Repair Cost: ${int(cost)}**")
    
    with tab2:
        st.markdown("### 🔄 **Upcycle & Transform**")
        st.write("Don't replace — transform! We give your furniture new life.")
        
        # Transformation Gallery
        st.markdown("#### 🎨 **Popular Transformations**")
        
        transformations = [
            {"From": "Old Sofa", "To": "2 Armchairs + Ottoman", "Cost": "$399", "Time": "3 weeks", "Savings": "70% vs new"},
            {"From": "Dining Table", "To": "Desk + Bookshelf", "Cost": "$299", "Time": "2 weeks", "Savings": "65% vs new"},
            {"From": "Wardrobe", "To": "Entertainment Unit + Shelves", "Cost": "$349", "Time": "2 weeks", "Savings": "60% vs new"},
            {"From": "Bed Frame", "To": "Bench + Side Tables", "Cost": "$449", "Time": "3 weeks", "Savings": "75% vs new"},
        ]
        
        for transform in transformations:
            with st.container(border=True):
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.metric("Cost", transform["Cost"])
                with col2:
                    st.markdown(f"**{transform['From']} → {transform['To']}**")
                    st.caption(f"{transform['Time']} • {transform['Savings']}")
        
        # Custom Upcycle
        st.markdown("---")
        st.markdown("#### 🎯 **Custom Upcycle Idea**")
        
        old_item = st.text_input("What furniture would you like to transform?")
        new_purpose = st.text_area("What would you like it to become?")
        
        if old_item and new_purpose:
            st.info(f"✨ **Great idea!** Turning {old_item} into {new_purpose}.")
            if st.button("Get Custom Upcycle Quote", type="primary"):
                quote = random.randint(199, 899)
                st.success(f"**Estimated Cost: ${quote}**")
                st.write("Includes: Design, materials, labor, pickup & delivery")
    
    with tab3:
        st.markdown("### ♻️ **Zero-Waste Recycling**")
        st.write("When repair or upcycle isn't possible, we ensure 100% responsible recycling.")
        
        st.markdown("#### 📊 **Our Recycling Process**")
        
        recycling_steps = [
            ("1. **Material Separation**", "Wood, metal, fabric, foam meticulously separated"),
            ("2. **Wood Processing**", "Turned into particle board or clean biomass energy"),
            ("3. **Metal Recycling**", "Melted and reformed into new products"),
            ("4. **Fabric Repurposing**", "Converted to insulation or industrial rags"),
            ("5. **Foam Recycling**", "Processed for carpet underlay or packaging"),
            ("6. **Landfill Diversion**", "100% success rate - nothing to landfill")
        ]
        
        for step, desc in recycling_steps:
            st.markdown(f"{step}")
            st.caption(desc)
        
        st.markdown("---")
        
        # Environmental Impact
        st.markdown("#### 🌍 **Environmental Impact**")
        
        impact_col1, impact_col2, impact_col3 = st.columns(3)
        with impact_col1:
            st.metric("CO₂ Saved", "85%", "vs new furniture")
        with impact_col2:
            st.metric("Landfill Reduction", "100%", "zero waste")
        with impact_col3:
            st.metric("Materials Recovered", "92%", "closed loop")
        
        st.info("✅ **Free recycling service** for all IN SPACE furniture")
    
    with tab4:
        st.markdown("### 📦 **Furniture Take-Back Program**")
        st.write("Sell your old IN SPACE furniture back to us for store credit.")
        
        st.markdown("#### 💰 **How It Works**")
        st.markdown("""
        1. **Request valuation** through the app  
        2. **We assess** age, condition, materials  
        3. **Get offer** (30-60% of original value)  
        4. **Schedule free pickup** at your convenience  
        5. **Receive store credit** instantly
        """)
        
        # Valuation Calculator
        st.markdown("---")
        st.markdown("#### 🧮 **Valuation Calculator**")
        
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Age (years)", 0, 20, 3)
            condition = st.select_slider("Condition", ["Poor", "Fair", "Good", "Excellent"])
            original_price = st.number_input("Original Price ($)", 500, 10000, 1500, step=100)
        
        with col2:
            material = st.selectbox("Primary Material", ["Teak", "Mango", "Teak-Mango", "Walnut", "Oak", "Other"])
            usage = st.select_slider("Usage Intensity", ["Light", "Medium", "Heavy"])
            location = st.selectbox("Location", ["Same City", "Same State", "Other State"])
        
        if st.button("Calculate Valuation", type="primary"):
            # Valuation logic
            base_value = original_price * 0.5
            
            # Depreciation
            age_factor = max(0.3, 1 - (age * 0.05))
            
            # Condition multipliers
            condition_map = {"Poor": 0.3, "Fair": 0.5, "Good": 0.7, "Excellent": 0.9}
            condition_factor = condition_map[condition]
            
            # Material factors
            material_map = {"Teak": 1.2, "Mango": 1.0, "Teak-Mango": 1.1, "Walnut": 1.3, "Oak": 1.2, "Other": 0.8}
            material_factor = material_map.get(material, 1.0)
            
            # Usage factor
            usage_map = {"Light": 1.1, "Medium": 1.0, "Heavy": 0.8}
            usage_factor = usage_map[usage]
            
            # Calculate final valuation
            valuation = base_value * age_factor * condition_factor * material_factor * usage_factor
            
            # Shipping adjustment
            if location == "Other State":
                valuation *= 0.9
            elif location == "Same State":
                valuation *= 0.95
            
            # Round to nearest 10
            valuation = round(valuation / 10) * 10
            
            st.success(f"**Estimated Market Value: ${int(valuation)}**")
            st.write(f"**Store Credit Offer: ${int(valuation * 0.9)}**")
            st.info(f"*Based on: {condition} condition, {age} years old, {material}*")
        
        # Impact Dashboard
        st.markdown("---")
        st.markdown("#### 📈 **Your Circular Impact**")
        
        impact_data = pd.DataFrame({
            "Metric": ["CO₂ Saved", "Trees Preserved", "Landfill Diverted", "Energy Saved"],
            "Your Impact": ["320 kg", "0.8 trees", "110 kg", "180 kWh"],
            "Community Total": ["45,600 kg", "115 trees", "15,700 kg", "25,600 kWh"]
        })
        
        st.dataframe(impact_data, use_container_width=True, hide_index=True)
        
        st.caption("*Based on life cycle analysis of average furniture piece*")

# ========== PAGE 8: INVESTOR DASHBOARD ==========
elif page == "📊 7. INVESTOR DASHBOARD":
    st.title("📊 IN SPACE FURNITURE - Investor Dashboard")
    
    # Executive Summary
    st.markdown("## 🎯 **Executive Summary**")
    
    st.markdown("""
    **IN SPACE** is building the **complete digital-physical ecosystem** for furniture, combining:
    
    1. **📱 AR/VR Technology** - Millimeter-accurate room scanning
    2. **🧠 AI/ML Intelligence** - Climate-aware material science & design refinement
    3. **♻️ Circular Economy** - End-to-end sustainable lifecycle management
    4. **📊 Data Platform** - Anonymous insights for the $800B furniture industry
    
    **We're solving:** 40% furniture returns, material failure in wrong climates, design frustration, and 12M tons/year of furniture waste.
    """)
    
    # Market Opportunity
    st.markdown("## 📈 **Market Opportunity**")
    
    market_col1, market_col2, market_col3, market_col4 = st.columns(4)
    with market_col1:
        st.metric("**Global Furniture Market**", "$800B", "")
    with market_col2:
        st.metric("**Custom Furniture Segment**", "$120B", "15% of total")
    with market_col3:
        st.metric("**Sustainable Furniture Demand**", "$90B", "11% CAGR")
    with market_col4:
        st.metric("**Online Furniture Growth**", "18%", "Annual growth")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Financials", "🛠️ Technology", "🚀 Traction", "👥 Team"])
    
    with tab1:
        st.markdown("### 💰 **Financial Projections**")
        
        # Revenue Projections
        st.markdown("#### **Revenue Streams**")
        
        revenue_data = pd.DataFrame({
            "Stream": ["Furniture Sales", "AI Design License", "Circular Subscriptions", "Data Insights", "Total"],
            "Year 1": ["$500K", "$50K", "$30K", "$20K", "$600K"],
            "Year 2": ["$3.0M", "$500K", "$300K", "$200K", "$4.0M"],
            "Year 3": ["$8.0M", "$1.2M", "$800K", "$500K", "$10.5M"],
            "Margin": ["40%", "85%", "70%", "90%", "52%"]
        })
        
        st.dataframe(revenue_data, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Funding Ask
        st.markdown("#### 💵 **Seed Round: $1.5M**")
        
        use_of_funds = pd.DataFrame({
            "Category": ["Tech Development", "Pilot Program", "Operations", "Legal & IP", "Total"],
            "Amount": ["$750K", "$450K", "$225K", "$75K", "$1.5M"],
            "Percentage": ["50%", "30%", "15%", "5%", "100%"],
            "Description": [
                "AR/AI engineers, 3D developers",
                "3 city pilots, 100 customers",
                "Team, marketing, infrastructure",
                "Patents, trademarks, compliance",
                ""
            ]
        })
        
        st.dataframe(use_of_funds, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Valuation
        st.markdown("#### 🏦 **Valuation & Exit Strategy**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("**Pre-money Valuation**", "$6.5M")
        with col2:
            st.metric("**Post-money Valuation**", "$8.0M")
        with col3:
            st.metric("**Ownership Offered**", "18.75%")
        
        st.markdown("""
        **Exit Potential (5-7 years):**
        - **Strategic Acquisition:** IKEA, Wayfair, Amazon ($500M-$1B)
        - **IPO:** Furniture tech category leader
        - **Secondary Sale:** PE firms, furniture conglomerates
        """)
    
    with tab2:
        st.markdown("### 🛠️ **Technology Stack & IP**")
        
        st.markdown("#### **Core Intellectual Property**")
        
        ip_data = pd.DataFrame({
            "Technology": [
                "AR Room Scanning Algorithm",
                "Climate-Material Database",
                "AI Design Refinement Engine",
                "Circular Logistics Platform",
                "3D Model Optimization"
            ],
            "Status": [
                "Patent Pending",
                "Proprietary Database",
                "Trade Secret",
                "Patent Filed",
                "Proprietary Algorithm"
            ],
            "Competitive Advantage": [
                "2mm accuracy vs 10mm industry standard",
                "10K+ material-climate combinations",
                "Reduces design time by 70%",
                "100% landfill diversion",
                "90% smaller file size"
            ]
        })
        
        st.dataframe(ip_data, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.markdown("#### **Development Roadmap**")
        
        roadmap = [
            {"Phase": "Q2 2024", "Focus": "Seed Round & MVP", "Deliverables": ["This demo", "3 pilot workshops", "Waitlist: 500+"]},
            {"Phase": "Q3-Q4 2024", "Focus": "Native App Development", "Deliverables": ["React Native app", "ARKit/ARCore integration", "First 100 customers"]},
            {"Phase": "2025", "Focus": "Scale & Expansion", "Deliverables": ["5 cities", "10K customers", "Series A ($5M)"]},
            {"Phase": "2026", "Focus": "Market Leadership", "Deliverables": ["International expansion", "50K customers", "Profitability"]}
        ]
        
        for phase in roadmap:
            with st.container(border=True):
                st.markdown(f"**{phase['Phase']} - {phase['Focus']}**")
                for deliverable in phase['Deliverables']:
                    st.markdown(f"• {deliverable}")
    
    with tab3:
        st.markdown("### 🚀 **Traction & Metrics**")
        
        # Current Traction
        st.markdown("#### **Current Metrics**")
        
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
        with metric_col1:
            st.metric("Waitlist", "500+", "")
        with metric_col2:
            st.metric("Pilot Workshops", "3", "Confirmed")
        with metric_col3:
            st.metric("Designs Created", "50+", "In testing")
        with metric_col4:
            st.metric("NPS Score", "72", "Excellent")
        
        st.markdown("---")
        
        # Key Performance Indicators
        st.markdown("#### **Key Performance Indicators**")
        
        kpi_data = pd.DataFrame({
            "KPI": [
                "Customer Acquisition Cost",
                "Lifetime Value",
                "Return Rate Reduction",
                "Design Time Reduction",
                "Customer Satisfaction",
                "Circular Adoption"
            ],
            "Current": ["$150", "$2,400", "47%", "70%", "4.8/5.0", "85%"],
            "Industry Avg.": ["$300", "$800", "40%", "0%", "3.2/5.0", "15%"],
            "Advantage": ["50% lower", "3x higher", "7% better", "70% better", "50% higher", "70% better"]
        })
        
        st.dataframe(kpi_data, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Partnerships
        st.markdown("#### **Strategic Partnerships**")
        
        st.markdown("""
        **Confirmed:**
        • **3 Artisan Workshops** - Mumbai, Bangalore, Delhi  
        • **Wood Suppliers** - FSC-certified plantations  
        • **Logistics Partners** - Green shipping options  
        
        **In Discussion:**
        • **Home Decor Brands** - Cross-promotion  
        • **Real Estate Developers** - Pre-furnished homes  
        • **Sustainability Certifiers** - Carbon credits
        """)
    
    with tab4:
        st.markdown("### 👥 **Team & Advisors**")
        
        st.markdown("#### **Founding Team**")
        
        team_col1, team_col2 = st.columns(2)
        
        with team_col1:
            st.markdown("""
            **👨‍💻 [Your Name] - Founder & CEO**  
            *Background:* Furniture design + tech entrepreneurship  
            *Experience:* 10+ years in furniture industry, 2 successful startups  
            *Role:* Vision, fundraising, partnerships, product strategy
            
            **👩‍💻 [To Hire] - CTO**  
            *Background:* AR/VR + AI/ML expertise  
            *Experience:* 8+ years at tech companies  
            *Role:* Tech architecture, team building, product development
            """)
        
        with team_col2:
            st.markdown("""
            **👨‍🏭 [To Hire] - Head of Production**  
            *Background:* Furniture manufacturing & supply chain  
            *Experience:* 15+ years with major furniture brands  
            *Role:* Workshop partnerships, quality control, logistics
            
            **👩‍🎨 [To Hire] - Head of Design**  
            *Background:* Industrial design + UX  
            *Experience:* 10+ years design leadership  
            *Role:* Design systems, user experience, AI training
            """)
        
        st.markdown("---")
        
        st.markdown("#### **Advisory Board**")
        
        st.markdown("""
        **🏢 Industry Veterans:**  
        • **Former IKEA Executive** - 20+ years furniture retail  
        • **Sustainable Materials Expert** - PhD in Wood Science  
        • **Tech Investor** - 3 successful AR/VR exits  
        
        **🎯 Key Roles:**  
        • Market strategy & expansion  
        • Technical validation  
        • Fundraising guidance  
        • Industry connections
        """)
        
        st.markdown("---")
        
        st.markdown("#### **Hiring Plan**")
        
        hiring = pd.DataFrame({
            "Timeline": ["Immediate (Seed)", "6 Months", "12 Months", "24 Months"],
            "Roles": [
                "CTO, AR Engineer, AI/ML Specialist",
                "Product Manager, Design Lead, Operations",
                "Marketing, Sales, Customer Success",
                "International expansion team"
            ],
            "Team Size": ["5", "12", "25", "50+"]
        })
        
        st.dataframe(hiring, use_container_width=True, hide_index=True)
    
    # Call to Action
    st.markdown("---")
    st.markdown("## 🤝 **Investment Opportunity**")
    
    cta_col1, cta_col2 = st.columns([3, 1])
    
    with cta_col1:
        st.markdown("""
        **Why Invest Now?**
        
        1. **First-mover advantage** in furniture tech  
        2. **Proven demand** - 40% industry returns problem  
        3. **Scalable model** - Asset-light, high-margin  
        4. **Sustainable focus** - Aligns with ESG trends  
        5. **Strong IP position** - Multiple moats  
        
        **Next Steps:**
        • Review detailed pitch deck  
        • Schedule executive briefing  
        • Meet the team  
        • Participate in seed round
        """)
    
    with cta_col2:
        st.markdown("#### **Contact**")
        st.markdown("""
        📧 **Email:** hello@inspace.furniture  
        🔗 **LinkedIn:** [Your Profile]  
        🎥 **Demo:** [Live Streamlit App]  
        📄 **Deck:** [Available on request]
        
        **Seed Round Closes:** June 30, 2024
        """)

# ========== FOOTER ==========
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([2, 1, 1])

with footer_col1:
    st.caption("🪑 **IN SPACE FURNITURE** © 2024 | Complete Ecosystem | Streamlit Cloud")

with footer_col2:
    st.caption("✅ **All Features Active**")

with footer_col3:
    st.caption("🚀 **Live Investor Demo**")

# Add confetti on order placement
if st.session_state.order_placed and page == "💰 5. QUOTE & ORDER":
    st.balloons()
