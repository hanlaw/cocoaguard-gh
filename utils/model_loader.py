import tensorflow as tf
import streamlit as st
from model_utils import EfficientNetPreprocessing

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        'model/phase2.keras',
        compile=False,
        custom_objects={
            'EfficientNetPreprocessing': EfficientNetPreprocessing
        }
    )