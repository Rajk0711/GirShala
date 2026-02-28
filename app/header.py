import streamlit as st
from PIL import Image
import os

# ---------------------------------------------------
# HUMPY STYLE HEADER CSS
# ---------------------------------------------------
def initialize_header_css():
    st.markdown("""
    <style>
    /* Hide default Streamlit elements */
    [data-testid="collapsedControl"] {display:none;}
    section[data-testid="stSidebar"] {display:none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* ===== STICKY HEADER ===== */
    div[data-testid="stVerticalBlock"] > div:first-child {
        position: sticky;
        top: 0;
        z-index: 999;
        background: white;
        padding: 10px 40px;
        border-bottom: 1px solid #eee;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
    }

    /* ===== NAV CENTER ALIGN ===== */
    div.stRadio > div[role="radiogroup"] {
        flex-direction: row;
        justify-content: center;
        gap: 30px;
    }

    /* ===== MENU ITEMS ===== */
    div.stRadio label {
        font-size: 16px;
        font-weight: 600;
        color: #333;
        padding-bottom: 4px;
        border-bottom: 2px solid transparent;
        transition: all 0.25s ease;
        cursor: pointer;
    }

    div.stRadio label:hover {
        color: #e67e22;
        border-bottom: 2px solid #e67e22;
    }

    /* ===== ULTRA-TIGHT ICON BUTTONS (NO AURA) ===== */
    /* Target buttons in the right column */
    div[data-testid="stColumn"] button {
        background: transparent !important;
        border: none !important;
        padding: 0px !important;
        margin: 0px !important;
        width: 35px !important; /* Fixed width for alignment */
        height: 35px !important;
        min-height: 0px !important;
        line-height: 1 !important;
        box-shadow: none !important;
        font-size: 22px !important;
        display: flex !important;
        align-items: center;
        justify-content: center;
        transition: transform 0.2s ease, color 0.2s ease;
    }

    div[data-testid="stColumn"] button:hover {
        transform: scale(1.2);
        color: #e67e22 !important;
        background: transparent !important;
    }

    div[data-testid="stColumn"] button:active, 
    div[data-testid="stColumn"] button:focus {
        background: transparent !important;
        color: #e67e22 !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* Fix for button container spacing */
    div[data-testid="stColumn"] [data-testid="stVerticalBlock"] > div {
        padding: 0px !important;
    }

    /* Logo Vertical Alignment */
    .logo-text {
        font-size: 24px;
        font-weight: 800;
        color: #e67e22;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER COMPONENT
# ---------------------------------------------------
def render_header():
    # Initialize session states
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    if "cart" not in st.session_state:
        st.session_state.cart = []

    initialize_header_css()
    cart_count = len(st.session_state.cart)

    # Header Layout
    # Ratio: 1.5 (Logo) : 5 (Nav) : 1.5 (Icons)
    col_left, col_center, col_right = st.columns([1.5, 5, 1.5])

    with col_left:
        # Load Logo Image
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path = os.path.join(base_dir, "images", "pageicon.png")
        if os.path.exists(logo_path):
            img = Image.open(logo_path)
            st.image(img, width=90)
        else:
            st.markdown('<p class="logo-text">Girshala</p>', unsafe_allow_html=True)

    with col_center:
        pages = ["Home", "About Us", "Product", "Contact"]
        
        # Determine current index for radio
        try:
            current_idx = pages.index(st.session_state.page)
        except ValueError:
            current_idx = None

        selected = st.radio(
            "nav",
            pages,
            index=current_idx,
            horizontal=True,
            label_visibility="collapsed",
            key="header_nav_radio"
        )

        if selected is not None and selected != st.session_state.page:
            st.session_state.page = selected
            st.rerun()

    with col_right:
        # We use a nested 3-column layout with NO GAP to keep icons tight
        ic1, ic2, ic3 = st.columns([1, 1, 1])

        with ic1:
            if st.button("🔍", key="h_search"):
                st.toast("Search clicked")

        with ic2:
            if st.button("👤", key="h_profile"):
                st.toast("Profile clicked")

        with ic3:
            # Cart icon shows count if > 0
            cart_display = f"🛒{cart_count}" if cart_count > 0 else "🛒"
            if st.button(cart_display, key="h_cart"):
                st.session_state.page = "Cart"
                st.rerun()

    return st.session_state.page
