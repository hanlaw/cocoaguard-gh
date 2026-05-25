import streamlit as st
from PIL import Image

from utils.model_loader import load_model
from utils.preprocessor import preprocess_image
from utils.predictor import predict
from utils.recommendations import get_recommendation
from utils.charts import confidence_bar_chart

st.title('🌿 CSSVD Detection')
st.caption('Upload a photo to receive an instant AI diagnosis')
st.divider()

model = load_model()

uploaded = st.file_uploader(
    'Upload a photo of a cocoa leaf, stem or pod',
    type=['jpg', 'jpeg', 'png'],
    help='Take a clear, close-up photo in good lighting'
)

if uploaded:
    image = Image.open(uploaded)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    with st.spinner('Analysing image...'):
        processed = preprocess_image(image)
        result = predict(model, processed)
        recommendation = get_recommendation(result['predicted_class'])

    with col2:
        if result['predicted_class'] == 'healthy':
            st.success(f"✅ **Healthy Plant**")
        else:
            st.error(f"🚨 **CSSVD Detected**")

        st.metric(
            label='Confidence',
            value=f"{result['confidence']:.1f}%"
        )

        fig = confidence_bar_chart(
            result['cssvd_probability'],
            result['healthy_probability']
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader('📋 Recommended Actions')

    if recommendation['urgency'] == 'high':
        st.error(f"⚠️ {recommendation['summary']}")
    else:
        st.success(f"✅ {recommendation['summary']}")

    for action in recommendation['actions']:
        st.markdown(f"- {action}")

    st.divider()

    st.caption(
        '⚠️ This tool is designed to assist farmers and '
        'extension officers. Always consult a qualified '
        'agricultural officer for final diagnosis decisions.'
    )

    st.divider()

st.subheader('📖 Visual Reference Guide')
st.caption('Use these examples to understand what to look for before uploading your photo')

ref_col1, ref_col2 = st.columns(2)

with ref_col1:
    st.image(
        'assets/sample_healthy.jpg',
        caption='✅ Healthy Cocoa Plant — Even green colour, no distortion, normal leaf shape',
        use_column_width=True
    )

with ref_col2:
    st.image(
        'assets/sample_cssvd.jpg',
        caption='🚨 CSSVD Infected Plant — Mosaic patterns, leaf distortion, vein banding, swollen shoots',
        use_column_width=True
    )

with st.expander('What symptoms should I look for?'):
    st.markdown("""
    ### Early CSSVD Symptoms
    - **Leaf mosaic** — irregular light and dark green patches on leaves
    - **Vein banding** — yellowing along the leaf veins
    - **Leaf distortion** — leaves appear twisted or curled
    - **Reddish flush** — bronze or reddish tinge on young leaves

    ### Advanced CSSVD Symptoms
    - **Swollen shoots** — abnormal thickening of stems and branches
    - **Stunted growth** — tree is noticeably smaller than surrounding trees
    - **Reduced pod production** — fewer and smaller pods
    - **Dieback** — branches dying from the tips downward

    ### Healthy Plant Signs
    - Uniform deep green leaf colour
    - Normal leaf shape with no distortion
    - Firm stems with no swelling
    - Active pod development
    """)