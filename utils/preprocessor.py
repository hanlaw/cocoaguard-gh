import numpy as np
from PIL import Image

IMG_SIZE = (224, 224)

def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Takes a PIL Image and returns a numpy array
    ready for model prediction.
    
    Raw pixels 0-255 are passed through without
    scaling — EfficientNetPreprocessing inside
    the model handles the scaling internally.
    """
    image = image.convert('RGB')
    image = image.resize(IMG_SIZE)
    img_array = np.array(image, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array