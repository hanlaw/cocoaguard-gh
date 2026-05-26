import streamlit as st

st.set_page_config(
    page_title='CocoaGuard GH',
    page_icon='🌿',
    layout='centered'
)

st.title('CocoaGuard GH')
st.caption('CSSVD Early Detection — Powered by Sankofa Intelligence')
st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.image('assets/logo.jpeg', width=200)

with col2:
    st.markdown("""
    ## What is CocoaGuard GH?

    CocoaGuard GH is an AI-powered tool designed to help 
    Ghanaian cocoa farmers detect **Cocoa Swollen Shoot Virus 
    Disease (CSSVD)** early using a photo of a leaf, stem or pod.

    Early detection saves farms. CSSVD spreads silently — 
    by the time visible damage is severe, nearby trees are 
    already infected.

    ---

    ### How to Use
    1. Navigate to **Detection** in the sidebar
    2. Upload a clear photo of a cocoa leaf or stem
    3. Receive an instant AI diagnosis with confidence score
    4. Follow the recommended actions
    """)

st.divider()

col3, col4, col5 = st.columns(3)

with col3:
    st.info("**AI Detection**\n\nUpload a photo for instant CSSVD diagnosis")

with col4:
    st.info("**Analytics**\n\nExplore dataset and model performance data")

with col5:
    st.info("**Model Info**\n\nUnderstand how the AI model was built")

st.divider()
st.caption('Sankofa Intelligence | Ghana | 2026')
