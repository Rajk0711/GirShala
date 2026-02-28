import streamlit as st
from PIL import Image
import os

from utils import load_image, add_to_cart

# ---------------------------------------------------
# PRODUCT PAGE STYLING
# ---------------------------------------------------
def apply_product_styles():
    st.markdown("""
    <style>
    /* Product Card Styling */
    .product-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #f0f0f0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        border-color: #e67e22;
    }

    /* FIX: Make the 'Add to Cart' button highly visible */
    div.stButton > button[kind="primary"] {
        background-color: #e67e22 !important; /* Humpy Orange */
        color: white !important;
        border: none !important;
        width: 100% !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        box-shadow: 0 4px 6px rgba(230, 126, 34, 0.2) !important;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #d35400 !important;
        border: none !important;
        color: white !important;
    }

    /* Radio button styling to match theme */
    div[data-testid="stMarkdownContainer"] h3 {
        color: #2c3e50;
    }
    
    /* Comparison Image Container */
    .comp-img {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)


# ---------------------------------------------------
# PRODUCTS PAGE FUNCTION
# ---------------------------------------------------
def products_page():
    apply_product_styles()

    st.markdown("<h1 style='text-align: center; color: #2c3e50;'>Our Products</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #7f8c8d;'>Premium A2 Quality at Accessible Pricing</p>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2, gap="large")

    # --- PRODUCT 1: GHEE ---
    with col1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### Girshala Premium A2 Ghee 🧈")
        
        # Replace dummy_load_image with your actual load_image function
        img1 = load_image("product_image.jpeg")
        if img1:
            st.image(img1, use_container_width=True)
        else:
            st.warning("Product Image Missing")
            
        st.info("Authentic A2 Desi Cow Ghee made with traditional Bilona method locally.")
        
        # Product Variations
        size_options = {
            "250 gm": 650,
            "500 gm": 1200,
            "1 kg": 2200
        }
        
        selected_size = st.radio("Select Weight", list(size_options.keys()), horizontal=True, key="ghee_size")
        selected_price = size_options[selected_size]
        
        st.markdown(f"### Price: ₹{selected_price}")
        
        if st.button(f"Add {selected_size} to Cart", key="buy_main", type="primary"):
            # Replace with your actual add_to_cart
            add_to_cart("Girshala Premium A2 Ghee", selected_size, selected_price)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- PRODUCT 2: TRIAL PACK ---
    with col2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### Girshala Trial Pack 🍯")
        
        img2 = load_image("product_image.jpeg")
        if img2:
            st.image(img2, use_container_width=True)
        else:
            st.warning("Trial Image Missing")

        st.info("Perfect for first-time buyers! Experience our premium aroma and taste.")
        
        trial_size_options = {
            "50 gm": 150,
            "100 gm": 280
        }
        
        selected_trial_size = st.radio("Choose Trial Weight", list(trial_size_options.keys()), horizontal=True, key="trial_size")
        selected_trial_price = trial_size_options[selected_trial_size]
        
        st.markdown(f"### Price: ₹{selected_trial_price}")

        if st.button(f"Add {selected_trial_size} to Cart", key="buy_trial", type="primary"):
             # Replace with your actual add_to_cart
             add_to_cart("Girshala Trial Pack", selected_trial_size, selected_trial_price)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write("---")
    
    # --- COMPARISON SECTION ---
    st.markdown("<h2 style='text-align: center;'>🆚 Why Choose Girshala?</h2>", unsafe_allow_html=True)
    
    # Diagrammatic representation of quality levels
    

    img_comparision = load_image("product_comparision.jpeg")
    if img_comparision:
        st.image(img_comparision, use_container_width=True, caption="Girshala vs Others")
        
    st.write("---")
    st.success("✨ **Bulk Orders:** Reach out on WhatsApp for special discounts on 5kg+ orders!")
