from typing import Dict, List
from recommender import ContentRecommender, UserBasedRecommender


class HybridRecommender:
    def __init__(self, content_recommender: ContentRecommender, 
                 user_based_recommender: UserBasedRecommender):
        self.content_recommender = content_recommender
        self.user_based_recommender = user_based_recommender

    def get_recommendations(self, title: str, user_ratings: Dict[str, float], 
                          count: int = 5) -> List[str]:
        content_recommendations = self.content_recommender.find_similar_content(title)
        user_recommendations = self.user_based_recommender.recommend_from_ratings(user_ratings)
        
        combined_scores = {}
        for title, score in content_recommendations:
            combined_scores[title] = score * 0.5
        for title, score in user_recommendations:
            combined_scores[title] = combined_scores.get(title, 0) + score * 0.5
                
        sorted_recommendations = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
        return [title for title, _ in sorted_recommendations[:count]]
    