import streamlit as st
import random
from PIL import Image
import io

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
            import time
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

def show_room_visualization(room_data):
    """Show room visualization"""
    if room_data:
        st.subheader("🏠 Room Visualization")
        
        # Simple ASCII room visualization
        width = room_data['dimensions']['width']
        length = room_data['dimensions']['length']
        
        st.code(f"""
        ROOM LAYOUT:
        {'┌' + '─' * width + '┐'}
        {'│' + ' ' * width + '│'}  Length: {length} ft
        {'│' + ' ' * width + '│'}
        {'│' + ' ' * width + '│'}  Width: {width} ft
        {'│' + ' ' * width + '│'}
        {'└' + '─' * width + '┘'}
        
        Key:
        ░ - Walking Space ({room_data['walking_space']} ft)
        █ - Furniture Placement Zone
        """)
        
        # Climate summary
        st.info(f"**Climate Summary:** {room_data['climate']['humidity']}% humidity, "
                f"{room_data['climate']['temperature']}°C in {room_data['climate']['location']}")
