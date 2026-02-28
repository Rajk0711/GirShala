import streamlit as st

def contact_page():
    st.title("📞 Contact Us")
    st.subheader("We'd love to hear from you!")
    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        ### Get in Touch
        Reach out to us directly for any inquiries, bulk orders, or support.
        
        - 📧 **Email:** support@girshala.com
        - 📱 **Phone / WhatsApp:** +91 98765 43210
        - 📍 **Farm Location:** Girshala Farms, Chittorgarh District, Rajasthan, India
        """)
        
    with c2:
        st.markdown("### Send a Message")
        with st.form("contact_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
            
            if submitted:
                st.success(f"Thank you {name}! Your message has been sent successfully.")
