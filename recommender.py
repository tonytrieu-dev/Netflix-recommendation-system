from data_manager import DataManager
from similarity import SimilarityCalculator
from typing import Dict, List
import pandas as pd


class ContentRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator

    def find_similar_content(self, title: str, count: int) -> List[tuple]:
        reference_description = self.data_manager.data[
            self.data_manager.data['title'] == title]['description'].iloc[0]
        
        similarities = []
        for _, content in self.data_manager.data.iterrows():
            if content['title'] != title:
                similarity = self.similarity_calculator.calculate_text_similarity(reference_description, content['description'])
                similarities.append((content['title'], similarity))
        
        return sorted(similarities, key=lambda x: x[1], reverse=True)[:count]

class UserBasedRecommender:
    def __init__(self, data_manager: DataManager, similarity_calculator: SimilarityCalculator):
        self.data_manager = data_manager
        self.similarity_calculator = similarity_calculator

    def recommend_from_ratings(self, user_ratings: Dict[str, float], count: int) -> List[tuple]:
        if not user_ratings:
            return []
            
        recommendations = []
        for _, content in self.data_manager.data.iterrows():
            title = content['title']
            if title in user_ratings:
                continue
                
            total_score = self.calculate_rating_score(content, user_ratings)
            recommendations.append((title, total_score))
            
        return sorted(recommendations, key=lambda x: x[1], reverse=True)[:count]

    def calculate_rating_score(self, content: pd.Series, user_ratings: Dict[str, float]) -> float:
        total_score = 0
        for rated_title, rating in user_ratings.items():
            rated_description = self.data_manager.data[self.data_manager.data['title'] == rated_title]['description'].iloc[0]
            similarity = self.similarity_calculator.calculate_text_similarity(rated_description, content['description'])
            total_score += similarity * (rating / 10.0)
        return total_score
    
