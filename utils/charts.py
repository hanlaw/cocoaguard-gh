import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def confidence_bar_chart(cssvd_prob: float, healthy_prob: float):
    """
    Horizontal bar chart showing probability for each class.
    """
    df = pd.DataFrame({
        'Class': ['CSSVD', 'Healthy'],
        'Probability': [cssvd_prob, healthy_prob],
        'Color': ['#E74C3C', '#2ECC71']
    })

    fig = px.bar(
        df,
        x='Probability',
        y='Class',
        orientation='h',
        color='Class',
        color_discrete_map={
            'CSSVD': '#E74C3C',
            'Healthy': '#2ECC71'
        },
        title='Prediction Confidence Breakdown',
        range_x=[0, 100]
    )

    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FAFAFA',
        xaxis_title='Confidence (%)',
        yaxis_title=''
    )

    return fig


def dataset_distribution_chart(cssvd_count: int, healthy_count: int):
    """
    Pie chart showing dataset class distribution.
    """
    fig = px.pie(
        names=['CSSVD', 'Healthy'],
        values=[cssvd_count, healthy_count],
        title='Dataset Class Distribution',
        color_discrete_sequence=['#E74C3C', '#2ECC71']
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FAFAFA'
    )

    return fig


def training_history_chart(metric: str, train_values: list, val_values: list):
    """
    Line chart for training vs validation metrics.
    metric: 'Accuracy' or 'Loss'
    """
    epochs = list(range(1, len(train_values) + 1))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=epochs,
        y=train_values,
        mode='lines+markers',
        name=f'Training {metric}',
        line=dict(color='#2ECC71')
    ))

    fig.add_trace(go.Scatter(
        x=epochs,
        y=val_values,
        mode='lines+markers',
        name=f'Validation {metric}',
        line=dict(color='#3498DB')
    ))

    fig.update_layout(
        title=f'Training vs Validation {metric}',
        xaxis_title='Epoch',
        yaxis_title=metric,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#FAFAFA'
    )

    return fig