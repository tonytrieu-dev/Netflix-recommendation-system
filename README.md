# Netflix Recommendation System

A Python package that provides personalized Netflix recommendations using hybrid-based recommendation.

## Installation

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/tonytrieu-dev/Netflix-recommendation-system.git
```

Or clone the repository and install locally:

```bash
git clone https://github.com/tonytrieu-dev/Netflix-recommendation-system.git
cd Netflix-recommendation-system
pip install -e .
```

## Features

- Hybrid recommendation system that uses content-based filtering and collaborative filtering
- Easy-to-use interface for getting personalized recommendations
- Built-in dataset management for some Netflix content

## Quick Start

```python
from netflix_recommender import ContentRecommender, DataManager
from netflix_recommender.similarity import SimilarityCalculator

# Initialize components
data_manager = DataManager()
similarity_calculator = SimilarityCalculator()
recommender = ContentRecommender(data_manager, similarity_calculator)

# Get recommendations
recommendations = recommender.recommend_from_title("The Matrix", 5)
```

## Requirements

- Python >= 3.6
- pandas
- numpy
- scikit-learn
