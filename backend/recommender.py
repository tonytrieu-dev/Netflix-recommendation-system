from typing import List, Tuple, Dict
from data_manager import DataManager
from similarity import SimilarityCalculator

class ContentRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        """Initialize the content recommender with data manager and similarity calculator."""
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator

    def find_similar_content(self, title: str, number_of_recommendations: int = 5) -> List[Tuple[str, float]]:
        """
        Find similar content based on multiple features:
        - Description similarity
        - Genre similarity
        - Title word similarity
        
        Args:
            title: Title to find recommendations for
            number_of_recommendations: Number of recommendations to return
            
        Returns:
            List of (title, similarity_score) tuples
        """
        if title not in self.data_manager.data['title'].values:
            raise ValueError(f"Title '{title}' not found in dataset")

        # Get the reference movie data
        reference_movie = self.data_manager.data[
            self.data_manager.data['title'] == title].iloc[0].to_dict()
        
        # Calculate similarity with all other movies
        similarities = []
        for _, content in self.data_manager.data.iterrows():
            if content['title'] != title:
                similarity = self.similarity_calculator.calculate_content_similarity(
                    reference_movie,
                    content.to_dict()
                )
                similarities.append((content['title'], similarity))
        
        # Sort by similarity and return top N
        return sorted(similarities, key=lambda x: x[1], reverse=True)[:number_of_recommendations]


class UserBasedRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        """Initialize the user-based recommender."""
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator

    def recommend_from_ratings(self, user_ratings: Dict[str, float], number_of_recommendations: int) -> List[Tuple[str, float]]:
        """
        Recommend content based on user ratings.
        
        Args:
            user_ratings: Dictionary mapping title to rating (1-5)
            number_of_recommendations: Number of recommendations to return
            
        Returns:
            List of (title, score) tuples
        """
        if not user_ratings:
            return []
            
        recommendations = []
        
        # For each unrated movie, calculate a weighted similarity score
        for _, content in self.data_manager.data.iterrows():
            title = content['title']
            if title in user_ratings:
                continue
                
            total_score = 0.0
            for rated_title, rating in user_ratings.items():
                rated_movie = self.data_manager.data[
                    self.data_manager.data['title'] == rated_title].iloc[0].to_dict()
                
                similarity = self.similarity_calculator.calculate_content_similarity(
                    rated_movie,
                    content.to_dict()
                )
                total_score += similarity * (rating / 5.0)  # Normalize rating to 0-1 range
            
            recommendations.append((title, total_score))
        
        # Sort by score and return top N
        return sorted(recommendations, key=lambda x: x[1], reverse=True)[:number_of_recommendations]
