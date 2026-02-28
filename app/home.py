import streamlit as st
from utils import load_image

def home_page():
    st.title("GIRSHALA")
    st.subheader("Tradition You Can Taste • Purity You Can Trust")
    st.write("---")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        #### Premium A2 Desi Cow Ghee

        Girshala brings authentic A2 ghee directly from village farmers to your home.
        We combine **traditional dairy practices**, **ethical sourcing**, and
        **modern transparency** to deliver purity you can trust.
        """)

        # Core USP
        st.info("""
        **Our Core USP:** Authentic A2 ghee made locally, sourced fairly from farmers, 
        and priced for real families — combining tradition, trust, and accessibility.
        """)
        
        if st.button("Explore Products", type="primary"):
            st.session_state.page = "Product"
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        img_bestseller = load_image("BestSeller.jpeg")
        if img_bestseller:
            st.image(img_bestseller, caption="Our Best Seller", use_container_width=True)

    with col2:
        img_a2 = load_image("product_image.jpeg")
        if img_a2:
            st.image(img_a2, use_container_width=True)

    st.write("---")
    
    st.markdown("<h2 style='text-align: center;'>🌿 Why Girshala?</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("###Indigenous A2 Milk")
        st.write("Milk sourced from Gir, Sahiwal, Rathi and other A2 cows ensuring purity.")
    with c2:
        st.markdown("### Connect with Farmers")
        st.write("Direct procurement from nearby villages ensuring fair pricing.")
    with c3:
        st.markdown("### Small Batch Fresh")
        st.write("Local production ensures fresher and aromatic ghee.")
        
    st.write("---")
    
    # Adding customer/review section
    st.markdown("<h2 style='text-align: center;'>⭐ Happy Customers</h2>", unsafe_allow_html=True)
    img_cust = load_image("Customer.jpeg")
    if img_cust:
        st.image(img_cust, use_container_width=True)
