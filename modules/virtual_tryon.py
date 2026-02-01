import streamlit as st
import plotly.graph_objects as go
import numpy as np
import random

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
    
    # Walls
    fig.add_trace(go.Mesh3d(
        x=[0, width, width, 0],
        y=[0, 0, 0, 0],
        z=[0, 0, height, height],
        color='beige',
        opacity=0.2,
        name='Wall 1'
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
        
        st.image("https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=800", 
                caption="AR Furniture Preview Concept")
    
    return fit_score
