# Netflix Recommendation System

A Python package that provides personalized Netflix recommendations using hybrid-based recommendation.

## Installation

```bash
pip install netflix-recommender
```

## Features

- Hybrid recommendation system that uses content-based filtering and collaborative filtering
- Easy-to-use interface for getting personalized recommendations
- Built-in dataset management for some Netflix content

## Quick Start

```python
from netflix_recommender import HybridRecommender

# Initialize the recommender
recommender = HybridRecommender()

# Get recommendations
recommendations = recommender.get_recommendations("The Matrix")
```

## Requirements

- Python >= 3.6
- pandas
- numpy
- scikit-learn
