import streamlit as st

# Import our custom header & utilities
from header import render_header
from utils import load_image, local_css, init_cart

# Import page modules
from home import home_page
from about import about_us_page
from products import products_page
from contact import contact_page
from cart import cart_page
from footer import render_footer

# Load Custom Icon
icon_img = load_image("pageicon.png")

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Girshala | Tradition You Can Taste",
    page_icon=icon_img if icon_img else " ",  # Setting our custom image as the browser tab icon
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------
# MAIN APP ROUTING
# -----------------------------------
def main():
    # Setup global CSS styles
    local_css()

    # Init session state Cart variables
    init_cart()

    # Render Header Navigation
    current_page = render_header()

    # Routing
    if current_page == "Home":
        home_page()
    elif current_page == "About Us":
        about_us_page()
    elif current_page in ["Product", "Products"]: 
        products_page()
    elif current_page == "Contact":
        contact_page()
    elif current_page == "Cart":
        cart_page()

    # Footer displayed on all pages natively
    render_footer()

if __name__ == "__main__":
    main()
