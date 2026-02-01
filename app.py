# app.py - COMPLETE IN SPACE FURNITURE - ALL FEATURES
import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# TRY to import Plotly, with fallback
PLOTLY_AVAILABLE = False
try:
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    st.sidebar.warning("⚠️ Plotly 3D features loading...")

# TRY to import Pillow, with fallback
PILLOW_AVAILABLE = False
try:
    from PIL import Image
    PILLOW_AVAILABLE = True
except ImportError:
    pass

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
        font-size: 2.8rem;
        color: #2A5C3D;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.3rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-left: 6px solid #2A5C3D;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        border: 2px solid #2A5C3D;
        text-align: center;
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

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("## 🪑 IN SPACE")
    st.markdown("---")
    
    page = st.radio(
        "**NAVIGATE:**",
        [
            "🏠 **HOME** - Vision",
            "📱 **1. AR ROOM SCAN**", 
            "🌳 **2. MATERIAL ADVISOR**",
            "🎨 **3. AI DESIGN STUDIO**",
            "👗 **4. VIRTUAL TRY-ON**",
            "💰 **5. QUOTE & ORDER**",
            "♻️ **6. CIRCULAR SERVICE**",
            "📊 **7. INVESTOR DASHBOARD**"
        ]
    )
    
    st.markdown("---")
    
    # Status indicators
    if st.session_state.room_data:
        st.success("✅ Room Scanned")
    if st.session_state.wood_recommendation:
        st.success("✅ Material Selected")
    if st.session_state.design_data:
        st.success("✅ Design Created")
    
    st.markdown("---")
    st.caption("**Deployment Status:** Building...")
    if not PLOTLY_AVAILABLE:
        st.warning("3D features loading...")

# ========== PAGE 1: HOME ==========
if page == "🏠 **HOME** - Vision":
    st.markdown('<div class="main-header">IN SPACE FURNITURE</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">From Room Scan to Circular Design — Furniture That Fits Your Space, Style, and Planet</div>', unsafe_allow_html=True)
    
    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### 🚀 **The Future of Furniture is Here**")
        st.write("""
        We're building the **complete ecosystem** where furniture meets technology:
        
        1. **📱 AR Room Scanning** - Millimeter-accurate measurements
        2. **🌳 Climate-Aware Materials** - AI recommends perfect wood
        3. **🎨 AI Design Refinement** - Professional results from your ideas
        4. **👗 Virtual Try-On** - See it in your space before buying
        5. **♻️ Circular Service** - Repair, upcycle, recycle forever
        """)
        
        st.markdown("---")
        
        # Quick Stats
        st.markdown("### 📊 **By The Numbers**")
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
        with stat_col1:
            st.markdown('<div class="metric-card"><h3>47%</h3><p>Fewer Returns</p></div>', unsafe_allow_html=True)
        with stat_col2:
            st.markdown('<div class="metric-card"><h3>3.2x</h3><p>Longer Lifespan</p></div>', unsafe_allow_html=True)
        with stat_col3:
            st.markdown('<div class="metric-card"><h3>85%</h3><p>Waste Reduced</p></div>', unsafe_allow_html=True)
        with stat_col4:
            st.markdown('<div class="metric-card"><h3>$800B</h3><p>Market Size</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎯 **Quick Demo**")
        
        # Interactive demo
        with st.container(border=True):
            st.write("**Try AR Scanning:**")
            if st.button("📏 Scan Mock Room", use_container_width=True):
                with st.spinner("Scanning..."):
                    time.sleep(1)
                    st.session_state.room_data = {
                        "width": 15,
                        "length": 12,
                        "humidity": 78
                    }
                    st.success("✅ Room scanned: 15×12 ft, 78% humidity")
            
            st.write("**Try AI Design:**")
            user_idea = st.text_input("Your idea", "Lion + peacock sofa")
            if st.button("✨ AI Refine", use_container_width=True):
                st.success(f"**AI Enhanced:** 'Regal fusion with balanced motifs'")
        
        st.markdown("---")
        st.info("**🎯 Investor Ready:** Complete demo deployed on Streamlit Cloud")

# ========== PAGE 2: AR ROOM SCAN ==========
elif page == "📱 **1. AR ROOM SCAN**":
    st.title("Step 1: AR Room Scanning")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### 📱 **How It Works**")
        st.write("""
        1. **Point your phone** around the room
        2. **AI scans** dimensions, sunlight, humidity zones
        3. **Get precise measurements** (±2mm accuracy)
        4. **Climate analysis** for material recommendations
        """)
        
        st.markdown("---")
        
        # Mock scanner
        st.markdown("### 🏠 **Room Scanner**")
        scan_type = st.radio("Scan method:", ["Upload Photo", "Live Camera", "Use Mock Data"])
        
        if scan_type == "Upload Photo" and PILLOW_AVAILABLE:
            uploaded = st.file_uploader("Upload room photo", type=['jpg', 'png'])
            if uploaded:
                st.image(uploaded, caption="Your Room")
        
        if st.button("🚀 Start AR Scan", type="primary", use_container_width=True):
            with st.spinner("🔄 Scanning room with AR..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                    time.sleep(0.02)
                
                # Generate scan data
                humidity = random.randint(65, 85)
                scan_data = {
                    "dimensions": {
                        "width": random.randint(12, 18),
                        "length": random.randint(10, 16),
                        "height": random.randint(8, 12)
                    },
                    "climate": {
                        "humidity": humidity,
                        "temperature": random.randint(25, 35),
                        "sunlight_hours": random.randint(4, 8),
                        "location": random.choice(["Chennai", "Mumbai", "Goa", "Bangalore"])
                    },
                    "walking_space": random.randint(4, 7),
                    "scan_quality": f"{random.randint(97, 99)}% accurate"
                }
                
                st.session_state.room_data = scan_data
                st.success(f"✅ Scan complete! **{humidity}% humidity** detected")
    
    with col2:
        st.markdown("### 📊 **Scan Results**")
        
        if st.session_state.room_data:
            data = st.session_state.room_data
            
            st.metric("Room Width", f"{data['dimensions']['width']} ft", "±2mm")
            st.metric("Room Length", f"{data['dimensions']['length']} ft", "±2mm")
            st.metric("Humidity", f"{data['climate']['humidity']}%")
            st.metric("Temperature", f"{data['climate']['temperature']}°C")
            
            st.progress(data['climate']['humidity']/100, 
                       text=f"Humidity Level: {data['climate']['humidity']}%")
            
            st.info(f"**Location:** {data['climate']['location']}")
            st.info(f"**Walking Space:** {data['walking_space']} ft clearance")
        else:
            st.info("👆 **Scan a room to see results here**")

# ========== PAGE 3: MATERIAL ADVISOR ==========
elif page == "🌳 **2. MATERIAL ADVISOR**":
    st.title("Step 2: Climate-Aware Material Selection")
    
    if not st.session_state.room_data:
        st.warning("⚠️ Please scan your room first!")
        if st.button("Go to Room Scanner"):
            st.rerun()
    else:
        climate_data = st.session_state.room_data['climate']
        humidity = climate_data['humidity']
        
        st.markdown(f"### 🌡️ **Your Climate: {humidity}% humidity in {climate_data['location']}**")
        
        # Wood recommendation logic
        if humidity > 75:
            wood = "Teak"
            reason = "**Perfect for high humidity** - Naturally water-resistant, prevents warping"
            icon = "🪵"
            durability = "95/100"
        elif humidity > 60:
            wood = "Teak/Mango Blend"
            reason = "**Optimal balance** - Teak's durability + Mango's sustainability"
            icon = "🌳"
            durability = "88/100"
        elif humidity > 45:
            wood = "Mango Wood"
            reason = "**Sustainable choice** - Fast-growing, beautiful grain for moderate climates"
            icon = "🪴"
            durability = "82/100"
        else:
            wood = "Walnut/Oak"
            reason = "**Luxury & stability** - Rich appearance, ideal for dry conditions"
            icon = "🌲"
            durability = "90/100"
        
        # Display recommendation
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"# {icon}")
            st.markdown(f"## {wood}")
            st.metric("Durability", durability)
            st.metric("Climate Match", f"{100 - abs(humidity - 70)}%")
        
        with col2:
            st.markdown("### 🎯 **AI Recommendation**")
            st.success(reason)
            
            # Detailed analysis
            with st.expander("📊 **Material Analysis**"):
                woods_df = pd.DataFrame({
                    "Wood": ["Teak", "Mango", "Teak/Mango", "Walnut"],
                    "Humidity Resist": ["95%", "70%", "85%", "80%"],
                    "Lifespan": ["50+ years", "25+ years", "35+ years", "40+ years"],
                    "Sustainability": ["High", "Very High", "High", "Medium"],
                    "Cost/ft³": ["$85", "$45", "$65", "$120"]
                })
                st.dataframe(woods_df, use_container_width=True, hide_index=True)
        
        st.session_state.wood_recommendation = {
            "wood": wood,
            "reason": reason,
            "durability": durability,
            "humidity_match": humidity
        }
        
        st.markdown("---")
        if st.button("✅ Select This Material & Continue", type="primary", use_container_width=True):
            st.success(f"Selected: **{wood}** for your {humidity}% humidity climate")
            st.rerun()

# ========== PAGE 4: AI DESIGN STUDIO ==========
elif page == "🎨 **3. AI DESIGN STUDIO**":
    st.title("Step 3: AI-Powered Design Studio")
    
    st.markdown("### 🦁 **Example: Lion + Peacock Fusion**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Your Design Input**")
        st.image("https://i.imgur.com/placeholder-lion-peacock.png", 
                caption="Lion + Peacock Design Idea", width=300)
        st.write("**Elements:** Lion strength + Peacock elegance")
        st.write("**Challenge:** Mismatched styles, unbalanced proportions")
    
    with col2:
        st.markdown("#### **AI-Enhanced Design**")
        st.image("https://i.imgur.com/placeholder-refined.png", 
                caption="AI-Refined: Regal Fusion", width=300)
        st.write("**AI Transformation:**")
        st.write("✅ Balanced lion motifs (60% scale)")
        st.write("✅ Peacock colors as accent stitching")
        st.write("✅ Geometric harmony added")
    
    st.markdown("---")
    
    # Interactive design studio
    st.markdown("### 🎨 **Design Your Furniture**")
    
    design_col1, design_col2 = st.columns(2)
    
    with design_col1:
        style = st.selectbox("Style", ["Modern", "Traditional", "Bohemian", "Industrial", "Fusion"])
        primary_color = st.color_picker("Primary Color", "#2A5C3D")
        furniture_type = st.selectbox("Furniture Type", 
                                     ["Sofa", "Dining Table", "Bed", "Bookshelf", "Cabinet"])
    
    with design_col2:
        elements = st.text_area("Special Elements", 
                               "e.g., lion motifs, peacock feathers, geometric patterns")
        complexity = st.slider("Design Complexity", 1, 10, 7)
    
    if st.button("✨ AI Design Refinement", type="primary", use_container_width=True):
        with st.spinner("AI is refining your design..."):
            time.sleep(2)
            
            # Generate AI enhancements
            ai_style = f"{style} with {random.choice(['contemporary', 'global', 'organic'])} influences"
            cohesion_score = random.randint(85, 98)
            
            st.session_state.design_data = {
                "original": {"style": style, "elements": elements},
                "ai_enhanced": {
                    "style": ai_style,
                    "cohesion_score": cohesion_score,
                    "recommendations": [
                        "Scale motifs to 60% for subtlety",
                        "Use complementary color palette",
                        "Balance asymmetric elements"
                    ]
                }
            }
            
            st.success("✅ Design Refined!")
            st.metric("Cohesion Score", f"{cohesion_score}/100")
            st.progress(cohesion_score/100)

# ========== PAGE 5: VIRTUAL TRY-ON ==========
elif page == "👗 **4. VIRTUAL TRY-ON**":
    st.title("Step 4: Virtual Try-On Experience")
    
    if PLOTLY_AVAILABLE and st.session_state.room_data:
        try:
            # Create 3D room visualization
            room_data = st.session_state.room_data
            width = room_data['dimensions']['width']
            length = room_data['dimensions']['length']
            
            fig = go.Figure()
            
            # Room
            fig.add_trace(go.Mesh3d(
                x=[0, width, width, 0],
                y=[0, 0, length, length],
                z=[0, 0, 0, 0],
                opacity=0.1,
                color='lightgray',
                name='Room'
            ))
            
            # Furniture
            fig.add_trace(go.Mesh3d(
                x=[2, 6, 6, 2, 2, 6, 6, 2],
                y=[2, 2, 5, 5, 2, 2, 5, 5],
                z=[0, 0, 0, 0, 2, 2, 2, 2],
                i=[7, 0, 0, 0, 4, 4, 6, 6],
                j=[3, 4, 1, 2, 5, 6, 5, 2],
                k=[0, 7, 2, 3, 6, 7, 1, 1],
                color='#2A5C3D',
                opacity=0.8,
                name='Your Furniture'
            ))
            
            fig.update_layout(
                title="3D Room Preview with Your Furniture",
                scene=dict(
                    xaxis_title="Width (ft)",
                    yaxis_title="Length (ft)", 
                    zaxis_title="Height (ft)",
                    aspectratio=dict(x=1, y=length/width, z=0.3)
                ),
                height=600
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.warning(f"3D rendering loading: {str(e)}")
            st.info("**3D Preview:** Furniture placed with optimal walking space")
    else:
        st.info("**3D Virtual Try-On**")
        st.write("In the mobile app: Point camera, see furniture in AR")
        
        # Mock visualization
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Fit Score", "95%")
            st.progress(0.95)
        with col2:
            st.metric("Walking Space", "5.2 ft")
        with col3:
            st.metric("Room Utilization", "68%", "Optimal")
    
    st.markdown("---")
    st.success("✅ **Perfect Fit!** Ready to order with confidence")

# ========== PAGE 6: QUOTE & ORDER ==========
elif page == "💰 **5. QUOTE & ORDER**":
    st.title("Step 5: Quote & Order")
    
    # Calculate quote
    base_price = 1200
    if st.session_state.get('wood_recommendation'):
        wood = st.session_state.wood_recommendation['wood']
        if 'Teak' in wood:
            base_price = 1400
        elif 'Walnut' in wood:
            base_price = 1800
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🛒 **Order Summary**")
        
        # Order details
        with st.container(border=True):
            st.write("**Custom Furniture Package:**")
            if st.session_state.design_data:
                st.write(f"- Design: {st.session_state.design_data['ai_enhanced']['style']}")
            if st.session_state.wood_recommendation:
                st.write(f"- Material: {st.session_state.wood_recommendation['wood']}")
                st.write(f"- Durability: {st.session_state.wood_recommendation['durability']}")
            
            st.markdown("---")
            
            st.write("**Cost Breakdown:**")
            st.write(f"- Materials: ${int(base_price * 0.5)}")
            st.write(f"- Craftsmanship: ${int(base_price * 0.35)}")
            st.write(f"- Sustainable Finish: ${int(base_price * 0.1)}")
            st.write(f"- Circular Service Fee: ${int(base_price * 0.05)}")
            
            st.markdown("---")
            st.markdown(f"## **Total: ${base_price}**")
            st.caption("All-inclusive | Free shipping | 5-year warranty")
        
        # Order button
        if st.button("🚀 **PLACE ORDER**", type="primary", use_container_width=True):
            st.balloons()
            st.success("🎉 **Order Confirmed!**")
            st.info("Expected delivery: 3-4 weeks. You'll receive design proofs in 48 hours.")
    
    with col2:
        st.markdown("### 📅 **Order Timeline**")
        
        timeline = [
            {"day": "Day 1-2", "task": "Design Finalization", "status": "✅"},
            {"day": "Day 3-7", "task": "Material Sourcing", "status": "⏳"},
            {"day": "Day 8-21", "task": "Craftsmanship", "status": "📅"},
            {"day": "Day 22-23", "task": "Quality Check", "status": "📅"},
            {"day": "Day 24-28", "task": "Delivery", "status": "📅"}
        ]
        
        for item in timeline:
            st.write(f"**{item['day']}** - {item['task']}")
            st.caption(f"Status: {item['status']}")

# ========== PAGE 7: CIRCULAR SERVICE ==========
elif page == "♻️ **6. CIRCULAR SERVICE**":
    st.title("Step 6: Circular Service Program")
    
    st.info("♻️ **Our Promise:** Your furniture never goes to landfill. Ever.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🛠️ Repair", "🔄 Upcycle", "♻️ Recycle", "📦 Take-Back"])
    
    with tab1:
        st.markdown("### 🛠️ **Repair & Restore**")
        st.write("Extend your furniture's life with expert repairs.")
        st.write("**Popular repairs:**")
        st.write("- Structural repairs: $99-199")
        st.write("- Reupholstery: $299-599")
        st.write("- Wood refinishing: $149-349")
        
        if st.button("Get Repair Quote", key="repair"):
            st.success("**Estimated: $199** (includes pickup & delivery)")
    
    with tab2:
        st.markdown("### 🔄 **Upcycle & Transform**")
        st.write("Turn old furniture into something new.")
        st.write("**Example:** Old sofa → 2 chairs + coffee table")
        st.write("**Cost:** $299 | **Time:** 2-3 weeks")
        
        old_item = st.text_input("What do you want to upcycle?")
        if old_item:
            st.success(f"We can transform your {old_item}!")
    
    with tab3:
        st.markdown("### ♻️ **Responsible Recycling**")
        st.write("100% material recovery when repair isn't possible.")
        st.metric("Landfill Reduction", "100%")
        st.metric("Materials Recovered", "92%")
        st.info("✅ **Free** for all IN SPACE furniture")
    
    with tab4:
        st.markdown("### 📦 **Take-Back Program**")
        st.write("Sell back your furniture for store credit.")
        
        age = st.slider("Age (years)", 0, 10, 2)
        condition = st.select_slider("Condition", ["Poor", "Fair", "Good", "Excellent"])
        
        if st.button("Calculate Value"):
            value = 1200 * (1 - age*0.1) * {"Poor":0.3, "Fair":0.5, "Good":0.7, "Excellent":0.9}[condition]
            st.success(f"**Estimated value: ${int(value)}**")
            st.write(f"Store credit: **${int(value*0.9)}**")

# ========== PAGE 8: INVESTOR DASHBOARD ==========
elif page == "📊 **7. INVESTOR DASHBOARD**":
    st.title("IN SPACE FURNITURE - Investor Dashboard")
    
    # Executive Summary
    st.markdown("## 🎯 **Executive Summary**")
    st.write("""
    IN SPACE is building the complete furniture ecosystem combining **AR room scanning**, 
    **climate-aware AI recommendations**, **design refinement**, and **circular economy services**.
    We're solving the $800B furniture industry's core problems: poor fit, material failure, 
    design frustration, and environmental waste.
    """)
    
    # Key Metrics
    st.markdown("## 📈 **Key Metrics**")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Market Size", "$800B", "Global furniture")
    with col2:
        st.metric("Target Segment", "$120B", "Custom furniture")
    with col3:
        st.metric("Seed Ask", "$1.5M")
    with col4:
        st.metric("Valuation", "$8M", "Post-money")
    
    # Business Model
    st.markdown("## 💰 **Business Model**")
    
    revenue_data = pd.DataFrame({
        "Revenue Stream": ["Furniture Sales", "AI Design License", "Circular Subscriptions", "Data Insights"],
        "Margin": ["40%", "85%", "70%", "90%"],
        "Year 1": ["$500K", "$50K", "$30K", "$20K"],
        "Year 2": ["$3M", "$500K", "$300K", "$200K"],
        "Year 3": ["$8M", "$1.2M", "$800K", "$500K"]
    })
    
    st.dataframe(revenue_data, use_container_width=True, hide_index=True)
    
    # Technology Stack
    st.markdown("## 🛠️ **Technology Stack**")
    
    tech_col1, tech_col2 = st.columns(2)
    with tech_col1:
        st.write("**Core IP:**")
        st.write("- Proprietary AR scanning algorithm")
        st.write("- Climate-material database (wood science)")
        st.write("- AI design refinement models")
        st.write("- Circular logistics platform")
    
    with tech_col2:
        st.write("**Development:**")
        st.write("- **MVP:** This Streamlit demo")
        st.write("- **Phase 2:** React Native + ARKit/ARCore")
        st.write("- **Phase 3:** Custom AI/ML stack")
        st.write("- **Scale:** Cloud-native microservices")
    
    # Funding Use
    st.markdown("## 💵 **Use of Funds**")
    
    use_data = pd.DataFrame({
        "Area": ["Tech Development", "Pilot Program", "Operations", "Legal & IP"],
        "Amount": ["$750K", "$450K", "$225K", "$75K"],
        "Percentage": ["50%", "30%", "15%", "5%"]
    })
    
    st.dataframe(use_data, use_container_width=True, hide_index=True)
    
    # Team
    st.markdown("## 👥 **Team**")
    st.write("- **Founder:** [Your Name] - Furniture design + tech vision")
    st.write("- **Seeking:** CTO with AR/AI experience")
    st.write("- **Advisors:** Furniture industry veterans (2 confirmed)")
    
    # Roadmap
    st.markdown("## 🚀 **Roadmap**")
    
    roadmap_df = pd.DataFrame({
        "Timeline": ["Q2 2024", "Q3 2024", "Q4 2024", "Q1 2025", "2025+"],
        "Milestone": [
            "Seed Round ($1.5M)", 
            "Native AR app launch", 
            "Pilot: 100 customers",
            "Series A ($5M)", 
            "Expand to 5 cities"
        ],
        "Status": ["🔄 In Progress", "📅 Planned", "📅 Planned", "🎯 Future", "🎯 Future"]
    })
    
    st.dataframe(roadmap_df, use_container_width=True, hide_index=True)
    
    # Call to Action
    st.markdown("---")
    st.markdown("## 🤝 **Ready to Transform Furniture?**")
    st.write("**Contact:** hello@inspace.furniture")
    st.write("**Demo:** [Live Streamlit App](https://your-app.streamlit.app)")
    st.write("**GitHub:** [View Code](https://github.com/yourusername/in-space-furniture)")

# ========== FOOTER ==========
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([2, 1, 1])

with footer_col1:
    st.caption("🪑 **IN SPACE FURNITURE** © 2024 | Complete Ecosystem Demo")

with footer_col2:
    if PLOTLY_AVAILABLE:
        st.caption("✅ 3D Features: Active")
    else:
        st.caption("🔄 3D Features: Loading...")

with footer_col3:
    st.caption("🚀 Deployed on Streamlit Cloud")
