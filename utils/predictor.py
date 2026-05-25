import numpy as np

CLASS_NAMES = ['cssvd', 'healthy']
OPTIMAL_THRESHOLD = 0.65

def predict(model, processed_image: np.ndarray) -> dict:
    """
    Runs model inference and applies optimal threshold.
    
    Returns a dictionary with:
    - predicted_class: 'cssvd' or 'healthy'
    - confidence: float 0-100
    - probability: raw sigmoid output 0-1
    - cssvd_probability: probability of CSSVD 0-100
    - healthy_probability: probability of Healthy 0-100
    """
    raw_output = model.predict(processed_image, verbose=0)
    probability = float(raw_output[0][0])

    # Apply threshold — not np.argmax, sigmoid outputs single value
    if probability > OPTIMAL_THRESHOLD:
        predicted_class = 'healthy'
        confidence = probability * 100
    else:
        predicted_class = 'cssvd'
        confidence = (1 - probability) * 100

    return {
        'predicted_class': predicted_class,
        'confidence': confidence,
        'probability': probability,
        'cssvd_probability': (1 - probability) * 100,
        'healthy_probability': probability * 100
    }