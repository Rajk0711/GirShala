import streamlit as st
from utils import remove_from_cart

def cart_page():
    # CSS for the Summary Card
    st.markdown("""
        <style>
        .summary-card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #e1e4e8;
        }
        .item-row {
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛒 Your Shopping Cart")
    st.write("---")
    
    if not st.session_state.cart:
        st.info("Your cart is empty. Let's find some pure A2 products!")
        if st.button("Browse Products", type="primary"):
            st.session_state.page = "Product"
            st.rerun()
        return

    # Layout: Items on Left, Summary on Right
    col_items, col_summary = st.columns([2.5, 1.5])
    
    subtotal = 0
    
    with col_items:
        st.subheader(f"{len(st.session_state.cart)} Items in your cart")
        
        for i, item in enumerate(st.session_state.cart):
            with st.container():
                c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
                c1.markdown(f"**{item['Product']}**")
                c2.write(f"Size: {item['Weight']}")
                c3.markdown(f"**₹{item['Price']}**")
                
                if c4.button("❌", key=f"del_{i}", help="Remove item"):
                    remove_from_cart(i)
                    st.rerun()
            
            subtotal += item['Price']
            st.write("---")

    with col_summary:
        st.markdown('<div class="summary-card">', unsafe_allow_html=True)
        st.subheader("Order Summary")
        
        # Calculate charges
        delivery_fee = 0 if subtotal > 1000 else 50 # Example logic: Free over 1000
        grand_total = subtotal + delivery_fee
        
        st.write(f"Subtotal: {' ' * 10} ₹{subtotal}")
        st.write(f"Delivery Fee: {' ' * 4} ₹{delivery_fee}")
        st.write("---")
        st.markdown(f"### Total: ₹{grand_total}")
        
        if st.button("Proceed to Checkout 🚀", type="primary", use_container_width=True):
            # Integrate payment logic here
            st.success("Order placed successfully!")
            st.balloons()
            st.session_state.cart = []
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("🔒 Secure checkout via Razorpay/UPI")