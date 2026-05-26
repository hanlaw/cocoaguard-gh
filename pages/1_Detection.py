import streamlit as st
from PIL import Image

from utils.model_loader import load_model
from utils.preprocessor import preprocess_image
from utils.predictor import predict
from utils.recommendations import get_recommendation
from utils.charts import confidence_bar_chart


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title='CSSVD Detection System',
    page_icon='🌿',
    layout='wide'
)


# ==========================================
# CUSTOM STYLING
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton > button {
    border-radius: 10px;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PAGE HEADER
# ==========================================

st.title('🌿 CSSVD Detection')

st.caption(
    'Upload or capture a photo to receive an instant AI diagnosis'
)

st.divider()


# ==========================================
# LOAD MODEL
# ==========================================

model = load_model()


# ==========================================
# IMAGE INPUT SECTION
# ==========================================

st.subheader('📸 Select Image Source')

st.info(
    'Choose whether to upload an existing image or capture one live using your camera.'
)

image = None


# ------------------------------------------
# TABS
# ------------------------------------------

tab1, tab2 = st.tabs([
    '📁 Upload Image',
    '📷 Use Camera'
])


# ==========================================
# TAB 1 — FILE UPLOAD
# ==========================================

with tab1:

    uploaded = st.file_uploader(
        'Upload a photo of a cocoa leaf, stem or pod',
        type=['jpg', 'jpeg', 'png'],
        help='Take a clear, close-up photo in good lighting'
    )

    if uploaded:

        image = Image.open(uploaded)


# ==========================================
# TAB 2 — CAMERA INPUT
# ==========================================

with tab2:

    camera_photo = st.camera_input(
        'Take a photo of a cocoa leaf, stem or pod',
        help='Ensure the image is clear and well lit'
    )

    if camera_photo:

        image = Image.open(camera_photo)


# ==========================================
# IMAGE PROCESSING + PREDICTION
# ==========================================

if image:

    st.divider()

    col1, col2 = st.columns(2)

    # --------------------------------------
    # IMAGE DISPLAY
    # --------------------------------------

    with col1:

        st.image(
            image,
            caption='Selected Image',
            use_container_width=True
        )

    # --------------------------------------
    # AI PROCESSING
    # --------------------------------------

    with st.spinner('🧠 Analysing image using AI model...'):

        processed = preprocess_image(image)

        result = predict(
            model,
            processed
        )

        recommendation = get_recommendation(
            result['predicted_class']
        )

    # --------------------------------------
    # PREDICTION RESULTS
    # --------------------------------------

    with col2:

        st.subheader('🔍 Diagnosis Result')

        if result['predicted_class'] == 'healthy':

            st.success('✅ Healthy Plant Detected')

        else:

            st.error('🚨 CSSVD Detected')

        st.metric(
            label='Confidence Score',
            value=f"{result['confidence']:.1f}%"
        )

        st.markdown('### 📊 Prediction Confidence')

        fig = confidence_bar_chart(
            result['cssvd_probability'],
            result['healthy_probability']
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ======================================
    # RECOMMENDATIONS SECTION
    # ======================================

    st.divider()

    st.subheader('📋 Recommended Actions')

    if recommendation['urgency'] == 'high':

        st.error(
            f"⚠️ {recommendation['summary']}"
        )

    else:

        st.success(
            f"✅ {recommendation['summary']}"
        )

    st.markdown('### Recommended Steps')

    for action in recommendation['actions']:

        st.markdown(f"- {action}")

    # ======================================
    # DISCLAIMER
    # ======================================

    st.divider()

    st.caption(
        '⚠️ This tool is designed to assist farmers and '
        'extension officers. Always consult a qualified '
        'agricultural officer for final diagnosis decisions.'
    )


# ==========================================
# VISUAL REFERENCE GUIDE
# ==========================================

st.divider()

st.subheader('📖 Visual Reference Guide')

st.caption(
    'Use these examples to understand symptoms before uploading your image.'
)

ref_col1, ref_col2 = st.columns(2)


# ------------------------------------------
# HEALTHY SAMPLE
# ------------------------------------------

with ref_col1:

    st.image(
        'assets/sample_healthy.jpg',
        caption=(
            '✅ Healthy Cocoa Plant — '
            'Even green colour, normal leaf shape, '
            'no distortion or swelling'
        ),
        use_container_width=True
    )


# ------------------------------------------
# CSSVD SAMPLE
# ------------------------------------------

with ref_col2:

    st.image(
        'assets/sample_cssvd.jpg',
        caption=(
            '🚨 CSSVD Infected Plant — '
            'Mosaic patterns, vein banding, '
            'leaf distortion and swollen shoots'
        ),
        use_container_width=True
    )


# ==========================================
# EDUCATIONAL SECTION
# ==========================================

with st.expander('🔬 What symptoms should I look for?'):

    st.markdown("""

    ## Early CSSVD Symptoms

    - **Leaf mosaic**  
      Irregular light and dark green patches on leaves

    - **Vein banding**  
      Yellowing along the leaf veins

    - **Leaf distortion**  
      Leaves may appear twisted or curled

    - **Reddish flush**  
      Bronze or reddish coloration on young leaves


    ## Advanced CSSVD Symptoms

    - **Swollen shoots**  
      Abnormal thickening of stems and branches

    - **Stunted growth**  
      Tree becomes smaller than surrounding trees

    - **Reduced pod production**  
      Fewer and smaller cocoa pods

    - **Dieback**  
      Branches begin dying from the tips downward


    ## Healthy Plant Signs

    - Uniform deep green leaf colour
    - Normal leaf structure
    - No swelling on stems
    - Active and healthy pod growth

    """)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    '🌍 AI-Powered Cocoa Disease Detection System | '
    'Built with Streamlit and TensorFlow'
)
