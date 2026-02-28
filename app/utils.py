import streamlit as st
import os
import base64
from PIL import Image

def load_image(image_name):
    """Loads an image from the images directory relative to the project root."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(base_dir, "images", image_name)
    if os.path.exists(image_path):
        return Image.open(image_path)
    return None

def get_base64_of_bin_file(bin_file):
    """Encodes a binary file (like an image) to a base64 string."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(base_dir, "images", bin_file)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

def init_cart():
    """Initializes the shopping cart in Streamlit's session state."""
    if "cart" not in st.session_state:
        st.session_state.cart = []

def add_to_cart(item_name, weight, price):
    """Adds an item to the session state shopping cart."""
    st.session_state.cart.append({"Product": item_name, "Weight": weight, "Price": price})
    st.toast(f"Added {weight} of {item_name} to cart! 🛒", icon="✅")

def remove_from_cart(index):
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)

def local_css():
    """Injects all application-wide custom styling overrides."""
    st.markdown("""
    <style>
    /* Main Background & Text Color */
    .stApp {
        background-color: #fdfaf6;
        color: #3e2723;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #d84315 !important;
        font-family: 'Georgia', serif;
    }
    
    /* Make standard app buttons (like Add to Cart) easily visible and matching theme */
    button[kind="primary"] {
        background-color: #d84315 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        transition: 0.3s !important;
    }
    button[kind="primary"]:hover {
        background-color: #bf360c !important;
    }
    
    /* Info/Success Boxes */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid #d84315;
        background-color: #ffe0b2;
        color: #4e342e;
    }
    
    hr {
        border-top: 1px solid #ffcc80;
    }
    </style>
    """, unsafe_allow_html=True)
