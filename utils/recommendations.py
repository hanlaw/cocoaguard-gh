def get_recommendation(predicted_class: str) -> dict:
    """
    Returns structured recommendation for the predicted class.
    """
    recommendations = {
        'healthy': {
            'summary': 'No signs of CSSVD detected.',
            'actions': [
                'Continue regular farm monitoring',
                'Maintain good farm sanitation',
                'Check surrounding trees periodically',
                'Keep records of farm health observations'
            ],
            'urgency': 'low'
        },
        'cssvd': {
            'summary': 'CSSVD infection detected on this plant.',
            'actions': [
                'Isolate the infected tree immediately',
                'Contact your agricultural extension officer',
                'Do not move plant material from infected area',
                'Monitor all surrounding trees closely',
                'Document the location and severity'
            ],
            'urgency': 'high'
        }
    }
    return recommendations[predicted_class]