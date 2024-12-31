# Netflix Recommendation System

A Python package that provides personalized movie and TV show recommendations using content-based and hybrid recommendation approaches.

## Installation

```bash
pip install netflix-recommender
```

## Features

- Content-based recommendation system for movies and TV shows
- Hybrid recommendation system combining multiple approaches
- Easy-to-use interface for getting personalized recommendations
- Built-in dataset management for Netflix content

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

## License

MIT License