from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List, Tuple, Set, Dict
import re

class SimilarityCalculator:
    @staticmethod
    def preprocess_text(text: str) -> Set[str]:
        """
        Clean and preprocess text by:
        1. Converting to lowercase
        2. Removing special characters
        3. Removing common words
        4. Splitting into words
        """
        # Common words to remove
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        
        # Convert to lowercase and remove special characters
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        
        # Split into words and remove common words
        words = set(text.split())
        return words - common_words

    @staticmethod
    def calculate_jaccard_similarity(first_set: Set[str], second_set: Set[str]) -> float:
        """
        Calculate Jaccard similarity between two sets of words.
        Jaccard similarity = size of intersection / size of union
        """
        if not first_set or not second_set:
            return 0.0
            
        intersection = len(first_set.intersection(second_set))
        union = len(first_set.union(second_set))
        
        return intersection / union if union > 0 else 0.0

    def calculate_content_similarity(self, first_movie: Dict[str, str], second_movie: Dict[str, str]) -> float:
        """
        Calculate similarity between two movies using multiple features:
        1. Description similarity (50% weight)
        2. Genre similarity (30% weight)
        3. Title word similarity (20% weight)
        """
        # Calculate description similarity
        description_similarity = self.calculate_jaccard_similarity(
            self.preprocess_text(first_movie['description']),
            self.preprocess_text(second_movie['description'])
        )
        
        # Calculate genre similarity
        genre_similarity = self.calculate_jaccard_similarity(
            set(first_movie.get('genre', '').lower().split(',')),
            set(second_movie.get('genre', '').lower().split(','))
        )
        
        # Calculate title similarity
        title_similarity = self.calculate_jaccard_similarity(
            self.preprocess_text(first_movie['title']),
            self.preprocess_text(second_movie['title'])
        )
        
        # Weighted combination
        total_similarity = (
            0.5 * description_similarity +  # Description has highest weight
            0.3 * genre_similarity +        # Genre matching is important
            0.2 * title_similarity          # Title words might indicate similarity
        )
        
        return total_similarity

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
