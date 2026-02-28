import streamlit as st
from utils import load_image

def about_us_page():
    st.title("🏢 About Us")
    st.subheader("Building a Sustainable and Ethical Dairy Ecosystem")
    
    img_main = load_image("image.png")
    if img_main:
        st.image(img_main, use_container_width=True)

    st.write("---")

    st.header("📈 Our Business Model")
    st.markdown("""
    - **Direct Village-Based Milk Procurement:** Procuring fresh A2 milk directly from nearby villages (within 20 km radius).
    - **On-Site Fat Testing:** We test fat percentage immediately to ensure fair payment and premium quality (4.5% to 6.5%).
    - **Fair Payment Pipeline:** Daily End-of-Day (EOD) credit system so farmers aren't left waiting.
    - **Hyper-Local Freshness:** Our batches are produced locally and delivered fast, maintaining freshness and aroma.
    """)

    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("🔍 Radical Transparency")
        st.markdown("""
        Girshala believes customers deserve to know **where their food comes from**.

        ✔ Milk sourced within a 20 km radius  
        ✔ Quality & fat testing available for scrutiny  
        ✔ Ethical village-level partnerships  
        ✔ Full traceability from farm to table
        """)
    with col2:
        st.header("🤝 Supporting Farmers")
        st.markdown("""
        We connect farmers with livestock loans through partner financial institutions. 
        By simplifying the process and assisting with documentation, we help them purchase indigenous A2 cows.
        This builds long-term partnerships and provides sustainable income opportunities.
        """)
