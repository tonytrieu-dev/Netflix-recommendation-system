from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Tuple

class SimilarityCalculator:
    @staticmethod
    def calculate_jaccard_similarity(first_description: str, second_description: str) -> float:
        """
        Calculate Jaccard similarity between two text descriptions.
        
        Args:
            first_description: First text description
            second_description: Second text description
            
        Returns:
            Jaccard similarity score between 0 and 1
        """
        # Convert descriptions to sets of words
        first_words = set(first_description.lower().split())
        second_words = set(second_description.lower().split())
        
        # Calculate intersection and union
        intersection = len(first_words.intersection(second_words))
        union = len(first_words.union(second_words))
        
        # Return Jaccard similarity
        if union == 0:
            return 0.0
        return intersection / union

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
