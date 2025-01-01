from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Tuple

class SimilarityCalculator:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self.titles = None

    def fit(self, descriptions: List[str], titles: List[str]) -> None:
        """Fit the vectorizer and create TF-IDF matrix."""
        self.tfidf_matrix = self.vectorizer.fit_transform(descriptions)
        self.titles = titles

    def get_similar_items(self, title_idx: int, n: int = 5) -> List[Tuple[str, float]]:
        """Get n most similar items to the given title index."""
        if self.tfidf_matrix is None or self.titles is None:
            raise ValueError("Calculator not fitted. Call fit() first.")

        # Calculate similarity scores
        sim_scores = cosine_similarity(
            self.tfidf_matrix[title_idx:title_idx+1], 
            self.tfidf_matrix
        ).flatten()

        # Get indices of top similar items (excluding self)
        similar_indices = sim_scores.argsort()[::-1][1:n+1]

        # Return titles and scores
        return [(self.titles[idx], sim_scores[idx]) for idx in similar_indices]
