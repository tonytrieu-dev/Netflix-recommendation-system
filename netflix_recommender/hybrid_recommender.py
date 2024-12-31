from typing import Dict, List
from netflix_recommender.recommender import ContentBasedRecommender
from netflix_recommender.data_manager import DataManager


class HybridRecommender:
    def __init__(self, content_recommender: ContentBasedRecommender, 
                 user_based_recommender: UserBasedRecommender):
        self.content_recommender = content_recommender
        self.user_based_recommender = user_based_recommender

    def get_recommendations(self, title: str, user_ratings: Dict[str, float], 
                          count: int) -> List[str]:
        content_recommendations = self.content_recommender.find_similar_content(title, count)
        user_recommendations = self.user_based_recommender.recommend_from_ratings(user_ratings, count)
        
        combined_scores = {}
        for title, score in content_recommendations:
            combined_scores[title] = score * 0.5
        for title, score in user_recommendations:
            combined_scores[title] = combined_scores.get(title, 0) + score * 0.5
                
        sorted_recommendations = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        return [title for title, _ in sorted_recommendations[:count]]