import streamlit as st
from utils import load_image

def render_footer():
    """Renders the common footer across all application pages."""
    st.write("---")
    col1, col2 = st.columns([1.5, 2])
    
    with col1:
        img_footer = load_image("Footer Image.jpeg")
        if img_footer:
            st.image(img_footer, use_container_width=True)
            
    with col2:
        st.markdown("### 📞 Contact Us & Info")
        st.markdown("""
        **Address:** Girshala Farms, Village Surroundings, Chittorgarh District, Rajasthan, India
        
        **Email:** contact@girshala.com
        
        **Phone / WhatsApp:** +91 98765 43210
        
        **About Us:**
        Girshala directly procures A2 milk from nearby village farmers, eliminating middlemen 
        and guaranteeing authenticity. We pride ourselves on the traditional Bilona method, 
        ethical partnerships, and a localized farm-to-family approach.
        """)
    st.markdown("<p style='text-align: center; color: #8d6e63; font-size: 14px;'>© 2026 Girshala | Farm to Family | All Rights Reserved.</p>", unsafe_allow_html=True)
