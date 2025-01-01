from typing import List, Tuple, Dict
from data_manager import DataManager
from similarity import SimilarityCalculator
import pandas as pd

class ContentRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator
        self._fit_similarity_calculator()

    def _fit_similarity_calculator(self) -> None:
        """Prepare the similarity calculator with the current dataset."""
        if self.data_manager.data is None:
            raise ValueError("No data loaded in DataManager")
        
        descriptions = self.data_manager.data['description'].fillna('').tolist()
        titles = self.data_manager.data['title'].tolist()
        self.similarity_calculator.fit(descriptions, titles)

    def find_similar_content(self, title: str, n: int = 5) -> List[Tuple[str, float]]:
        """Find n most similar titles to the given title."""
        if title not in self.data_manager.data['title'].values:
            raise ValueError(f"Title '{title}' not found in dataset")

        title_idx = self.data_manager.data[self.data_manager.data['title'] == title].index[0]
        return self.similarity_calculator.get_similar_items(title_idx, n)

class UserBasedRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator

    def recommend_from_ratings(self, user_ratings: Dict[str, float], count: int) -> List[Tuple[str, float]]:
        """
        Recommend content based on user ratings.
        
        Args:
            user_ratings: Dictionary mapping title to rating
            count: Number of recommendations to return
            
        Returns:
            List of (title, score) tuples
        """
        recommendations = []
        rated_titles = set(user_ratings.keys())
        
        # For each rated title, find similar content
        for title, rating in user_ratings.items():
            if title not in self.data_manager.data['title'].values:
                continue
                
            title_idx = self.data_manager.data[self.data_manager.data['title'] == title].index[0]
            similar_items = self.similarity_calculator.get_similar_items(title_idx)
            
            # Weight similar items by user rating
            for similar_title, similarity in similar_items:
                if similar_title not in rated_titles:
                    weighted_score = similarity * rating
                    recommendations.append((similar_title, weighted_score))
        
        # Aggregate scores for same titles and sort
        title_scores = {}
        for title, score in recommendations:
            title_scores[title] = title_scores.get(title, 0) + score
            
        sorted_recommendations = sorted(
            title_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        return sorted_recommendations[:count]
