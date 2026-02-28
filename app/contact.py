import streamlit as st

def contact_page():
    # 1. Page Header
    st.markdown("<h1 style='text-align: center; color: #2c3e50;'>📞 Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #7f8c8d;'>We'd love to hear from you!</p>", unsafe_allow_html=True)
    st.write("---")

    # 2. Add Specific CSS for Form Visibility
    st.markdown("""
    <style>
    /* Ensure form inputs are visible with a subtle border */
    .stTextInput input, .stTextArea textarea {
        border: 1px solid #ddd !important;
        background-color: #fafafa !important;
        color: #333 !important;
    }
    
    /* Contact Form Submit Button - High Contrast Orange */
    div.stForm button[kind="primary"] {
        background-color: #e67e22 !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem !important;
        font-weight: bold !important;
        transition: 0.3s;
    }

    div.stForm button[kind="primary"]:hover {
        background-color: #d35400 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.2], gap="large")
    
    with c1:
        st.markdown("""
        ### Get in Touch
        Reach out to us directly for any inquiries, bulk orders, or support.
        
        - 📧 **Email:** support@girshala.com
        - 📱 **WhatsApp:** [+91 98765 43210](https://wa.me/919876543210)
        - 📍 **Farm:** Girshala Farms, Chittorgarh, Rajasthan
        """)
        
        # Optional: Add a small decorative element or map placeholder
        st.info("💡 **Bulk Orders:** We offer special pricing for orders above 5kg. Mention 'BULK' in your message!")

    with c2:
        st.markdown("### Send a Message")
        # Ensure the form is clean and variables are defined
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name", placeholder="Enter your name")
            email = st.text_input("Email Address", placeholder="example@email.com")
            message = st.text_area("Your Message", placeholder="How can we help you?", height=120)
            
            # The 'submitted' variable captures the form click
            submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success(f"Thank you {name}! Your message has been sent successfully.")
                else:
                    st.error("Please fill in all fields before sending.")

    st.write("---")
    st.markdown("<p style='text-align: center; color: #95a5a6;'>Follow us on Instagram @Girshala_Ghee</p>", unsafe_allow_html=True)