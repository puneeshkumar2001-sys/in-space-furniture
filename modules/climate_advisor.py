import streamlit as st
import pandas as pd

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
    
    # Visual comparison
    st.subheader("📈 Climate Suitability Chart")
    
    # Create suitability bars
    humidity = climate_data.get('humidity', 50)
    woods = ["Teak", "Mango", "Teak/Mango", "Walnut"]
    suitability = [95, 70, 85, 80]
    
    # Adjust based on actual humidity
    adjustment = [0, -abs(humidity-70), -abs(humidity-65), -abs(humidity-60)]
    adjusted_suitability = [max(60, s + a) for s, a in zip(suitability, adjustment)]
    
    chart_data = pd.DataFrame({
        "Wood": woods,
        "Suitability Score": adjusted_suitability
    })
    
    st.bar_chart(chart_data.set_index("Wood"))
    
    st.session_state['recommendation'] = recommendation
    return recommendation
